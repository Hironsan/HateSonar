"""Baseline model."""

import argparse
from pathlib import Path

import pandas as pd
from skl2onnx import to_onnx
from skl2onnx.common.data_types import StringTensorType
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def main(args: argparse.Namespace) -> None:
    """Main function."""
    print("Loading dataset...")
    df = pd.read_csv(args.dataset)
    x, y = df["tweet"], df["class"]
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=args.test_size,
        random_state=42,
    )

    print("Fitting...")
    clf = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer()),
            ("logreg", LogisticRegression(penalty="l1", solver="saga", max_iter=1000)),
        ],
    )
    clf.fit(x_train, y_train)

    print("Saving...")
    onnx_model = to_onnx(
        clf,
        initial_types=[("text", StringTensorType([None]))],  # type: ignore
        target_opset=21,
    )

    with args.model_file.open("wb") as f:
        f.write(onnx_model.SerializeToString())  # type: ignore

    if args.test_size > 0.0:
        print("Predicting...")
        y_pred = clf.predict(x_test)
        print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    DATA_DIR = Path(__file__).parent.parent / "data"
    SAVE_DIR = Path(__file__).parent / "model"
    parser = argparse.ArgumentParser(description="Training a classifier")
    parser.add_argument(
        "--dataset",
        default=DATA_DIR / "labeled_data.csv",
        help="dataset",
    )
    parser.add_argument(
        "--model_file",
        default=SAVE_DIR / "model.onnx",
        help="model file",
    )
    parser.add_argument("--test_size", type=float, default=0.3, help="test data size")
    args = parser.parse_args()
    main(args)

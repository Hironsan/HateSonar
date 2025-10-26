"""Model API."""

from pathlib import Path
from typing import Any, TypedDict

import numpy as np
import onnxruntime as ort

DEFAULT_MODEL_FILE = Path(__file__).parent / "model" / "model.onnx"


class ClassConfidence(TypedDict):
    """Class confidence dictionary."""

    class_name: str
    confidence: float


class PredictionResult(TypedDict):
    """Prediction result dictionary."""

    text: str
    top_class: str
    classes: list[ClassConfidence]


class Sonar:
    """HateSonar API class."""

    def __init__(self, model_file: Path = DEFAULT_MODEL_FILE) -> None:
        """Initialize Sonar with ONNX model.

        Args:
            model_file (Path): Path to the ONNX model file.
        """
        self.sess = ort.InferenceSession(model_file, providers=["CPUExecutionProvider"])
        self.mapping = {0: "hate_speech", 1: "offensive_language", 2: "neither"}

    def ping(self, text: str) -> PredictionResult:
        """Predict hate speech from text.

        Args:
            text (str): Input text.

        Returns:
            PredictionResult: Prediction results.
        """
        test_inputs = np.array([text], dtype=object)
        outputs: list[Any] = self.sess.run(None, {"text": test_inputs})  # type: ignore
        labels, probs = outputs
        return {
            "text": text,
            "top_class": self.mapping[labels[0]],
            "classes": [{"class_name": self.mapping[k], "confidence": probs[0][k]} for k in sorted(self.mapping)],
        }

"""
Model API.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import joblib
import numpy as np


class Sonar(object):

    def __init__(self):
        BASE_DIR = os.path.join(os.path.dirname(__file__), './data')
        model_file = os.path.join(BASE_DIR, 'model.joblib')
        preprocessor_file = os.path.join(BASE_DIR, 'preprocess.joblib')
        self.estimator = joblib.load(model_file)
        self.preprocessor = joblib.load(preprocessor_file)

    def ping(self, text):
        assert isinstance(text, str)

        vector = self.preprocessor.transform([text])
        proba = self.estimator.predict_proba(vector)[0]
        mapping = {0: 'hate_speech', 1: 'offensive_language', 2: 'neither'}

        res = {
            'text': text,
            'top_class': mapping[np.argmax(proba)],
            'classes': [
                {'class_name': mapping[k],
                 'confidence': proba[k]}
                for k in sorted(mapping)
            ]
        }

        return res

    def get_weights(self, text):

        def get_class_idx():
            res = self.ping(text)
            for i, class_ in enumerate(res['classes']):
                if class_['class_name'] == res['top_class']:
                    return i

        class_idx = get_class_idx()
        features = self.preprocessor.get_feature_names()
        weights = self.estimator.coef_[class_idx]
        word2weight = {f: w for f, w in zip(features, weights)}
        tokenize = self.preprocessor.build_analyzer()
        words = tokenize(text)

        return {w: word2weight.get(w, 0) for w in words}

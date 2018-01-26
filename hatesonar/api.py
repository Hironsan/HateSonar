"""
Model API.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Sonar(object):

    def __init__(self):
        pass

    def ping(self, text):
        res = {
            "text": text,
            "top_class": "temperature",
            "classes": [{
                "class_name": "temperature",
                "confidence": 0.9998201258549781
            }, {
                "class_name": "conditions",
                "confidence": 1.7987414502176904E-4
            }]
        }

        return res

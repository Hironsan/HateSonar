# HateSonar: Hate Speech Detection

HateSonar is the *hate speech detection* library for Python.

Behold, the power of HateSonar:

```python
>>> from hatesonar import Sonar
>>> sonar = Sonar()
>>> sonar.ping(text="At least I'm not a nigger")
{
  "text" : "At least I'm not a nigger",
  "top_class" : "hate_speech",
  "classes" : [ {
    "class_name" : "hate_speech",
    "confidence" : 0.6001793646345871
  }, {
    "class_name" : "offensive_language",
    "confidence" : 0.399548534507691
  }, {
    "class_name": "neither",
    "confidence": 0.0002721008577219325
  } ]
}
```

HateSonar allows you to detect hate speech and offensive language in text, without the need for training. There's no need to train the model. You have only to fed text into HateSonar. It detects hate speech with the confidence score.

[BERT based model](https://colab.research.google.com/drive/1K4bH_vot_W9XXjlw9O-2ucROW9N4ZoDN?usp=sharing)

## Feature Support

* Hate speech and offensive language detection

HateSonar officially supports Python 3.10+

## Installation

To install HateSonar, simply use `pip`:

```bash
pip install hatesonar
```

## Reference

Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017. "Automated Hate Speech Detection and the Problem of Offensive Language." ICWSM.

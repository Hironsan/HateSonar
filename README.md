# HateSonar: Hate Speech Detection
HateSonar is the *hate speech detection* library for Python.

![Demo Image.](https://www.pakutaso.com/shared/img/thumb/doiteneko171027_TP_V.jpg)

<!--
https://www.pakutaso.com/20171036300post-13829.html
-->

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

HateSonar officially supports Python 3.9+

## Installation
To install HateSonar, simply use `pip`:

```bash
$ pip install hatesonar
```

<!--
## How to Contribute
1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
2. Fork the repository on GitHub to start making your changes to the master branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS.
-->

## Reference
Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017. "Automated Hate Speech Detection and the Problem of Offensive Language." ICWSM. 

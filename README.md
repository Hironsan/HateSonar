# HateSonar: Hate Speech Detection
HateSonar is the *hate speech detection* library for Python.

![Demo Image.](https://www.pakutaso.com/shared/img/thumb/doiteneko171027_TP_V.jpg)

<!--
https://www.pakutaso.com/20171036300post-13829.html
-->

Behold, the power of HateSonar:

```python
>>> import hatesonar
>>> sonar = hatesonar.Sonar()
>>> sonar.ping(text='How hot will it be today?')
{
  "text" : "How hot will it be today?",
  "top_class" : "temperature",
  "classes" : [ {
    "class_name" : "temperature",
    "confidence" : 0.9998201258549781
  }, {
    "class_name" : "conditions",
    "confidence" : 1.7987414502176904E-4
  } ]
}
```

HateSonar allows you to detect hate speech and offensive language in text, without the need for training. There's no need to train the model. You have only to fed text into HateSonar. It detects hate speech with the confidence score.

## Feature Support
* Hate speech and offensive language detection

HateSonar officially supports Python 2.7 & 3.4–3.6

## Installation
To install HateSonar, simply use `pip`:

```bash
$ pip install hatesonar
```

## How to Contribute
1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
2. Fork the repository on GitHub to start making your changes to the master branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS.

<!--
## Reference
Repository for Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017. "Automated Hate Speech Detection and the Problem of Offensive Language." ICWSM. 
-->
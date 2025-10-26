import unittest

from hatesonar.api import Sonar


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = "At least I'm not a nigger"

    def test_ping(self) -> None:
        sonar = Sonar()
        res = sonar.ping(self.text)
        assert "text" in res
        assert "top_class" in res
        assert "classes" in res
        assert isinstance(res["text"], str)
        assert isinstance(res["top_class"], str)
        assert isinstance(res["classes"], list)
        for d in res["classes"]:
            assert "class_name" in d
            assert "confidence" in d
            assert isinstance(d["class_name"], str)
            assert isinstance(d["confidence"], float)

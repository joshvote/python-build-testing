from src.consts import LONG_STRING, MEDIUM_STRING
from src.funcs import makeLonger, makeShorter


def test_makeShorter():
    assert makeShorter(None) == ""
    assert makeShorter("") == ""

    assert len(makeShorter(LONG_STRING)) < len(LONG_STRING)
    assert len(makeShorter(MEDIUM_STRING)) < len(MEDIUM_STRING)


def test_makeLonger():
    assert len(makeLonger(None)) > 0
    assert len(makeLonger("")) > 0

    assert len(makeLonger(LONG_STRING)) > len(LONG_STRING)
    assert len(makeLonger(MEDIUM_STRING)) > len(MEDIUM_STRING)

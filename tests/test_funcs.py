from src.consts import LONG_STRING, MEDIUM_STRING
from src.funcs import makeEvenLonger, makeLonger, makeShorter


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


def test_makeEvenLonger():
    assert len(makeEvenLonger(LONG_STRING)) > len(makeLonger(LONG_STRING))
    assert len(makeEvenLonger(MEDIUM_STRING)) > len(makeLonger(MEDIUM_STRING))


# def test_WillFail():
#    assert 1 == 0

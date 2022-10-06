from typing import Optional


def makeShorter(s: Optional[str]) -> str:
    if s is None or len(s) == 0:
        return ""

    return s[:-1]


def makeLonger(s: Optional[str]) -> str:
    if s is None or len(s) == 0:
        return "longer"

    return s + "longer"


def makeEvenLonger(s: Optional[str]) -> str:
    if s is None or len(s) == 0:
        return "evenlonger"

    return s + "evenlonger"

def addOne(s: Optional[int]) -> int:
    if s is None:
        return 0

    return s + 1

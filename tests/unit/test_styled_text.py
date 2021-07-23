"""
discord-styled-text - styler.py
---
Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from pytest import param, mark

from discord_styler import StyledText


StyledText_test_data = [
    param(["yo", "yo", "yo"], " ", "yo yo yo", id="basic")
]


@mark.parametrize("objs,sep,expected", StyledText_test_data)
def test_StyledText(objs, sep, expected):
    st = StyledText(*objs, sep=sep)
    assert str(st) == expected

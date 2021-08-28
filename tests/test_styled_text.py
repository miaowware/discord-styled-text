"""
discord-styled-text - test_styled_text.py
---
Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from pytest import param, mark

from discord_styler import StyledText, Italic, Bold, Underline, Strikethrough, InlineCode, Spoiler, BlockQuote


StyledText_test_data = [
    param(["yo", "yo", "yo"], " ", "yo yo yo", id="basic"),
    param(["yo", "yo", "yo"], ".", "yo.yo.yo", id="nondefault_sep"),
]


@mark.parametrize("objs,sep,expected", StyledText_test_data)
def test_StyledText(objs, sep, expected):
    styled = StyledText(*objs, sep=sep)
    assert str(styled) == expected


StyledText_single_word_test_data = [
    param("yo", StyledText, "yo", id="styledtext"),
    param("yo", Italic, "*yo*", id="italic"),
    param("yo", Bold, "**yo**", id="bold"),
    param("yo", Underline, "__yo__", id="underline"),
    param("yo", Strikethrough, "~~yo~~", id="strikethrough"),
    param("yo", InlineCode, "`yo`", id="inlinecode"),
    param("yo", Spoiler, "||yo||", id="spoiler"),
    param("yo", BlockQuote, "> yo\n", id="blockquote"),
]


@mark.parametrize("obj,cls,expected", StyledText_single_word_test_data)
def test_StyledText_single_word(obj, cls, expected):
    styled = cls(obj)
    assert str(styled) == expected


def test_BlockQuote_multiline():
    styled = BlockQuote("hello\nnewlines")
    expected = "> hello\n> newlines\n"
    assert str(styled) == expected

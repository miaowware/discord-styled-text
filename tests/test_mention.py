"""
discord-styled-text - test_mention.py
---
Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from pytest import param, mark, raises

from discord_styler import UserMention, RoleMention, ChannelMention


UserMention_test_data = [
    param(123456789, False, "<@123456789>", id="default"),
    param(123456789, True, "<@!123456789>", id="nickname"),
]


@mark.parametrize("id,nickname,expected", UserMention_test_data)
def test_UserMention(id, nickname, expected):
    mention = UserMention(id=id, nickname=nickname)
    assert str(mention) == expected


def test_RoleMention():
    mention = RoleMention(id=123456789)
    expected = "<@&123456789>"
    assert str(mention) == expected


def test_ChannelMention():
    mention = ChannelMention(id=123456789)
    expected = "<#123456789>"
    assert str(mention) == expected


Mention_exception_test_data = [
    param("yo", UserMention, id="str_user"),
    param("yo", RoleMention, id="str_role"),
    param("yo", ChannelMention, id="str_channel"),
    param(4.20, UserMention, id="float_user"),
    param(4.20, RoleMention, id="float_role"),
    param(4.20, ChannelMention, id="float_channel"),
]


@mark.parametrize("id,cls", Mention_exception_test_data)
def test_Mention_exception(id, cls):
    with raises(ValueError):
        cls(id=id)

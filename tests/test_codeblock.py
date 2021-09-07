"""
discord-styled-text - test_codeblock.py
---
Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from pytest import param, mark

from discord_styler import CodeBlock


CodeBlock_test_cases = [
    param("", None, "```\n\n```", id="empty_no_lang"),
    param("", "py", "```py\n\n```", id="empty_with_lang"),
    param("yolo", "", "```\nyolo\n```", id="str_empty_lang"),
    param('>>> Bold("hello", "world")\n\'**hello world**\'', None,
          '```\n>>> Bold("hello", "world")\n\'**hello world**\'\n```', id="no_lang"),
    param('>>> Bold("hello", "world")\n\'**hello world**\'', "py",
          '```py\n>>> Bold("hello", "world")\n\'**hello world**\'\n```', id="with_lang"),
]


@mark.parametrize("content,lang,expected", CodeBlock_test_cases)
def test_CodeBlock(content, lang, expected):
    code = CodeBlock(code=content, lang=lang)
    assert str(code) == expected

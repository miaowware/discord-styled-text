"""
discord-styled-text - test_escape.py
---
Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from pytest import param, mark

from discord_styler import escape_everything, escape_markdown, escape_mentions


md_test_data = [
    param(r"*some italic* **bold** \*pre-escaped\* ~~ __ || ``", False,
          r"\*some italic\* \*\*bold\*\* \*pre-escaped\* \~\~ \_\_ \|\| \`\`", id="inline_md_text"),
    param("> this is some text\n>>> here's some text too\n>> this shouldn't be escaped", False,
          "\\> this is some text\n\\>>> here's some text too\n>> this shouldn't be escaped", id="blockquote"),
    param("<t:12345>", False, "<t:12345>", id="timestamp"),
    param("<t:12345:f>", False, "<t:12345:f>", id="timestamp_with_format"),
    param("<t:12345>", True, "\\<t:12345>", id="esc_timestamp"),
    param("<t:12345:f>", True, "\\<t:12345:f>", id="esc_timestamp_with_format"),
]


@mark.parametrize("text,esc_timestamps,expected", md_test_data)
def test_escape_markdown(text, esc_timestamps, expected):
    escaped = escape_markdown(text, esc_timestamps=esc_timestamps)
    assert escaped == expected


mentions_test_data = [
    param("<@123456>", False, "<@\u200b123456>", id="username"),
    param("<@!12345>", False, "<@!\u200b12345>", id="nickname"),
    param("<@&12345>", False, "<@&\u200b12345>", id="role"),
    param("<#123456>", False, "<#123456>", id="channel"),
    param("@everyone @here", False, "@\u200beveryone @\u200bhere", id="everyone_here"),
    param("<@123456>", True, "<@\u200b123456>", id="esc_chan_username"),
    param("<@!12345>", True, "<@!\u200b12345>", id="esc_chan_nickname"),
    param("<@&12345>", True, "<@&\u200b12345>", id="esc_chan_role"),
    param("<#123456>", True, "<#\u200b123456>", id="esc_chan_channel"),
]


@mark.parametrize("text,esc_channels,expected", mentions_test_data)
def test_escape_mentions(text, esc_channels, expected):
    escaped = escape_mentions(text, esc_channels=esc_channels)
    assert escaped == expected


ET_TEXT = "1 * 1 = 2, but 1 ** 2 = 4. <@!1234567890> @everyone "
ET_CHAN = "<#123456789> "
ET_TS = "<t:123456:f>"
ET = ET_TEXT + ET_CHAN + ET_TS
ET_ESC_TEXT = "1 \\* 1 = 2, but 1 \\*\\* 2 = 4. <@!\u200b1234567890> @\u200beveryone "
ET_ESC_CHAN = "<#\u200b123456789> "
ET_ESC_TS = "\\<t:123456:f>"


everything_test_data = [
    param(ET, False, False, ET_ESC_TEXT + ET_CHAN + ET_TS, id="no_channel_ts"),
    param(ET, True, False, ET_ESC_TEXT + ET_CHAN + ET_ESC_TS, id="no_channel"),
    param(ET, False, True, ET_ESC_TEXT + ET_ESC_CHAN + ET_TS, id="no_ts"),
    param(ET, True, True, ET_ESC_TEXT + ET_ESC_CHAN + ET_ESC_TS, id="everything"),
]


@mark.parametrize("text,esc_timestamps,esc_channels,expected", everything_test_data)
def test_escape_everything(text, esc_timestamps, esc_channels, expected):
    escaped = escape_everything(text, esc_timestamps=esc_timestamps, esc_channels=esc_channels)
    assert escaped == expected

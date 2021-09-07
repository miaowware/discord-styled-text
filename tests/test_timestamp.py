"""
discord-styled-text - test_timestamp.py
---
Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from datetime import datetime, timezone, timedelta

from pytest import param, mark, raises

from discord_styler import TimeStamp, TimeStyle


UserMention_test_data = [
    param(123456789, None, "<t:123456789>", id="int_default"),
    param(123456789, TimeStyle.ShortTime, "<t:123456789:t>", id="int_short_time"),
    param(123456789, TimeStyle.LongTime, "<t:123456789:T>", id="int_long_time"),
    param(123456789, TimeStyle.ShortDate, "<t:123456789:d>", id="int_short_date"),
    param(123456789, TimeStyle.LongDate, "<t:123456789:D>", id="int_long_date"),
    param(123456789, TimeStyle.ShortDateTime, "<t:123456789:f>", id="int_short_date_time"),
    param(123456789, TimeStyle.LongDateTime, "<t:123456789:F>", id="int_long_date_time"),
    param(123456789, TimeStyle.Relative, "<t:123456789:R>", id="int_relative"),
    param(datetime.fromtimestamp(123456789), None, "<t:123456789>", id="datetime_naive"),
    param(datetime.fromtimestamp(123456789, tz=timezone(timedelta(hours=4))), None,
          "<t:123456789>", id="datetime_with_tz"),
]


@mark.parametrize("time,style,expected", UserMention_test_data)
def test_UserMention(time, style, expected):
    timestamp = TimeStamp(time=time, style=style)
    assert str(timestamp) == expected


TimeStamp_exception_test_data = [
    param("yo", id="str"),
    param(4.20, id="float"),
]


@mark.parametrize("time", TimeStamp_exception_test_data)
def test_TimeStamp_exception(time):
    with raises(ValueError):
        TimeStamp(time=time)

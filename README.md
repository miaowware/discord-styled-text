# discord-styled-text

A small library to style text for Discord without having to remember any syntax

[![PyPI](https://img.shields.io/pypi/v/discord-styled-text)](https://pypi.org/project/discord-styled-text/) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/discord-styled-text) ![PyPI - License](https://img.shields.io/pypi/l/discord-styled-text) [![Documentation Status](https://readthedocs.org/projects/discord-styled-text/badge/?version=latest)](https://discord-styled-text.miaow.io/en/latest/?badge=latest)

## Installation

`discord-styled-text` requires Python 3.6 at minimum.

```none
$ pip install discord-styled-text
```

## Documentation

Documentation is available on [ReadTheDocs](https://discord-styled-text.miaow.io/).

## Example Usage

```py
>>> from discord_styler import *

>>> bold_text = Bold("Here's some bold text")
>>> italic_text = Italic("and here's some", Underline("italic text"), "with nested styles!")
>>> text = StyledText("We can combine them:", bold_text, italic_text)
>>> str(text)
"We can combine them: **Here's some bold text** *and here's some __italic text__ with nested styles!*"

>>> quoted = StyledText(BlockQuote(text), "and we can do quotes too")
>>> str(quoted)
"> We can combine them: **Here's some bold text** *and here's some __italic text__ with nested styles!*\n and we can do quotes too"

>>> question = StyledText(
...     UserMention(200102491231092736),
...     f"will you be free at {TimeStamp(1618953630, TimeStyle.LongDateTime)}?",
...     f"I'll be doing code review in {ChannelMention(656893570711814145)} if you wanna join")
>>> str(question)
"<@200102491231092736> will you be free at <t:1618953630:F>? I'll be doing code review in <#656893570711814145> if you wanna join"

>>> link = NonEmbeddingURL("https://github.com/miaowware/discord-styled-text/pull/1")
>>> str(link)
'<https://github.com/miaowware/discord-styled-text/pull/1>'

>>> code = StyledText(
...     "What do you think of this?\n",
...     CodeBlock('def __str__(self) -> str:\n        return "||" + super().__str__() + "||"', lang="py"))
>>> str(code)
'What do you think of this?\n ```py\ndef __str__(self) -> str:\n        return "||" + super().__str__() + "||"\n```'
```

![The output of the example, rendered in Discord](/docs/discord_screenshot.png)

## Copyright

Copyright 2021 classabbyamp, 0x5c  
Released under the BSD 3-Clause License.  
See [`LICENSE`](LICENSE) for the full license text.

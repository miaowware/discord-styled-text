"""
discord-styled-text
---
A small library to style text for Discord without having to remember any syntax

Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from .__info__ import __version__  # noqa: F401
from .styler import StyledText, Italic, Bold, Underline, Strikethrough, InlineCode, Spoiler, BlockQuote  # noqa: F401
from .styler import CodeBlock  # noqa: F401
from .styler import TitledURL, NonEmbeddingURL  # noqa: F401
from .styler import MentionABC, UserMention, RoleMention, ChannelMention  # noqa: F401
from .styler import TimeStyle, TimeStamp  # noqa: F401

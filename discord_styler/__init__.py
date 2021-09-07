"""
discord-styled-text
---
A small library to style text for Discord without having to remember any syntax

Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from .__info__ import __version__
from .styler import StyledText, Italic, Bold, Underline, Strikethrough, InlineCode, Spoiler, BlockQuote
from .styler import CodeBlock
from .styler import TitledURL, NonEmbeddingURL
from .styler import MentionABC, UserMention, RoleMention, ChannelMention
from .styler import TimeStyle, TimeStamp
from .escape import escape_markdown, escape_mentions, escape_everything

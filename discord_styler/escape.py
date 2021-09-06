"""
discord-styled-text - escape.py
---
Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""

import re


__all__ = [
    "escape_markdown",
    "escape_mentions",
    "escape_everything",
]


INLINE_MD_RE = re.compile(r"(?P<bs>(?<!\\)(?:\\\\)*)(?P<char>[_*~|`])")
INLINE_MD_SUB = r"\g<bs>\\\g<char>"

BLOCKQUOTE_RE = re.compile(r"^>(?=(>>)? )", flags=re.MULTILINE)
TIMESTAMP_RE = re.compile(r"<t:[0-9]+(?::[a-zA-Z])?>")
GENERIC_SUB = r"\\\g<0>"

USER_ROLE_CHANNEL_RE = re.compile(r"<(@[!&]?|#)([0-9]+)>")
USER_ROLE_RE = re.compile(r"<(@[!&]?)([0-9]+)>")
MENTION_SUB = "<\\g<1>\u200b\\g<2>>"  # this cannot be a raw string because of the \u200b

EVERYONE_HERE_RE = re.compile(r"@(everyone|here)", flags=re.IGNORECASE)
EVERYONE_HERE_SUB = "@\u200b\\g<1>"  # this cannot be a raw string because of the \u200b


def escape_markdown(text: str, *, esc_timestamps: bool = True) -> str:
    """Utility function to escape markdown-like formatting in a string

    :param text: the text to escape
    :param esc_timestamps: whether to escape timestamp formatting in the text
    """
    text = re.sub(INLINE_MD_RE, INLINE_MD_SUB, text)
    text = re.sub(BLOCKQUOTE_RE, GENERIC_SUB, text)
    if esc_timestamps:
        text = re.sub(TIMESTAMP_RE, GENERIC_SUB, text)
    return text


def escape_mentions(text: str, *, esc_channels: bool = True) -> str:
    """Utility function to escape all mentions in the text

    Escapes user, role, everyone/here, and optionally, channel mentions.
    Escaping done by adding a non-breaking space (``\\u200b``) between the
    mention symbol (``@``/``@!``/``@&``/``#``) and the identifier (ID/``everyone``/``here``).

    :param text: the text to escape
    :param esc_channels: whether to escape channel mentions in the text
    """
    text = re.sub(EVERYONE_HERE_RE, EVERYONE_HERE_SUB, text)
    if esc_channels:
        text = re.sub(USER_ROLE_CHANNEL_RE, MENTION_SUB, text)
    else:
        text = re.sub(USER_ROLE_RE, MENTION_SUB, text)
    return text


def escape_everything(text: str, *, esc_timestamps: bool = True, esc_channels: bool = True) -> str:
    """Utility function to escape all special formatting and mentions

    Exactly the same as running both :func:`escape_markdown` and :func:`escape_mentions`.
    Provided as a convenience shortcut.

    :param text: the text to escape
    :param esc_timestamps: whether to escape timestamp formatting in the text
    :param esc_channels: whether to escape channel mentions in the text
    """
    return escape_mentions(escape_markdown(text, esc_timestamps=esc_timestamps),
                           esc_channels=esc_channels)

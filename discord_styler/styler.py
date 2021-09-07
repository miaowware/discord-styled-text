"""
discord-styled-text - styler.py
---
Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from abc import ABC, abstractmethod
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Union


__all__ = [
    "StyledText",
    "Italic",
    "Bold",
    "Underline",
    "Strikethrough",
    "InlineCode",
    "Spoiler",
    "BlockQuote",
    "CodeBlock",
    "TitledURL",
    "NonEmbeddingURL",
    "UserMention",
    "RoleMention",
    "ChannelMention",
    "TimeStyle",
    "TimeStamp",
]


ALLOWED_URL_SCHEMES = ("http://", "https://", "steam://")


# ---- Text Styles ----

class StyledText:
    """Container for styled text

    Strignifies and concatenates all given objects to simplify style composition.
    All subclasses follow the same logic while adding their markup.

    :param objects: Objects to style
    :param sep: The separator to use, defaults to a space
    """
    def __init__(self, *objects: Any, sep: str = " "):
        self.__objs = objects
        self.__sep = sep

    def __str__(self) -> str:
        return self.__sep.join(str(x) for x in self.__objs)


class Italic(StyledText):
    """Applies italic formatting to the objects using :class:`StyledText` logic

    Takes the same parameters as :class:`StyledText`.
    """
    def __str__(self) -> str:
        return "*" + super().__str__() + "*"


class Bold(StyledText):
    """Applies bold formatting to the objects using :class:`StyledText` logic

    Takes the same parameters as :class:`StyledText`.
    """
    def __str__(self) -> str:
        return "**" + super().__str__() + "**"


class Underline(StyledText):
    """Applies underline formatting to the objects using :class:`StyledText` logic

    Takes the same parameters as :class:`StyledText`.
    """
    def __str__(self) -> str:
        return "__" + super().__str__() + "__"


class Strikethrough(StyledText):
    """Applies strikethrough formatting to the objects using :class:`StyledText` logic

    Takes the same parameters as :class:`StyledText`.
    """
    def __str__(self) -> str:
        return "~~" + super().__str__() + "~~"


class InlineCode(StyledText):
    """Applies inline code block formatting to the objects using :class:`StyledText` logic

    Takes the same parameters as :class:`StyledText`.
    """
    def __str__(self) -> str:
        return "`" + super().__str__() + "`"


class Spoiler(StyledText):
    """Applies spoiler formatting to the objects using :class:`StyledText` logic

    Takes the same parameters as :class:`StyledText`.
    """
    def __str__(self) -> str:
        return "||" + super().__str__() + "||"


class BlockQuote(StyledText):
    """Applies block quote styling to the objects using :class:`StyledText` logic

    All newlines will be appended with a ``>`` and a space.
    The inner text will be prepended with a ``>`` and space and appended with a ``\\n``.

    Takes the same parameters as :class:`StyledText`.
    """
    def __str__(self) -> str:
        # the final newline is intended because otherwise the text
        # after the blockquote will still be blockquoted
        return "> " + super().__str__().replace("\n", "\n> ") + "\n"


# ---- Code Blocks ----

class CodeBlock:
    """Wraps the given code in a code block, optionally with language highlighting

    :param code: The contents of the code block
    :param lang: The language code of the code block, left unspecified in the generated markup if absent
    """
    def __init__(self, code: str, lang: str = None):
        self.__code = code
        self.__lang = lang if lang else ""

    def __str__(self) -> str:
        return f"```{self.__lang}\n{self.__code}\n```"


# ---- URLs ----

class TitledURL:
    """URL with title

    This only works inside embeds.

    :param title: The text to use as the link title
    :param url: The URL. Must be http or https protocol
    """
    def __init__(self, title: Union[str, StyledText], url: str):
        self.__title = title
        # Discord will only render http(s) and steam URLs
        if not url.lower().startswith(ALLOWED_URL_SCHEMES):
            raise ValueError(f"The URL must start with one of: {', '.join(ALLOWED_URL_SCHEMES)}")
        self.__url = url

    def __str__(self) -> str:
        return f"[{self.__title}]({self.__url})"


class NonEmbeddingURL:
    """Non-embedding URL

    URL which Discord will not generate an embed for.

    :param url: The URL. Must be http or https protocol
    """
    def __init__(self, url: str):
        # Discord will only render http(s) and steam URLs
        if not url.lower().startswith(ALLOWED_URL_SCHEMES):
            raise ValueError(f"The URL must start with one of: {', '.join(ALLOWED_URL_SCHEMES)}")
        self.__url = url

    def __str__(self) -> str:
        return "<" + self.__url + ">"


# ---- Mentions ----

class MentionABC(ABC):
    """Abstract base class for mention ID formatters

    Cannot be directly instantiated. Subclasses must implement ``__str__()``.

    :param id: The ID to mention
    """
    def __init__(self, id: int):
        if not isinstance(id, int):
            raise ValueError("The ID must be an integer!")
        self._id = id

    @abstractmethod
    def __str__(self) -> str:
        pass


class UserMention(MentionABC):
    """User mention formatter

    Creates a user mention for the given ID.
    If using this library in a discord.py bot/client, we recommend using ``User.mention`` when possible.

    :param id: The ID to mention
    :param nickname: Whether to use the "nickname" format instead.
        Currently, this changes nothing in the client and always renders the nickname if it exists
    """
    def __init__(self, id: int, nickname: bool = False):
        super().__init__(id)
        self.__nickname = nickname

    def __str__(self) -> str:
        return f"<@{'!' if self.__nickname else ''}{self._id}>"


class RoleMention(MentionABC):
    """Role mention formatter

    Creates a role mention for the given ID.
    If using this library in a discord.py bot/client, we recommend using ``Role.mention`` when possible.

    :param id: The ID to mention
    """
    def __str__(self) -> str:
        return f"<@&{self._id}>"


class ChannelMention(MentionABC):
    """Channel mention formatter

    Creates a channel mention for the given ID.
    If using this library in a discord.py bot/client, we recommend using ``GuildChannel.mention`` when possible.

    :param id: The ID to mention
    """
    def __str__(self) -> str:
        return f"<#{self._id}>"


# ---- Time ----

class TimeStyle(Enum):
    """Timestamp styles for :class:`TimeStamp`"""
    ShortTime = "t"
    LongTime = "T"
    ShortDate = "d"
    LongDate = "D"
    ShortDateTime = "f"
    LongDateTime = "F"
    Relative = "R"


class TimeStamp:
    """Creates a smart timestamp

    Renders on the client according to the selected style and the client's locale and timezone.
    The style used when left unspecified and the specifics of each styles are entirely controlled by Discord.

    `Timestamp Styles`_ (Discord API Docs)

    .. _Timestamp Styles: https://discord.com/developers/docs/reference#message-formatting-timestamp-styles

    :param time: The UNIX timestamp (in seconds)
    :param style: The smart timestamp style to use
    """
    def __init__(self, time: Union[int, datetime], style: TimeStyle = None):
        if isinstance(time, int):
            self.__time = datetime.fromtimestamp(time, tz=timezone.utc)
        elif isinstance(time, datetime):
            if time.tzinfo != timezone.utc:
                self.__time = time.astimezone(timezone.utc)
            else:
                self.__time = time
        else:
            raise ValueError("The time must be an int or a datetime object!")
        self.__style = style

    def __str__(self):
        return f"<t:{self.__time.timestamp():.0f}{':' + self.__style.value if self.__style is not None else ''}>"

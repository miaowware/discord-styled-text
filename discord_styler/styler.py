from typing import Union
from datetime import datetime, timezone
from enum import Enum

# TODO:
# - escaping text
# - write tests
# - clean up repo
# - write docs


class TimeStyle(Enum):
    ShortTime = "t"
    LongTime = "T"
    ShortDate = "d"
    LongDate = "D"
    ShortDateTime = "f"
    LongDateTime = "F"
    Relative = "R"


class StyledText:
    def __init__(self, *objects, sep=" "):
        self.__objs = objects
        self.__sep = sep

    def __str__(self):
        return self.__sep.join(self.__objs)


class Italic(StyledText):
    def __str__(self):
        return "*" + super().__str__() + "*"


class Bold(StyledText):
    def __str__(self):
        return "**" + super().__str__() + "**"


class Underline(StyledText):
    def __str__(self):
        return "__" + super().__str__() + "__"


class Strikethrough(StyledText):
    def __str__(self):
        return "~~" + super().__str__() + "~~"


class InlineCode(StyledText):
    def __str__(self):
        return "`" + super().__str__() + "`"


class Spoiler(StyledText):
    def __str__(self):
        return "||" + super().__str__() + "||"


class CodeBlock:
    def __init__(self, code: str, lang: str = None):
        self.__code = code
        self.__lang = lang

    def __str__(self) -> str:
        return f"```{self.__lang}\n" + self.__code + "\n```"


# ---- URLs ----

class TitledURL:
    def __init__(self, title: Union[str, StyledText], url: str):
        self.__title = title
        # TODO: Check URL validity?
        if not url.lower().startswith("http://") or not url.lower().startswith("https://"):
            raise ValueError("The URL must be either HTTP or HTTPS!")
        self.__url = url

    def __str__(self) -> str:
        return f"[{self.__title}]({self.__url})"


class NonEmbeddingURL:
    def __init__(self, url: str):
        # TODO: Check URL validity?
        if not url.lower().startswith("http://") or not url.lower().startswith("https://"):
            raise ValueError("The URL must be either HTTP or HTTPS!")
        self.__url = url

    def __str__(self) -> str:
        return "<" + self.__url + ">"


# ---- Mentions ----

class Mention:
    def __init__(self, id: int):
        if not isinstance(id, int):
            raise ValueError("The ID must be an integer!")
        self.__id = id


class UserMention(Mention):
    def __init__(self, id: int, nickname: bool = False):
        super().__init__(id)
        self.__nickname = nickname

    def __str__(self) -> str:
        return f"<@{'!' if self.__nickname else ''}{self.__id}>"


class RoleMention(Mention):
    def __str__(self) -> str:
        return f"<@&{self.__id}>"


class ChannelMention(Mention):
    def __str__(self) -> str:
        return f"<#{self.__id}>"


# ---- Time ----

class TimeStamp:
    def __init__(self, time: Union[int, datetime], style: TimeStyle = None):
        if isinstance(time, int):
            self.__time = datetime.fromtimestamp(time, tz=timezone.utc)
        elif time.tzinfo != timezone.utc:
            self.__time = time.astimezone(timezone.utc)
        else:
            self.__time = time
        self.__style = style

    def __str__(self):
        return f"<t:{self.__time.timestamp():.0f}{':' + self.__style if self.__style is not None else ''}>"


"""
x User <@_>
x UserNickname <@!_>
x Role <@&_>
x Channel <#_>
"""

"""
X Italics *_* or _-_
X Bold **_**
X Underline __-__
X Strikethrough ~~_~~
X inline code `_`
X spoilers

block quotes

X titled URL (for embeds)
X non-embedding URL

X code blocks (with languages)
    ```lang
    _
    ```
x timestamp
    <t:UNIX_SEC_TIME>
    <t:UNIX_SEC_TIME:STYLE>
    STYLE is enum
"""

"""
unicode/custom/animated emoji?
"""

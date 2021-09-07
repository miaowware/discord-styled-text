"""
discord-styled-text - test_url.py
---
Copyright 2021 classabbyamp, 0x5c
Released under the terms of the BSD 3-Clause license.
"""


from pytest import param, mark, raises

from discord_styler import TitledURL, NonEmbeddingURL


TitledURL_test_data = [
    param("", "http://miaow.io", "[](http://miaow.io)", id="http_no_title"),
    param("", "https://miaow.io", "[](https://miaow.io)", id="https_no_title"),
    param("", "steam://friends/", "[](steam://friends/)", id="steam_no_title"),
    param("check this out", "http://miaow.io", "[check this out](http://miaow.io)", id="http_with_title"),
    param("check this out", "https://miaow.io", "[check this out](https://miaow.io)", id="https_with_title"),
    param("check this out", "steam://friends/", "[check this out](steam://friends/)", id="steam_with_title"),
]


@mark.parametrize("title,url,expected", TitledURL_test_data)
def test_TitledURL(title, url, expected):
    url_obj = TitledURL(title=title, url=url)
    assert str(url_obj) == expected


NonEmbeddingURL_test_data = [
    param("http://miaow.io", "<http://miaow.io>", id="http"),
    param("https://miaow.io", "<https://miaow.io>", id="https"),
    param("steam://friends/", "<steam://friends/>", id="steam"),
]


@mark.parametrize("url,expected", NonEmbeddingURL_test_data)
def test_NonEmbeddingURL(url, expected):
    url_obj = NonEmbeddingURL(url=url)
    assert str(url_obj) == expected


exception_test_data = [
    param("title", "", TitledURL, id="titled_no_url"),
    param(None, "", NonEmbeddingURL, id="nonembedding_no_url"),
    param("title", "notaurl.com", TitledURL, id="titled_no_scheme"),  # not aurl
    param(None, "notaurl.com", NonEmbeddingURL, id="nonembedding_no_scheme"),  # not aurl
    param("title", "ftps://example.com", TitledURL, id="titled_invalid_scheme"),
    param(None, "ftps://example.com", NonEmbeddingURL, id="nonembedding_invalid_scheme"),
]


@mark.parametrize("title,url,cls", exception_test_data)
def test_URL_exception(title, url, cls):
    with raises(ValueError):
        if title is not None:
            cls(title=title, url=url)
        else:
            cls(url=url)

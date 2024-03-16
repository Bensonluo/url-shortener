# coding: utf-8
"""
url tool
"""
import pyshorteners as shr

from urllib.parse import urlparse

encode_hmap = {}  # {"original": "shorter"}
decode_hmap = {}  # {"shorter: "original"}


def encode_url(url: str) -> str:
    """
    encoded(shorter) url
    """
    if url is None:
        return None
    global encode_hmap
    global decode_hmap

    # can an url be repeatedly shortened？
    # res = decode_hmap.get(url, None)
    # if res is not None:
    #     return res
    res = encode_hmap.get(url, None)
    if res is not None:
        return res
    else:
        shortener = shr.Shortener()
        res = shortener.tinyurl.short(url)
        encode_hmap[url] = res
        decode_hmap[res] = url
        return res


def decode_url(s_url) -> str:
    """
    decode shortened url to original
    """
    if s_url is None:
        return None
    global decode_hmap
    return decode_hmap.get(s_url, None)


def is_url(s):
    """
    check is a str valid url
    :param s:
    :return:
    """
    try:
        result = urlparse(s)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

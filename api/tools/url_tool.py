# coding: utf-8
"""
url tool
"""
import pyshorteners as shr

from urllib.parse import urlparse


def encode_url(url: str) -> str:
    """
    encoded(shorter) url
    """
    pass


def decode_url(s_url: str) -> str:
    """
    decode shortened url to original
    """
    pass


def is_url(s: str) -> bool:
    """
    check is a str valid url
    :param s:
    :return: bool
    """
    try:
        result = urlparse(s)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

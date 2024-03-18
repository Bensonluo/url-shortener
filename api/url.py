# coding: utf-8
"""
url api
"""
import logging

from flask import Blueprint, request, redirect
from api.tools.response import api_return
from api.tools.url_tool import encode_url, is_url, decode_url

bp = Blueprint('url', __name__, url_prefix='/url')


@bp.route("/encode", methods=["POST"])
def encode():
    """
    API encodes an url to a shorter version
    input:JSON original URLs in Body
    return:JSON shortened URLs in Body
    """
    pass


@bp.route("/decode", methods=["POST"])
def decode():
    """
    API decodes an url from shorter version to original
    input:JSON shortened URLs in Body
    return:JSON original URLs in Body
    """
    pass


@bp.route("/follow", methods=["POST"])
def follow():
    """
    This api redirects user to the original URL.
    input:JSON  shortened URLs in Body
    return:JSON
    """
    pass


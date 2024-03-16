# coding: utf-8
"""
url api
"""
from flask import Blueprint


bp = Blueprint('url_tool', __name__, url_prefix='/url')


@bp.route("/encode", methods=["POST"])
def encode():
    """
    encode an url to a shorter version
    :return:
    """
    return


@bp.route("/decode", methods=["POST"])
def decode():
    """
    decode an url from shorter version to original
    :return:
    """
    return


@bp.route("/follow", methods=["POST"])
def follow():
    """
    This api accepts previously shortened URLs.
    Redirects responses to the original URL.
    :return:
    """
    return

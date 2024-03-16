# coding: utf-8
"""
url api
"""
import logging

from flask import Blueprint, request, redirect
from api.tools.response import api_return
from api.tools.url_tool import encode_url, is_url, decode_url

bp = Blueprint('url_tool', __name__, url_prefix='/url')


@bp.route("/encode", methods=["POST"])
def encode():
    """
    API encodes an url to a shorter version
    input:JSON original URLs in Body
    return:JSON shortened URLs in Body
    """
    try:
        data = request.get_json()
    except Exception as e:
        logging.info(e)
        return api_return(400, "Bad Request")
    if data is None:
        logging.info("fail to load request data")
        return api_return(400, "Bad Request")

    url = data['url']
    if not is_url(url):
        logging.info("Invalid URL: {}".format(url))
        return api_return(400, "Bad Request", data="Invalid URL")

    s_url = encode_url(url)
    return api_return(200, s_url=s_url)


@bp.route("/decode", methods=["POST"])
def decode():
    """
    API decodes an url from shorter version to original
    input:JSON shortened URLs in Body
    return:JSON original URLs in Body
    """
    try:
        data = request.get_json()
    except Exception as e:
        logging.info(e)
        return api_return(400, "Bad Request")
    if data is None:
        return api_return(400, "Bad Request")

    s_url = data['s_url']
    if not is_url(s_url):
        logging.info("Invalid URL: {}".format(s_url))
        return api_return(400, "Bad Request", data="Invalid URL")
    url = decode_url(s_url)
    if url is None:
        logging.info("original url not found: {}".format(s_url))
        return api_return(200, "original url not found.", url=url)
    return api_return(200, url=url)


@bp.route("/follow", methods=["POST"])
def follow():
    """
    This api redirects user to the original URL.
    input:JSON  shortened URLs in Body
    return:JSON
    """
    try:
        data = request.get_json()
    except Exception as e:
        logging.info(e)
        return api_return(400, "Bad Request")
    if data is None:
        return api_return(400, "Bad Request")

    s_url = data['s_url']
    if not is_url(s_url):
        logging.info("Invalid URL: {}".format(s_url))
        return api_return(400, "Bad Request", data="Invalid URL")
    url = decode_url(s_url)
    if url is None:
        logging.info("original url not found: {}".format(s_url))
        return api_return(200, "original url not found.", url=url)
    return redirect(url)


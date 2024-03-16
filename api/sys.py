# coding: utf-8
"""
system api module
"""
import logging

from flask import Blueprint
from api.tools.response import api_return

bp = Blueprint('sys', __name__, url_prefix='/')


@bp.route("/")
def index():
    """
    basic check
    :return:
    """
    return api_return(200, data="Hello, world!")


@bp.route("/health")
def health():
    """
    health check
    :return:
    """
    return api_return(200, data="OK")


@bp.app_errorhandler(Exception)
def server_error(error):
    """
    server error handler
    :param error:
    :return:
    """
    logging.info(f"Got an error! {error}")
    return api_return(500, f"Got an error! {error}")

from flask import Blueprint, Response, jsonify, request

import logging

from tools.response import api_return

bp = Blueprint('sys', __name__, url_prefix='/')


@bp.route("/")
def index():
    return api_return(200, "Hello, world!")


@bp.route("/health")
def health():
    return api_return(200, "OK")


@bp.app_errorhandler(Exception)
def server_error(error):
    logging.info(f"Got an error! {error}")
    return api_return(500, f"Got an error! {error}")

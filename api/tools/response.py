# coding: utf-8
"""
response standardize tool
"""

import json
from flask import Response


RESPONSE_CODE_LIST = {
    -1: "unknown errors",
    200: "Success",
    400: "Bad Request",
    404: "Page not found",
    500: "Internal error"
}


def json_return(data):
    """
    jsonify
    :param data:
    :return:
    """
    return Response(
        json.dumps(data, separators=(",", ":")), status=data["code"], mimetype="application/json")


def api_return(code, msg=None, data=None, **kwargs):
    """
    api return wrapper
    :param code:
    :param msg:
    :param data:
    :param kwargs:
    :return:
    """
    if code not in RESPONSE_CODE_LIST.keys():
        code = -1
    if msg is None:
        msg = RESPONSE_CODE_LIST[code]
    if data is None:
        data = ""

    result = {"code": code, "msg": msg, "data": data}
    result.update(kwargs)
    return json_return(result)

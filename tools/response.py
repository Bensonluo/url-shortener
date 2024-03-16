# coding: utf-8
"""
response standardize tool
"""

import json
import decimal
import logging

from datetime import date, time, datetime
from flask import Response


RESPONSE_CODE_LIST = {
    -1: "unknown errors",
    200: "Success",
    400: "Bad Request",
    404: "Page not found",
    500: "Internal error"
}


class JsonEncoder(json.JSONEncoder):
    """
    json encoder
    """
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, time):
            return obj.strftime('%H:%M:%S')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return super().default(self, obj)


def json_return(data):
    """
    jsonify
    :param data:
    :return:
    """
    return Response(
        json.dumps(data, cls=JsonEncoder, separators=(",", ":")), mimetype="application/json")


def api_return(code, msg=None, data=None, **kwargs):
    """
    api return wrapper
    :param code:
    :param msg:
    :param data:
    :param kwargs:
    :return:
    """
    logging.info(code)

    if code not in RESPONSE_CODE_LIST.keys():
        logging.info(RESPONSE_CODE_LIST.keys())
        code = -1
    if msg is None:
        msg = RESPONSE_CODE_LIST[code]
    if data is None:
        data = ""

    result = {"code": code, "msg": msg, "data": data}
    result.update(kwargs)
    return json_return(result)

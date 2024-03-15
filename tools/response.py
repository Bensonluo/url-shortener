# coding: utf-8
"""
response tool
"""

import json
import decimal
from datetime import date, time, datetime

from flask import Response


RESPONSE_CODE_LIST = {
    "ERR": (-1, "unknown errors"),
    "OK": (200, "ok"),
    "SUCCESS": (200, "SUCCESS"),

    "CODE400": (400, "Bad Request"),
    "CODE404": (404, "Page not found"),
    "CODE500": (500, "Internal error"),
}


class JsonEncoder(json.JSONEncoder):
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
    return Response(json.dumps(data, cls=JsonEncoder, separators=(",", ":")), mimetype="application/json")


def api_return(code, msg=None, data=None, **kwargs):
    code = str(code).upper()
    if code not in RESPONSE_CODE_LIST.keys():
        code = "ERR"
    if msg is None:
        msg = RESPONSE_CODE_LIST[code][1]
    if data is None:
        data = ""

    result = {"code": RESPONSE_CODE_LIST[code][0], "msg": msg, "data": data}
    result.update(kwargs)
    return json_return(result)
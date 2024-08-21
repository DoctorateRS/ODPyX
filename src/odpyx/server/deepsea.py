from flask import request

from ..const import USER_JSON_PATH
from .util import read_json, write_json


def deepSeaBranch():
    request_data = request.get_json()["branches"]
    techTrees = {branch["techTreeId"]: {"branch": branch["branchId"], "state": 2} for branch in request_data}

    saved_data = read_json(USER_JSON_PATH)
    saved_data["user"]["deepSea"]["techTrees"] = techTrees
    write_json(saved_data, USER_JSON_PATH)

    data = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {"deepSea": {"techTrees": techTrees}},
        }
    }

    return data


def deepSeaEvent():
    data = {"playerDataDelta": {"deleted": {}, "modified": {}}}

    return data

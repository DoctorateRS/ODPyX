from flask import request

from ..const import USER_JSON_PATH
from .util import read_json, write_json


def charmSetSquad():
    charm_squad = request.get_json()["squad"]

    saved_data = read_json(USER_JSON_PATH)
    saved_data["user"]["charm"]["squad"] = charm_squad
    write_json(saved_data, USER_JSON_PATH)

    data = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {"charm": {"squad": charm_squad}},
        }
    }

    return data

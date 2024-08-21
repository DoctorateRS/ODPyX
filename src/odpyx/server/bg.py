from flask import request

from ..const import USER_JSON_PATH, CONFIG_PATH
from .util import read_json, write_json


def backgroundSetBackground():
    request_data = request.get_json()

    bgID = request_data["bgID"]
    data = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {"background": {"selected": bgID}},
        }
    }

    config = read_json(CONFIG_PATH)
    config["userConfig"]["background"] = bgID

    saved_data = read_json(USER_JSON_PATH)
    saved_data["user"]["background"]["selected"] = bgID
    write_json(saved_data, USER_JSON_PATH)
    write_json(config, CONFIG_PATH)

    return data


def homeThemeChange():
    request_data = request.get_json()

    themeId = request_data["themeId"]

    data = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {"homeTheme": {"selected": themeId}},
        }
    }

    config = read_json(CONFIG_PATH)
    config["userConfig"]["theme"] = themeId

    saved_data = read_json(USER_JSON_PATH)
    saved_data["user"]["homeTheme"]["selected"] = themeId
    write_json(saved_data, USER_JSON_PATH)
    write_json(config, CONFIG_PATH)

    return data

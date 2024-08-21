from flask import request

from .util import read_json, write_json
from ..const import USER_JSON_PATH


def bossrushBattleStart():
    data = {
        "apFailReturn": 0,
        "battleId": "abcdefgh-1234-5678-a1b2c3d4e5f6",
        "inApProtectPeriod": False,
        "isApProtect": 0,
        "notifyPowerScoreNotEnoughIfFailed": False,
        "playerDataDelta": {"modified": {}, "deleted": {}},
        "result": 0,
    }

    return data


def bossrushBattleFinish():
    data = {
        "result": 0,
        "apFailReturn": 0,
        "expScale": 1.2,
        "goldScale": 1.2,
        "rewards": [],
        "firstRewards": [],
        "unlockStages": [],
        "unusualRewards": [],
        "additionalRewards": [],
        "furnitureRewards": [],
        "alert": [],
        "suggestFriend": False,
        "pryResult": [],
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }
    return data


def bossRushRelicSelect():
    user_data = read_json(USER_JSON_PATH)
    request_data = request.get_json()
    activityId = request_data["activityId"]
    relicId = request_data["relicId"]

    user_data["user"]["activity"]["BOSS_RUSH"][activityId]["relic"]["select"] = relicId
    write_json(user_data, USER_JSON_PATH)

    data = {
        "playerDataDelta": {
            "modified": {"activity": {"BOSS_RUSH": {activityId: {"relic": {"select": relicId}}}}},
            "deleted": {},
        }
    }

    return data

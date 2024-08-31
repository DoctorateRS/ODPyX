import random
from flask import request

from ..const import GACHA_JSON_PATH, GACHA_TEMP_JSON_PATH
from .util import read_json, time


def pool_len(list):
    i = 0
    for _ in list:
        i += 1
    return i


def normalGacha():
    request_json = request.get_json()
    start_ts = int(time())
    return {
        "playerDataDelta": {
            "modified": {
                "recruit": {
                    "normal": {
                        "slots": {
                            str(request_json["slotId"]): {
                                "state": 2,
                                "selectTags": [
                                    {"tagId": i, "pick": 1}
                                    for i in request_json["tagList"]
                                ],
                                "startTs": start_ts,
                                "durationInSec": request_json["duration"],
                                "maxFinishTs": start_ts + request_json["duration"],
                                "realFinishTs": start_ts + request_json["duration"],
                            }
                        }
                    }
                }
            },
            "deleted": {},
        }
    }


def boostNormalGacha():
    request_json = request.get_json()
    real_finish_ts = int(time())
    return {
        "playerDataDelta": {
            "modified": {
                "recruit": {
                    "normal": {
                        "slots": {
                            str(request_json["slotId"]): {
                                "state": 3,
                                "realFinishTs": real_finish_ts,
                            }
                        }
                    }
                }
            },
            "deleted": {},
        }
    }


def finishNormalGacha():
    request_json = request.get_json()
    gacha = read_json(GACHA_JSON_PATH)
    char_id = gacha["normal"]["charId"]
    char_inst_id = int(char_id.split("_")[1])
    is_new = gacha["normal"]["isNew"]
    return {
        "result": 0,
        "charGet": {
            "charInstId": char_inst_id,
            "charId": char_id,
            "isNew": is_new,
            "itemGet": [
                {"type": "HGG_SHD", "id": "4004", "count": 999},
                {"type": "LGG_SHD", "id": "4005", "count": 999},
                {"type": "MATERIAL", "id": f"p_{char_id}", "count": 999},
            ],
            "logInfo": {},
        },
        "playerDataDelta": {
            "modified": {
                "recruit": {
                    "normal": {
                        "slots": {
                            str(request_json["slotId"]): {
                                "state": 1,
                                "selectTags": [],
                                "startTs": -1,
                                "durationInSec": -1,
                                "maxFinishTs": -1,
                                "realFinishTs": -1,
                            }
                        }
                    }
                }
            },
            "deleted": {},
        },
    }


def syncNormalGacha():
    return {"playerDataDelta": {"modified": {}, "deleted": {}}}


def advancedGacha():
    gacha = read_json(GACHA_JSON_PATH)

    pl_len = pool_len(gacha["advanced"])
    gacha_res = random.randint(0, pl_len - 1)

    char_id = gacha["advanced"][gacha_res]["charId"]
    char_inst_id = int(char_id.split("_")[1])
    is_new = gacha["advanced"][gacha_res]["isNew"]

    return {
        "result": 0,
        "charGet": {
            "charInstId": char_inst_id,
            "charId": char_id,
            "isNew": is_new,
            "itemGet": [
                {"type": "HGG_SHD", "id": "4004", "count": 999},
                {"type": "LGG_SHD", "id": "4005", "count": 999},
                {"type": "MATERIAL", "id": f"p_{char_id}", "count": 999},
            ],
            "logInfo": {},
        },
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }


def tenAdvancedGacha():
    gacha = read_json(GACHA_JSON_PATH)
    pl_len = pool_len(gacha["advanced"])
    chars = gacha["advanced"]
    gachaResultList = []
    for i in range(10):
        gacha_res = random.randint(0, pl_len - 1)
        char_id = chars[gacha_res]["charId"]
        char_inst_id = int(char_id.split("_")[1])
        is_new = chars[gacha_res]["isNew"]
        gachaResultList.append(
            {
                "charInstId": char_inst_id,
                "charId": char_id,
                "isNew": is_new,
                "itemGet": [
                    {"type": "HGG_SHD", "id": "4004", "count": 999},
                    {"type": "LGG_SHD", "id": "4005", "count": 999},
                    {"type": "MATERIAL", "id": f"p_{char_id}", "count": 999},
                ],
                "logInfo": {},
            }
        )
    return {
        "result": 0,
        "gachaResultList": gachaResultList,
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }


def getPoolDetail():
    pool = read_json(f"{GACHA_TEMP_JSON_PATH}pool.json")
    return pool

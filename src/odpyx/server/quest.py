from genericpath import exists
from flask import request
from base64 import b64decode, b64encode
import io
import zipfile

from ..const import (
    BATTLE_REPLAY_JSON_PATH,
    USER_JSON_PATH,
    CONFIG_PATH,
    ASSIST_PATH,
    SQUADS_PATH,
)
from .util import read_json, write_json, decrypt_battle_data, JsonUtils, time


def decode_battle_replay(encoded_battle_replay):
    count = 1
    encrypted_path = "dump/encrypted/DATA_1.txt"
    while exists(encrypted_path):
        count += 1
        encrypted_path = f"dump/encrypted/DATA_{count}.txt"
    with open(encrypted_path, "w") as f:
        f.write(encoded_battle_replay)

    bytes_io = io.BytesIO(b64decode(encoded_battle_replay))

    with zipfile.ZipFile(bytes_io) as zip_file:
        decoded_battle_replay = JsonUtils.load(zip_file.read("default_entry"))
    return decoded_battle_replay


def encode_battle_replay(decoded_battle_replay):
    count = 1
    decrypted_path = "dump/decrypted/DATA_1.json"
    while exists(decrypted_path):
        count += 1
        decrypted_path = f"dump/decrypted/DATA_{count}.json"

    with open(decrypted_path, "w") as f:
        f.write(JsonUtils.dumps(decoded_battle_replay))
    bytes_io = io.BytesIO()
    with zipfile.ZipFile(bytes_io, "w") as zip_file:
        zip_file.writestr("default_entry", JsonUtils.dumps(decoded_battle_replay))
    encoded_battle_replay = b64encode(bytes_io.getvalue()).decode("utf-8")
    return encoded_battle_replay


def questBattleStart():
    request_data = request.get_json()
    data = {
        "apFailReturn": 0,
        "battleId": "abcdefgh-1234-5678-a1b2c3d4e5f6",
        "inApProtectPeriod": False,
        "isApProtect": 0,
        "notifyPowerScoreNotEnoughIfFailed": False,
        "playerDataDelta": {"modified": {}, "deleted": {}},
        "result": 0,
    }

    replay_data = read_json(BATTLE_REPLAY_JSON_PATH)
    replay_data["current"] = request_data["stageId"]
    write_json(replay_data, BATTLE_REPLAY_JSON_PATH)

    return data


def questBattleFinish():
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
        "overrideRewards": [],
        "alert": [],
        "suggestFriend": False,
        "pryResult": [],
        "itemReturn": [],
        "wave": 0,
        "milestoneBefore": 0,
        "milestoneAdd": 0,
        "isMileStoneMax": False,
        "tokenAdd": 0,
        "isTokenMax": False,
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }

    return data


def questSaveBattleReplay():
    request_data = request.get_json()

    replay_data = read_json(BATTLE_REPLAY_JSON_PATH)

    data = {
        "result": 0,
        "playerDataDelta": {
            "modified": {
                "dungeon": {"stages": {replay_data["current"]: {"hasBattleReplay": 1}}}
            },
            "deleted": {},
        },
    }

    char_config = replay_data["currentCharConfig"]

    encoded_battle_replay = request_data["battleReplay"]
    decoded_battle_replay = decode_battle_replay(encoded_battle_replay)

    if read_json(CONFIG_PATH)["battleReplayConfig"]["anonymous"]:
        decoded_battle_replay["campaignOnlyVersion"] = 0
        decoded_battle_replay["timestamp"] = "1700000000"
        decoded_battle_replay["journal"]["metadata"]["saveTime"] = (
            "2023-11-15T06:13:20Z"
        )

    if char_config in list(replay_data["saved"].keys()):
        replay_data["saved"][char_config].update(
            {replay_data["current"]: decoded_battle_replay}
        )
    else:
        replay_data["saved"].update(
            {char_config: {replay_data["current"]: decoded_battle_replay}}
        )
    replay_data["current"] = None
    write_json(replay_data, BATTLE_REPLAY_JSON_PATH)

    return data


def questGetBattleReplay():
    stageId = request.get_json()["stageId"]

    replay_data = read_json(BATTLE_REPLAY_JSON_PATH)

    decoded_battle_replay = replay_data["saved"][replay_data["currentCharConfig"]][
        stageId
    ]
    encoded_battle_replay = encode_battle_replay(decoded_battle_replay)

    battleData = {
        "battleReplay": encoded_battle_replay,
        "playerDataDelta": {"deleted": {}, "modified": {}},
    }

    return battleData


def questChangeSquadName():
    request_data = request.get_json()
    data = {"playerDataDelta": {"modified": {"troop": {"squads": {}}}, "deleted": {}}}

    if request_data["squadId"] and request_data["name"]:
        data["playerDataDelta"]["modified"]["troop"]["squads"].update(
            {str(request_data["squadId"]): {"name": request_data["name"]}}
        )

        squad_data = read_json(SQUADS_PATH)
        saved_data = read_json(USER_JSON_PATH)
        saved_data["user"]["troop"]["squads"][str(request_data["squadId"])]["name"] = (
            request_data["name"]
        )
        squad_data[str(request_data["squadId"])]["name"] = request_data["name"]
        write_json(saved_data, USER_JSON_PATH)
        write_json(squad_data, SQUADS_PATH)

    return data


def questSquadFormation():
    request_data = request.get_json()
    data = {"playerDataDelta": {"modified": {"troop": {"squads": {}}}, "deleted": {}}}

    if request_data["squadId"] and request_data["slots"]:
        data["playerDataDelta"]["modified"]["troop"]["squads"].update(
            {str(request_data["squadId"]): {"slots": request_data["slots"]}}
        )

        saved_data = read_json(USER_JSON_PATH)
        saved_data["user"]["troop"]["squads"][str(request_data["squadId"])]["slots"] = (
            request_data["slots"]
        )
        write_json(saved_data, USER_JSON_PATH)

    return data


def questGetAssistList():
    assist_unit_configs = read_json(ASSIST_PATH)
    saved_data = read_json(USER_JSON_PATH)["user"]["troop"]["chars"]
    assist_units = []
    for assist_unit_config in assist_unit_configs:
        assist_unit = {}

        flag = False
        for _, char in saved_data.items():
            if char["charId"] == assist_unit_config["charId"]:
                assist_unit.update(
                    {
                        "charId": char["charId"],
                        "skinId": char["skin"],
                        "skills": char["skills"],
                        "mainSkillLvl": char["mainSkillLvl"],
                        "skillIndex": assist_unit_config["skillIndex"],
                        "evolvePhase": char["evolvePhase"],
                        "favorPoint": char["favorPoint"],
                        "potentialRank": char["potentialRank"],
                        "level": char["level"],
                        "crisisRecord": {},
                        "currentEquip": assist_unit_config["currentEquip"]
                        if assist_unit_config["currentEquip"] in char["equip"]
                        else None,
                        "equip": char["equip"],
                    }
                )
                flag = True
                break
        if flag:
            assist_units.append(assist_unit)

    data = {
        "allowAskTs": int(time()),
        "assistList": [
            {
                "uid": "88888888",
                "aliasName": "",
                "nickName": "ABCDEF",
                "nickNumber": "8888",
                "level": 200,
                "avatarId": "0",
                "avatar": {"type": "ASSISTANT", "id": "char_421_crow#1"},
                "lastOnlineTime": int(time()),
                "assistCharList": [assist_unit],
                "powerScore": 500,
                "isFriend": True,
                "canRequestFriend": False,
                "assistSlotIndex": 0,
            }
            for assist_unit in assist_units
        ],
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }

    return data


def markStoryAcceKnown():
    return {
        "playerDataDelta": {
            "modified": {"storyreview": {"tags": {"knownStoryAcceleration": 1}}},
            "deleted": {},
        }
    }


def readStory():
    return {"readCount": 1, "playerDataDelta": {"modified": {}, "deleted": {}}}


def confirmBattleCar():
    return {
        "playerDataDelta": {
            "modified": {"car": {"battleCar": request.get_json()["car"]}},
            "deleted": {},
        }
    }


def typeAct20side_competitionStart():
    return {
        "result": 0,
        "battleId": "abcdefgh-1234-5678-a1b2c3d4e5f6",
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }


def typeAct20side_competitionFinish():
    return {
        "performance": 0,
        "expression": 0,
        "operation": 0,
        "total": 0,
        "level": "B",
        "isNew": False,
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }


def questBattleContinue():
    return {
        "result": 0,
        "battleId": "abcdefgh-1234-5678-a1b2c3d4e5f6",
        "apFailReturn": 0,
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }


def setTool():
    request_data = request.get_json()
    tool = {"tool_trap": 1, "tool_wirebug": 1, "tool_flashbomb": 1, "tool_bomb": 1}
    for i in request_data["tools"]:
        tool[i] = 2
    data = {
        "playerDataDelta": {
            "modified": {"activity": {"TYPE_ACT24SIDE": {"act24side": {"tool": tool}}}},
            "deleted": {},
        }
    }
    return data


def relicSelect():
    request_data = request.get_json()
    activityId = request_data["activityId"]
    relicId = request_data["relicId"]
    data = {
        "playerDataDelta": {
            "modified": {
                "activity": {"BOSS_RUSH": {activityId: {"relic": {"select": relicId}}}}
            },
            "deleted": {},
        }
    }
    return data


def setTrapSquad():
    request_data = request.get_json()
    trapDomainId = request_data["trapDomainId"]
    trapSquad = request_data["trapSquad"]
    data = {
        "playerDataDelta": {
            "modified": {
                "templateTrap": {"domains": {trapDomainId: {"squad": trapSquad}}}
            },
            "deleted": {},
        }
    }
    return data


def act5fun_questBattleFinish():
    battle_data = decrypt_battle_data(request.get_json()["data"])
    score = 0
    for i in battle_data["battleData"]["stats"]["extraBattleInfo"]:
        if i.startswith("SIMPLE,money,"):
            score = int(i.split(",")[-1])
    return {
        "result": 0,
        "score": score,
        "isHighScore": False,
        "npcResult": {},
        "playerResult": {"totalWin": 0, "streak": 0, "totalRound": 10},
        "reward": [],
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }


def act4fun_questBattleFinish():
    return {
        "materials": [
            {"instId": i, "materialId": j, "materialType": 1}
            for i, j in enumerate(
                [
                    "spLiveMat_tr_1",
                    "spLiveMat_tr_2",
                    "spLiveMat_01_1",
                    "spLiveMat_01_2",
                    "spLiveMat_01_3",
                    "spLiveMat_01_4",
                    "spLiveMat_01_5",
                    "spLiveMat_01_6",
                    "spLiveMat_01_7",
                    "spLiveMat_01_8",
                    "spLiveMat_01_9",
                    "spLiveMat_02_1",
                    "spLiveMat_02_2",
                    "spLiveMat_02_3",
                    "spLiveMat_02_4",
                    "spLiveMat_02_5",
                    "spLiveMat_02_6",
                    "spLiveMat_02_7",
                    "spLiveMat_02_8",
                    "spLiveMat_02_9",
                    "spLiveMat_03_1",
                    "spLiveMat_03_2",
                    "spLiveMat_03_3",
                    "spLiveMat_03_4",
                    "spLiveMat_03_5",
                    "spLiveMat_03_6",
                    "spLiveMat_03_7",
                    "spLiveMat_03_8",
                    "spLiveMat_03_9",
                ]
            )
        ],
        "liveId": "abcdefgh-1234-5678-a1b2c3d4e5f6",
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }


def act4fun_liveSettle():
    return {
        "ending": "goodending_1",
        "playerDataDelta": {"modified": {}, "deleted": {}},
    }

from flask import request

from ..const import USER_JSON_PATH
from .util import read_json, write_json, time


def charBuildBatchSetCharVoiceLan():
    data = {"result": {}, "playerDataDelta": {"modified": {}, "deleted": {}}}
    return data


def charBuildaddonStoryUnlock():
    request_data = request.get_json()

    ts = {"fts": int(time()), "rts": int(time())}

    data = {"playerDataDelta": {"deleted": {}, "modified": {"troop": {"addon": {}}}}}

    storyId = {"story": {request_data["storyId"]: ts}}
    charId = {request_data["charId"]: storyId}

    saved_data = read_json(USER_JSON_PATH)
    saved_data["user"]["troop"]["addon"].update(charId)

    data["playerDataDelta"]["modified"]["troop"]["addon"].update(charId)

    write_json(saved_data, USER_JSON_PATH)

    return data


def charBuildSetCharVoiceLan():
    request_data = request.get_json()

    data = {"playerDataDelta": {"deleted": {}, "modified": {"troop": {"chars": {}}}}}

    saved_data = read_json(USER_JSON_PATH)
    for character in request_data["charList"]:
        saved_data["user"]["troop"]["chars"][str(character)]["voiceLan"] = request_data["voiceLan"]
        data["playerDataDelta"]["modified"]["troop"]["chars"].update({str(character): {"voiceLan": request_data["voiceLan"]}})

    write_json(saved_data, USER_JSON_PATH)

    return data


def charBuildSetDefaultSkill():
    request_data = request.get_json()
    charInstId = request_data["charInstId"]
    defaultSkillIndex = request_data["defaultSkillIndex"]
    data = {"playerDataDelta": {"modified": {"troop": {"chars": {}}}, "deleted": {}}}

    saved_data = read_json(USER_JSON_PATH)

    data["playerDataDelta"]["modified"]["troop"]["chars"].update({str(charInstId): {"defaultSkillIndex": defaultSkillIndex}})

    saved_data["user"]["troop"]["chars"][str(charInstId)]["defaultSkillIndex"] = defaultSkillIndex
    write_json(saved_data, USER_JSON_PATH)

    return data


def charBuildChangeCharSkin():
    request_data = request.get_json()
    charInstId = request_data["charInstId"]
    skinId = request_data["skinId"]
    data = {"playerDataDelta": {"modified": {"troop": {"chars": {}}}, "deleted": {}}}

    saved_data = read_json(USER_JSON_PATH)
    data["playerDataDelta"]["modified"]["troop"]["chars"].update({str(charInstId): {"skin": skinId}})

    saved_data["user"]["troop"]["chars"][str(charInstId)]["skin"] = skinId
    write_json(saved_data, USER_JSON_PATH)

    return data


def charBuildSetEquipment():
    request_data = request.get_json()
    charInstId = request_data["charInstId"]
    equipId = request_data["equipId"]
    data = {"playerDataDelta": {"modified": {"troop": {"chars": {}}}, "deleted": {}}}

    saved_data = read_json(USER_JSON_PATH)
    data["playerDataDelta"]["modified"].update({"troop": {"chars": {str(charInstId): {"currentEquip": equipId}}}})

    saved_data["user"]["troop"]["chars"][str(charInstId)]["currentEquip"] = equipId
    write_json(saved_data, USER_JSON_PATH)

    return data


def charBuildChangeCharTemplate():
    request_data = request.get_json()

    data = {
        "playerDataDelta": {
            "modified": {"troop": {"chars": {str(request_data["charInstId"]): {"currentTmpl": request_data["templateId"]}}}},
            "deleted": {},
        }
    }

    saved_data = read_json(USER_JSON_PATH)
    saved_data["user"]["troop"]["chars"][str(request_data["charInstId"])]["currentTmpl"] = request_data["templateId"]
    write_json(saved_data, USER_JSON_PATH)

    return data

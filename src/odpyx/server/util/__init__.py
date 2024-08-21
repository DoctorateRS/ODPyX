
from typing import Any
from .json import JsonUtils, read_json, write_json
from .crypto import decrypt_battle_data

from os import path as ospath, makedirs
from requests import get

def update_data(url: str) -> Any:
    BASE_URL_LIST = [
        (
            "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata",
            "./data",
        ),
        (
            "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/en_US/gamedata",
            "./data-global",
        ),
        (
            "https://ak-conf.hypergryph.com/config/prod/announce_meta/Android",
            "./data/announce",
        ),
        (
            "https://ark-us-static-online.yo-star.com/announce/Android",
            "./data/announce",
        ),
    ]

    localPath = ""

    for index in BASE_URL_LIST:
        if index[0] in url:
            if not ospath.isdir(index[1]):
                makedirs(index[1])
            localPath = url.replace(index[0], index[1])
            break

    if "Android/version" in url:
        reponse = get(url)
        data = JsonUtils.load(reponse.content)
    else:
        data = read_json(localPath, encoding="utf-8")

    return data

import re
from flask import request
from random import shuffle

from ..const import CONFIG_PATH
from .util import read_json, write_json, update_data, JsonUtils


def randomHash():
    hash = list("abcdef")
    shuffle(hash)

    return "".join(hash)


def prodRefreshConfig():
    data = {"resVersion": None}

    return data, 200


def prodAndroidVersion():
    server_config = read_json(CONFIG_PATH)
    mode = server_config["server"]["mode"]
    match mode:
        case "cn":
            version = server_config["version"]["android"]
        case "global":
            version = server_config["versionGlobal"]["android"]
        case _:
            version = server_config["version"]["android"]

    if server_config["assets"]["enableMods"]:
        version["resVersion"] = version["resVersion"][:18] + randomHash()

    return version


def prodNetworkConfig():
    server_config = read_json(CONFIG_PATH)

    mode = server_config["server"]["mode"]
    server = (
        "http://"
        + server_config["server"]["host"]
        + ":"
        + str(server_config["server"]["port"])
    )
    if server_config["server"]["adaptive"]:
        server = request.host_url[:-1]
    network_config = server_config["networkConfig"][mode]
    funcVer = network_config["content"]["funcVer"]

    if server_config["assets"]["autoUpdate"]:
        match mode:
            case "cn":
                version = update_data(
                    "https://ak-conf.hypergryph.com/config/prod/official/Android/version"
                )
                server_config["version"]["android"] = version
            case "global":
                version = update_data(
                    "https://ark-us-static-online.yo-star.com/assetbundle/official/Android/version"
                )
                server_config["versionGlobal"]["android"] = version
            case _:
                version = update_data(
                    "https://ak-conf.hypergryph.com/config/prod/official/Android/version"
                )
                server_config["version"]["android"] = version

        write_json(server_config, CONFIG_PATH)

    for index in network_config["content"]["configs"][funcVer]["network"]:
        url = network_config["content"]["configs"][funcVer]["network"][index]
        if isinstance(url, str) and url.find("{server}") >= 0:
            network_config["content"]["configs"][funcVer]["network"][index] = re.sub(
                "{server}", server, url
            )

    network_config["content"] = JsonUtils.dumps(network_config["content"])

    return network_config


def prodRemoteConfig():
    remote = read_json(CONFIG_PATH)["remote"]

    return remote


def prodPreAnnouncement():
    server_config = read_json(CONFIG_PATH)
    mode = server_config["server"]["mode"]
    match mode:
        case "cn":
            data = update_data(
                "https://ak-conf.hypergryph.com/config/prod/announce_meta/Android/preannouncement.meta.json"
            )
        case "global":
            data = update_data(
                "https://ark-us-static-online.yo-star.com/announce/Android/preannouncement.meta.json"
            )
        case _:
            data = update_data(
                "https://ak-conf.hypergryph.com/config/prod/announce_meta/Android/preannouncement.meta.json"
            )

    return data


def prodAnnouncement():
    server_config = read_json(CONFIG_PATH)
    mode = server_config["server"]["mode"]
    match mode:
        case "cn":
            data = update_data(
                "https://ak-conf.hypergryph.com/config/prod/announce_meta/Android/announcement.meta.json"
            )
        case "global":
            data = update_data(
                "https://ark-us-static-online.yo-star.com/announce/Android/announcement.meta.json"
            )
        case _:
            data = update_data(
                "https://ak-conf.hypergryph.com/config/prod/announce_meta/Android/announcement.meta.json"
            )

    return data

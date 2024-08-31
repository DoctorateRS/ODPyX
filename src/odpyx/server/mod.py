import zlib
import os
import socket
import zipfile
import hashlib
from datetime import datetime

from .util import JsonUtils


def writeLog(data):
    time = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    clientIp = socket.gethostbyname(socket.gethostname())
    print(f"{clientIp} - - [{time}] {data}")


def loadMods(log: bool = True, no_validate_mod_cache=False):
    fileList = []
    loadedModList = {"mods": [], "name": [], "path": [], "download": []}

    for file in os.listdir("./mods/"):
        if file != ".placeholder" and file.endswith(".dat"):
            fileList.append("./mods/" + file)

    dat_file_infos = {}

    for filePath in fileList:
        with open(filePath, "rb") as f:
            file_content = f.read()
            file_size = len(file_content)
            file_crc32 = zlib.crc32(file_content)
            dat_file_infos[filePath] = {"size": file_size, "crc32": file_crc32}

    mod_cache = None

    if os.path.isfile("mods.json"):
        with open("mods.json", encoding="utf-8") as f:
            mod_cache = JsonUtils.load(f)

    if mod_cache is not None and no_validate_mod_cache:
        writeLog("\033[1;32mUsing Not Validated Cached Mod...\033[0;0m")
        return mod_cache["mod"]
    else:
        mod_cache = {}

    mod_cache_valid = False

    if mod_cache is not None:
        cached_dat_file_infos = mod_cache["file"]
        if dat_file_infos == cached_dat_file_infos:
            mod_cache_valid = True

    if mod_cache_valid:
        writeLog("\033[1;32mUsing Cached Mod...\033[0;0m")
        return mod_cache["mod"]

    for filePath in fileList:
        if not zipfile.is_zipfile(filePath) or os.path.getsize(filePath) == 0:
            continue
        modFile = zipfile.ZipFile(filePath, "r")

        try:
            for fileName, info in zip(modFile.namelist(), modFile.infolist()):
                if not zipfile.ZipInfo.is_dir(info):
                    modName = fileName
                    if modName in loadedModList["name"]:
                        writeLog(filePath + " - \033[1;33mConflict with other mods...\033[0;0m")
                        continue

                    byteBuffer = modFile.read(fileName)
                    totalSize = os.path.getsize(filePath)
                    abSize = len(byteBuffer)
                    modMd5 = hashlib.md5(byteBuffer).hexdigest()

                    abInfo = {
                        "name": modName,
                        "hash": modMd5,
                        "md5": modMd5,
                        "totalSize": totalSize,
                        "abSize": abSize,
                    }

                    if log:
                        writeLog(filePath + " - \033[1;32mMod loaded successfully...\033[0;0m")

                    loadedModList["mods"].append(abInfo)
                    loadedModList["name"].append(modName)
                    loadedModList["path"].append(filePath)
                    downloadName = os.path.splitext(modName.replace("/", "_").replace("#", "__"))[0] + ".dat"
                    loadedModList["download"].append(downloadName)

        except Exception as e:
            writeLog(filePath + " - \033[1;31mMod file loading failed...\033[0;0m")
        modFile.close()

    with open("mods.json", "w", encoding="utf-8") as f:
        f.write(JsonUtils.dumps({"mod": loadedModList, "file": dat_file_infos}))

    return loadedModList

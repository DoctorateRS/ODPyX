from typing import Any
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import md5

from .json import JsonUtils

KEY = "pM6Umv*^hVQuB6t&"

def decrypt_battle_data(data: str, login: int = 1672502400) -> Any:
    battle_data = bytes.fromhex(data[: len(data) - 32])
    src = KEY + str(login)
    x = 1
    key = md5(src.encode()).digest()
    iv = bytes.fromhex(data[len(data) - 32 :])

    aes = AES.new(key, AES.MODE_CBC, iv)

    try:
        decrypted_data = unpad(aes.decrypt(battle_data), AES.block_size)
        data = JsonUtils.load(decrypted_data)
        return data

    except Exception as e:
        return {}

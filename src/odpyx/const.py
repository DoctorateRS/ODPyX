from .server.util import read_json

# Config Data
CONFIG_PATH = "config/config.json"
MAILLIST_PATH = "config/mails.json"
RLV2_CONFIG_PATH = "config/rlv2Config.json"
SQUADS_PATH = "config/squads.json"
SYNC_DATA_TEMPLATE_PATH = "syncData.json"
ASSIST_PATH = "config/assist.json"

# User Data
USER_JSON_PATH = "data/user/user.json"
BATTLE_REPLAY_JSON_PATH = "data/user/battleReplays.json"
RLV2_JSON_PATH = "data/user/rlv2.json"
RLV2_STATIC_JSON_PATH = "data/user/rlv2Static.json"
RLV2_SETTINGS_PATH = "data/user/rlv2Settings.json"
RLV2_USER_SETTINGS_PATH = "data/user/rlv2UserSettings.json"
RLV2_TEMPBUFF_JSON_PATH = "data/user/rlv2TempBuffs.json"
CRISIS_JSON_BASE_PATH = "data/crisis/"
CRISIS_V2_JSON_BASE_PATH = "data/crisisV2/"
RUNE_JSON_PATH = "data/user/rune.json"
BUILDING_JSON_PATH = "data/user/building.json"

# RLV2 Options
RLV2_CHOICEBUFFS = "data/rlv2/choiceBuffs.json"
RLV2_RECRUITGROUPS = "data/rlv2/recruitGroups.json"
RLV2_NODESINFO = "data/rlv2/nodesInfo.json"

# TOWER Data
TOWERDATA_PATH = "data/tower/towerData.json"

SANDBOX_JSON_PATH = "data/user/sandbox.json"
SANDBOX_TEMP_JSON_PATH = "data/user/sandboxTemp.json"

POOL_JSON_PATH = "data/user/pool.json"
POOL_CLASSIC_JSON_PATH = "data/user/poolClassic.json"
GACHA_JSON_PATH = "data/user/gacha.json"
GACHA_TEMP_JSON_PATH = "data/user/gachaTemp.json"

GACHA_UP_CHAR_JSON_PATH = "data/user/gachaUpChar.json"

POOL_JSON_DIR = "data/gacha/"

config = read_json(CONFIG_PATH)
mode = config["server"]["mode"]

if mode == "cn":
    BASE_URL = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata"
else:
    BASE_URL = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/main/en_US/gamedata/excel/"

# TABLE Urls
ACTIVITY_TABLE_URL = BASE_URL + "/excel/activity_table.json"
CHARM_TABLE_URL = BASE_URL + "/excel/charm_table.json"
SKIN_TABLE_URL = BASE_URL + "/excel/skin_table.json"
CHARACTER_TABLE_URL = BASE_URL + "/excel/character_table.json"
BATTLEEQUIP_TABLE_URL = BASE_URL + "/excel/battle_equip_table.json"
EQUIP_TABLE_URL = BASE_URL + "/excel/uniequip_table.json"
STORY_TABLE_URL = BASE_URL + "/excel/story_table.json"
STAGE_TABLE_URL = BASE_URL + "/excel/stage_table.json"
RL_TABLE_URL = BASE_URL + "/excel/roguelike_topic_table.json"
DM_TABLE_URL = BASE_URL + "/excel/display_meta_table.json"
RETRO_TABLE_URL = BASE_URL + "/excel/retro_table.json"
HANDBOOK_INFO_TABLE_URL = BASE_URL + "/excel/handbook_info_table.json"
TOWER_TABLE_URL = BASE_URL + "/excel/climb_tower_table.json"
BUILDING_TABLE_URL = BASE_URL + "/excel/building_data.json"
STORY_REVIEW_TABLE_URL = BASE_URL + "/excel/story_review_table.json"
ENEMY_HANDBOOK_TABLE_URL = BASE_URL + "/excel/enemy_handbook_table.json"
MEDAL_TABLE_URL = BASE_URL + "/excel/medal_table.json"
SANDBOX_TABLE_URL = BASE_URL + "/excel/sandbox_perm_table.json"
CHARWORD_TABLE_URL = BASE_URL + "/excel/charword_table.json"
STORY_REVIEW_META_TABLE_URL = BASE_URL + "/excel/story_review_meta_table.json"

from typing import Any
from flask import Flask
from logging import getLogger, INFO

from .server import (
    account,
    bg,
    building,
    campaignv2,
    char,
    charbuild,
    charm,
    crisis,
    deepsea,
    mail,
    online,
    tower,
    quest,
    pay,
    rlv2,
    shop,
    story,
    user,
    assets,
    prod,
    sandbox,
    gacha,
)

from .server.util.json import read_json
from .const import CONFIG_PATH

app = Flask(__name__)
logger = getLogger("werkzeug").setLevel(INFO)

app.add_url_rule("/app/getSettings", methods=["POST"], view_func=user.appGetSettings)
app.add_url_rule("/app/getCode", methods=["POST"], view_func=user.appGetCode)

app.add_url_rule("/aprilFool/act5fun/battleStart", methods=["POST"], view_func=quest.questBattleStart)
app.add_url_rule(
    "/aprilFool/act5fun/battleFinish",
    methods=["POST"],
    view_func=quest.act5fun_questBattleFinish,
)

app.add_url_rule("/aprilFool/act4fun/battleStart", methods=["POST"], view_func=quest.questBattleStart)
app.add_url_rule(
    "/aprilFool/act4fun/battleFinish",
    methods=["POST"],
    view_func=quest.act4fun_questBattleFinish,
)
app.add_url_rule(
    "/aprilFool/act4fun/liveSettle",
    methods=["POST"],
    view_func=quest.act4fun_liveSettle,
)

app.add_url_rule("/aprilFool/act3fun/battleStart", methods=["POST"], view_func=quest.questBattleStart)
app.add_url_rule(
    "/aprilFool/act3fun/battleFinish",
    methods=["POST"],
    view_func=quest.questBattleFinish,
)

app.add_url_rule("/account/login", methods=["POST"], view_func=account.accountLogin)
app.add_url_rule("/account/syncData", methods=["POST"], view_func=account.accountSyncData)
app.add_url_rule("/account/syncStatus", methods=["POST"], view_func=account.accountSyncStatus)
app.add_url_rule(
    "/account/yostar_auth_request",
    methods=["POST"],
    view_func=account.accountYostarAuthRequest,
)
app.add_url_rule(
    "/account/yostar_auth_submit",
    methods=["POST"],
    view_func=account.accountYostarAuthSubmit,
)

app.add_url_rule(
    "/assetbundle/official/Android/assets/<string:assetsHash>/<string:fileName>",
    methods=["GET"],
    view_func=assets.getFile,
)

app.add_url_rule(
    "/background/setBackground",
    methods=["POST"],
    view_func=bg.backgroundSetBackground,
)
app.add_url_rule("/homeTheme/change", methods=["POST"], view_func=bg.homeThemeChange)

app.add_url_rule("/building/sync", methods=["POST"], view_func=building.buildingSync)

app.add_url_rule(
    "/building/getRecentVisitors",
    methods=["POST"],
    view_func=building.building_getRecentVisitors,
)
app.add_url_rule(
    "/building/getInfoShareVisitorsNum",
    methods=["POST"],
    view_func=building.building_getInfoShareVisitorsNum,
)
app.add_url_rule(
    "/building/changeDiySolution",
    methods=["POST"],
    view_func=building.building_changeDiySolution,
)
app.add_url_rule("/building/assignChar", methods=["POST"], view_func=building.building_assignChar)
app.add_url_rule(
    "/building/setBuildingAssist",
    methods=["POST"],
    view_func=building.building_setBuildingAssist,
)
app.add_url_rule(
    "/building/getAssistReport",
    methods=["POST"],
    view_func=building.building_getAssistReport,
)

app.add_url_rule(
    "/campaignV2/battleStart",
    methods=["POST"],
    view_func=campaignv2.campaignV2BattleStart,
)
app.add_url_rule(
    "/campaignV2/battleFinish",
    methods=["POST"],
    view_func=campaignv2.campaignV2BattleFinish,
)
app.add_url_rule(
    "/campaignV2/battleSweep",
    methods=["POST"],
    view_func=campaignv2.campaignV2BattleSweep,
)

app.add_url_rule("/char/changeMarkStar", methods=["POST"], view_func=char.charChangeMarkStar)

app.add_url_rule(
    "/charBuild/addonStage/battleStart",
    methods=["POST"],
    view_func=quest.questBattleStart,
)
app.add_url_rule(
    "/charBuild/addonStage/battleFinish",
    methods=["POST"],
    view_func=quest.questBattleFinish,
)
app.add_url_rule(
    "/charBuild/addonStory/unlock",
    methods=["POST"],
    view_func=charbuild.charBuildaddonStoryUnlock,
)
app.add_url_rule(
    "/charBuild/batchSetCharVoiceLan",
    methods=["POST"],
    view_func=charbuild.charBuildBatchSetCharVoiceLan,
)
app.add_url_rule(
    "/charBuild/setCharVoiceLan",
    methods=["POST"],
    view_func=charbuild.charBuildSetCharVoiceLan,
)
app.add_url_rule(
    "/charBuild/setDefaultSkill",
    methods=["POST"],
    view_func=charbuild.charBuildSetDefaultSkill,
)
app.add_url_rule(
    "/charBuild/changeCharSkin",
    methods=["POST"],
    view_func=charbuild.charBuildChangeCharSkin,
)
app.add_url_rule(
    "/charBuild/setEquipment",
    methods=["POST"],
    view_func=charbuild.charBuildSetEquipment,
)
app.add_url_rule(
    "/charBuild/changeCharTemplate",
    methods=["POST"],
    view_func=charbuild.charBuildChangeCharTemplate,
)

app.add_url_rule("/charm/setSquad", methods=["POST"], view_func=charm.charmSetSquad)

app.add_url_rule(
    "/config/prod/announce_meta/Android/preannouncement.meta.json",
    methods=["GET"],
    view_func=prod.prodPreAnnouncement,
)
app.add_url_rule(
    "/config/prod/announce_meta/Android/announcement.meta.json",
    methods=["GET"],
    view_func=prod.prodAnnouncement,
)
app.add_url_rule(
    "/config/prod/official/Android/version",
    methods=["GET"],
    view_func=prod.prodAndroidVersion,
)
app.add_url_rule(
    "/config/prod/official/network_config",
    methods=["GET"],
    view_func=prod.prodNetworkConfig,
)
app.add_url_rule(
    "/config/prod/official/refresh_config",
    methods=["GET"],
    view_func=prod.prodRefreshConfig,
)
app.add_url_rule(
    "/config/prod/official/remote_config",
    methods=["GET"],
    view_func=prod.prodRemoteConfig,
)
app.add_url_rule("/crisis/getInfo", methods=["POST"], view_func=crisis.crisisGetCrisisInfo)
app.add_url_rule("/crisis/battleStart", methods=["POST"], view_func=crisis.crisisBattleStart)
app.add_url_rule("/crisis/battleFinish", methods=["POST"], view_func=crisis.crisisBattleFinish)
app.add_url_rule("/crisisV2/getInfo", methods=["POST"], view_func=crisis.crisisV2_getInfo)
app.add_url_rule("/crisisV2/battleStart", methods=["POST"], view_func=crisis.crisisV2_battleStart)
app.add_url_rule("/crisisV2/battleFinish", methods=["POST"], view_func=crisis.crisisV2_battleFinish)
app.add_url_rule("/crisisV2/getSnapshot", methods=["POST"], view_func=crisis.crisisV2_getSnapshot)

app.add_url_rule("/deepSea/branch", methods=["POST"], view_func=deepsea.deepSeaBranch)
app.add_url_rule("/deepSea/event", methods=["POST"], view_func=deepsea.deepSeaEvent)

app.add_url_rule("/mail/getMetaInfoList", methods=["POST"], view_func=mail.mailGetMetaInfoList)
app.add_url_rule("/mail/listMailBox", methods=["POST"], view_func=mail.mailListMailBox)
app.add_url_rule("/mail/receiveMail", methods=["POST"], view_func=mail.mailReceiveMail)
app.add_url_rule("/mail/receiveAllMail", methods=["POST"], view_func=mail.mailReceiveAllMail)
app.add_url_rule(
    "/mail/removeAllReceivedMail",
    methods=["POST"],
    view_func=mail.mailRemoveAllReceivedMail,
)

app.add_url_rule("/online/v1/ping", methods=["POST"], view_func=online.onlineV1Ping)
app.add_url_rule("/online/v1/loginout", methods=["POST"], view_func=online.onlineV1LoginOut)

app.add_url_rule("/tower/createGame", methods=["POST"], view_func=tower.towerCreateGame)
app.add_url_rule("/tower/initGodCard", methods=["POST"], view_func=tower.towerInitGodCard)
app.add_url_rule("/tower/initGame", methods=["POST"], view_func=tower.towerInitGame)
app.add_url_rule("/tower/initCard", methods=["POST"], view_func=tower.towerInitCard)
app.add_url_rule("/tower/battleStart", methods=["POST"], view_func=tower.towerBattleStart)
app.add_url_rule("/tower/battleFinish", methods=["POST"], view_func=tower.towerBattleFinish)
app.add_url_rule("/tower/recruit", methods=["POST"], view_func=tower.towerRecruit)
app.add_url_rule("/tower/chooseSubGodCard", methods=["POST"], view_func=tower.towerChooseSubGodCard)
app.add_url_rule("/tower/settleGame", methods=["POST"], view_func=tower.towerSettleGame)

app.add_url_rule(
    "/pay/getUnconfirmedOrderIdList",
    methods=["POST"],
    view_func=pay.payGetUnconfirmedOrderIdList,
)
app.add_url_rule("/u8/pay/getAllProductList", methods=["POST"], view_func=pay.paygetAllProductList)

app.add_url_rule("/quest/battleStart", methods=["POST"], view_func=quest.questBattleStart)
app.add_url_rule("/quest/battleFinish", methods=["POST"], view_func=quest.questBattleFinish)
app.add_url_rule("/quest/saveBattleReplay", methods=["POST"], view_func=quest.questSaveBattleReplay)
app.add_url_rule("/quest/getBattleReplay", methods=["POST"], view_func=quest.questGetBattleReplay)
app.add_url_rule("/quest/changeSquadName", methods=["POST"], view_func=quest.questChangeSquadName)
app.add_url_rule("/quest/squadFormation", methods=["POST"], view_func=quest.questSquadFormation)
app.add_url_rule("/quest/getAssistList", methods=["POST"], view_func=quest.questGetAssistList)

app.add_url_rule("/quest/battleContinue", methods=["POST"], view_func=quest.questBattleContinue)

app.add_url_rule(
    "/storyreview/markStoryAcceKnown",
    methods=["POST"],
    view_func=quest.markStoryAcceKnown,
)
app.add_url_rule("/storyreview/readStory", methods=["POST"], view_func=quest.readStory)

app.add_url_rule("/act25side/battleStart", methods=["POST"], view_func=quest.questBattleStart)
app.add_url_rule("/act25side/battleFinish", methods=["POST"], view_func=quest.questBattleFinish)

app.add_url_rule("/car/confirmBattleCar", methods=["POST"], view_func=quest.confirmBattleCar)

app.add_url_rule("/templateTrap/setTrapSquad", methods=["POST"], view_func=quest.setTrapSquad)

app.add_url_rule(
    "/activity/act24side/battleStart",
    methods=["POST"],
    view_func=quest.questBattleStart,
)
app.add_url_rule(
    "/activity/act24side/battleFinish",
    methods=["POST"],
    view_func=quest.questBattleFinish,
)

app.add_url_rule("/activity/act24side/setTool", methods=["POST"], view_func=quest.setTool)

app.add_url_rule("/activity/bossRush/battleStart", methods=["POST"], view_func=quest.questBattleStart)
app.add_url_rule(
    "/activity/bossRush/battleFinish",
    methods=["POST"],
    view_func=quest.questBattleFinish,
)

app.add_url_rule("/activity/bossRush/relicSelect", methods=["POST"], view_func=quest.relicSelect)
app.add_url_rule(
    "/retro/typeAct20side/competitionStart",
    methods=["POST"],
    view_func=quest.typeAct20side_competitionStart,
)
app.add_url_rule(
    "/retro/typeAct20side/competitionFinish",
    methods=["POST"],
    view_func=quest.typeAct20side_competitionFinish,
)
app.add_url_rule("/rlv2/giveUpGame", methods=["POST"], view_func=rlv2.rlv2GiveUpGame)
app.add_url_rule("/rlv2/createGame", methods=["POST"], view_func=rlv2.rlv2CreateGame)
app.add_url_rule("/rlv2/chooseInitialRelic", methods=["POST"], view_func=rlv2.rlv2ChooseInitialRelic)
app.add_url_rule("/rlv2/selectChoice", methods=["POST"], view_func=rlv2.rlv2SelectChoice)
app.add_url_rule(
    "/rlv2/chooseInitialRecruitSet",
    methods=["POST"],
    view_func=rlv2.rlv2ChooseInitialRecruitSet,
)
app.add_url_rule(
    "/rlv2/activeRecruitTicket",
    methods=["POST"],
    view_func=rlv2.rlv2ActiveRecruitTicket,
)
app.add_url_rule("/rlv2/recruitChar", methods=["POST"], view_func=rlv2.rlv2RecruitChar)
app.add_url_rule("/rlv2/closeRecruitTicket", methods=["POST"], view_func=rlv2.rlv2CloseRecruitTicket)
app.add_url_rule("/rlv2/finishEvent", methods=["POST"], view_func=rlv2.rlv2FinishEvent)
app.add_url_rule("/rlv2/moveAndBattleStart", methods=["POST"], view_func=rlv2.rlv2MoveAndBattleStart)
app.add_url_rule("/rlv2/battleFinish", methods=["POST"], view_func=rlv2.rlv2BattleFinish)
app.add_url_rule("/rlv2/finishBattleReward", methods=["POST"], view_func=rlv2.rlv2FinishBattleReward)
app.add_url_rule("/rlv2/moveTo", methods=["POST"], view_func=rlv2.rlv2MoveTo)
app.add_url_rule("/rlv2/buyGoods", methods=["POST"], view_func=rlv2.rlv2BuyGoods)
app.add_url_rule("/rlv2/leaveShop", methods=["POST"], view_func=rlv2.rlv2LeaveShop)
app.add_url_rule("/rlv2/chooseBattleReward", methods=["POST"], view_func=rlv2.rlv2ChooseBattleReward)
app.add_url_rule("/shop/getSkinGoodList", methods=["POST"], view_func=shop.shopGetSkinGoodList)
app.add_url_rule("/story/finishStory", methods=["POST"], view_func=story.storyFinishStory)
app.add_url_rule("/quest/finishStoryStage", methods=["POST"], view_func=story.storyFinishStory)
app.add_url_rule("/user/auth", methods=["POST"], view_func=user.userAuth)
app.add_url_rule("/user/agreement", methods=["GET"], view_func=user.userAgreement)
app.add_url_rule("/user/checkIn", methods=["POST"], view_func=user.userCheckIn)
app.add_url_rule("/user/changeSecretary", methods=["POST"], view_func=user.userChangeSecretary)
app.add_url_rule("/user/login", methods=["POST"], view_func=user.userLogin)
app.add_url_rule("/user/changeAvatar", methods=["POST"], view_func=user.userChangeAvatar)
app.add_url_rule("/user/oauth2/v1/grant", methods=["POST"], view_func=user.userOAuth2V1Grant)
app.add_url_rule(
    "/user/info/v1/need_cloud_auth",
    methods=["POST"],
    view_func=user.userV1NeedCloudAuth,
)
app.add_url_rule("/user/yostar_createlogin", methods=["POST"], view_func=user.userYostarCreatelogin)
app.add_url_rule("/u8/user/v1/getToken", methods=["POST"], view_func=user.userV1getToken)
app.add_url_rule("/user/changeResume", methods=["POST"], view_func=user.user_changeResume)
app.add_url_rule("/social/getSortListInfo", methods=["POST"], view_func=user.social_getSortListInfo)
app.add_url_rule("/social/searchPlayer", methods=["POST"], view_func=user.social_searchPlayer)
app.add_url_rule(
    "/social/setAssistCharList",
    methods=["POST"],
    view_func=user.social_setAssistCharList,
)
app.add_url_rule("/social/setCardShowMedal", methods=["POST"], view_func=user.social_setCardShowMedal)
app.add_url_rule("/medal/setCustomData", methods=["POST"], view_func=user.medal_setCustomData)
app.add_url_rule(
    "/businessCard/changeNameCardComponent",
    methods=["POST"],
    view_func=user.businessCard_changeNameCardComponent,
)
app.add_url_rule(
    "/businessCard/changeNameCardSkin",
    methods=["POST"],
    view_func=user.businessCard_changeNameCardSkin,
)
app.add_url_rule("/sandboxPerm/sandboxV2/createGame", methods=["POST"], view_func=sandbox.createGame)
app.add_url_rule(
    "/sandboxPerm/sandboxV2/battleStart",
    methods=["POST"],
    view_func=sandbox.battleStart,
)
app.add_url_rule(
    "/sandboxPerm/sandboxV2/battleFinish",
    methods=["POST"],
    view_func=sandbox.battleFinish,
)
app.add_url_rule("/sandboxPerm/sandboxV2/setSquad", methods=["POST"], view_func=sandbox.setSquad)
app.add_url_rule(
    "/sandboxPerm/sandboxV2/homeBuildSave",
    methods=["POST"],
    view_func=sandbox.homeBuildSave,
)
app.add_url_rule("/sandboxPerm/sandboxV2/settleGame", methods=["POST"], view_func=sandbox.settleGame)
app.add_url_rule("/sandboxPerm/sandboxV2/eatFood", methods=["POST"], view_func=sandbox.eatFood)
app.add_url_rule(
    "/sandboxPerm/sandboxV2/exploreMode",
    methods=["POST"],
    view_func=sandbox.exploreMode,
)
app.add_url_rule(
    "/sandboxPerm/sandboxV2/monthBattleStart",
    methods=["POST"],
    view_func=sandbox.monthBattleStart,
)
app.add_url_rule(
    "/sandboxPerm/sandboxV2/monthBattleFinish",
    methods=["POST"],
    view_func=sandbox.monthBattleFinish,
)
app.add_url_rule("/gacha/normalGacha", methods=["POST"], view_func=gacha.normalGacha)
app.add_url_rule("/gacha/boostNormalGacha", methods=["POST"], view_func=gacha.boostNormalGacha)
app.add_url_rule("/gacha/finishNormalGacha", methods=["POST"], view_func=gacha.finishNormalGacha)
app.add_url_rule("/gacha/syncNormalGacha", methods=["POST"], view_func=gacha.syncNormalGacha)
app.add_url_rule("/gacha/getPoolDetail", methods=["POST"], view_func=gacha.getPoolDetail)
app.add_url_rule("/gacha/advancedGacha", methods=["POST"], view_func=gacha.advancedGacha)
app.add_url_rule("/gacha/tenAdvancedGacha", methods=["POST"], view_func=gacha.tenAdvancedGacha)
app.add_url_rule(
    "/user/auth/v1/token_by_phone_password",
    methods=["POST"],
    view_func=user.auth_v1_token_by_phone_password,
)
app.add_url_rule("/user/info/v1/basic", methods=["GET"], view_func=user.info_v1_basic)
app.add_url_rule("/user/oauth2/v2/grant", methods=["POST"], view_func=user.oauth2_v2_grant)
app.add_url_rule("/app/v1/config", methods=["GET"], view_func=user.app_v1_config)
app.add_url_rule("/general/v1/server_time", methods=["GET"], view_func=user.general_v1_server_time)
app.add_url_rule(
    "/u8/user/auth/v1/agreement_version",
    methods=["GET"],
    view_func=user.agreement_version,
)


@app.errorhandler(404)
def fallback(_) -> dict[str, dict[str, Any]]:
    return {"playerDataDelta": {"modified": {}, "deleted": {}}}

if __name__ == '__main__':
    cfg = read_json(CONFIG_PATH)

    host = cfg["server"]["host"]
    port = cfg["server"]["port"]
    app.run(host=host, port=port, debug=True)

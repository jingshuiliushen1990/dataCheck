#-*- coding:utf-8 -*-

from dataPreprocess.loadAllDictData import allExcelDictData
from dataCheck.sceneCheck import sceneCheckResult
from dataCheck.titleCheck import titleCheckResult
from dataCheck.arenaCheck import areanCheckResult
from dataCheck.growthFund import growthFundCheckResult
from dataCheck.kingdomCheck import kingdomCheckResult
from dataCheck.talentSkillCheck import talentSkillCheckResult
from dataCheck.monsterAttributeCheck import monsterAttrCheckResult
from dataCheck.shopCheck import shopCheckResult
from dataCheck.npcChallengeCheck import npcChallengeCheckResult
from dataCheck.roleLvCheck import roleLvCheckResult
from dataCheck.tradeCheck import tradeCheckResult
from dataCheck.payCheck import payCheckResult
from dataCheck.equipResolveCheck import checkEquipResolveResult
import time
import json
import urllib
import urllib3
import requests

# checkList = ["sceneCheckResult", "titleCheckResult", "areanCheckResult", "growthFundCheckResult", "kingdomCheckResult",
#              "talentSkillCheckResult", "monsterAttrCheckResult", "shopCheckResult", "npcChallengeCheckResult",
#              "roleLvCheckResult", "tradeCheckResult", "payCheckResult"]

checkList = {"sceneCheckResult":"场景",
              "titleCheckResult":"称号",
              "areanCheckResult":"个人竞技场",
              "growthFundCheckResult":"成长基金",
              "kingdomCheckResult":"王国事件",
              "talentSkillCheckResult":"天赋技能",
              "monsterAttrCheckResult":"怪物属性",
              "shopCheckResult":"商店",
              "npcChallengeCheckResult":"npc挑战",
              "roleLvCheckResult":"角色等级",
              "tradeCheckResult":"交易",
              "payCheckResult":"充值",
              "checkEquipResolveResult":"未鉴定装备分解"
              }

# robotUrl1 = "https://oapi.dingtalk.com/robot/send?access_token=9fe749815aaa826996e58195ecf9ea97a7b6ac0eaaae943f71ca9431fbcb2e0a"
robotUrl1 = "https://oapi.dingtalk.com/robot/send?access_token=0c2cf80264ba7714c6cedcf6d15664718742dad31a7c0ad7ce55b7b56d1a2bc7"

# with open("./result.txt",'w') as fData:
#     for i in checkList.keys():
#         excelCode = i+"(allExcelDictData)"
#         result = eval(excelCode)
#         if result:
#             fData.write("检查 " + str(checkList[i]) + " ：\n")
#             for iKey, iValue in result.items():
#                 result1["检查"+str(iKey)] = iValue
#                 title = str(iKey) + ":"
#                 fData.write(str(title)+"\n")
#                 for j in iValue:
#                     fData.write(str(j)+"\n")
#         else:
#             result1[str("检查 " + str(checkList[i]))] = " 没有异常问题。"
#             fData.write("检查 " + str(checkList[i]) + " 没有异常问题。\n")
#         fData.write("\n")


def write2File(checkDict, allExcelDictData):
    with open("./result.txt", 'w') as fData:
        for i in checkList.keys():
            excelCode = i + "(allExcelDictData)"
            result = eval(excelCode)
            if result:
                fData.write("检查 " + str(checkList[i]) + " ：\n")
                for iKey, iValue in result.items():
                    title = str(iKey) + ":"
                    fData.write(str(title) + "\n")
                    for j in iValue:
                        fData.write(str(j) + "\n")
            else:
                fData.write("检查 " + str(checkList[i]) + " 没有异常问题。\n")
            fData.write("\n")


def getResult(checkDict, allExcelDictData):
    result1 = {}
    for i in checkList.keys():
        excelCode = i + "(allExcelDictData)"
        result = eval(excelCode)
        if result:
            for iKey, iValue in result.items():
                result1["检查 " + str(iKey)] = iValue
        else:
            result1[str("检查 " + str(checkList[i]))] = " 没有异常问题。"
    return result1


# 结果信息预处理
def handleResult(checkResultDict):
    result = ""
    for ikey, ivalue in checkResultDict.items():
        if type(ivalue) != list:
            result += ikey
            result += " : "
            result += str(ivalue)+"\n\n"
        else:
            result += ikey
            result += " : "
            result += "\n"
            for i in ivalue:
                i = str(i) + "\n"
                result += i
            result += "\n"

    return result


def dingTalkRobot(robotUrl):
    msg = handleResult(getResult(checkList, allExcelDictData))
    # print("%%%%%%",msg)
    dingMsg = {
     "msgtype": "text",
     "text": {"content": msg,
              "title":"M1DataCheck检查结果："},
     "at": {"isAtAll": False}
    }

    headers = {"Content-Type":"application/json"}
    r = requests.post(robotUrl, data = json.dumps(dingMsg), headers = headers)
    # r = requests.post(robotUrl, data=dingMsg, headers=headers)
    print(r.text)



if __name__ == "__main__":
    write2File(checkList, allExcelDictData)
    dingTalkRobot(robotUrl1)
    print("程序执行完毕。请查看result或者setupLog日志。")
    time.sleep(5)


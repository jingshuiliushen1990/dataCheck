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


with open("./result.txt",'w') as fData:
    for i in checkList.keys():
        excelCode = i+"(allExcelDictData)"
        result = eval(excelCode)
        if result:
            fData.write("检查 " + str(checkList[i]) + " ：\n")
            for iKey, iValue in result.items():
                title = iKey + ":"
                fData.write(str(title)+"\n")
                for j in iValue:
                    fData.write(str(j)+"\n")
        else:
            fData.write("检查 " + str(checkList[i]) + " 没有异常问题。\n")
        fData.write("\n")

print("程序执行完毕。请查看result或者setupLog日志。")
time.sleep(5)





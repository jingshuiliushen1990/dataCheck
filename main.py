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
import time

checkList = ["sceneCheckResult", "titleCheckResult", "areanCheckResult", "growthFundCheckResult", "kingdomCheckResult",
             "talentSkillCheckResult", "monsterAttrCheckResult", "shopCheckResult", "npcChallengeCheckResult",
             "roleLvCheckResult", "tradeCheckResult", "payCheckResult"]

# print("%%%%%%%%%",eval("sceneCheckResult"+"(allExcelDictData)"))


with open("./result.txt",'w') as fData:
    for i in checkList:
        excelCode = i+"(allExcelDictData)"
        result = eval(excelCode)
        if result:
            for iKey, iValue in result.items():
                title = iKey + ":"
                fData.write(str(title)+"\n")
                for i in iValue:
                    fData.write(str(i)+"\n")
        fData.write("\n")

print("程序执行完毕。请查看result或者setupLog日志。")
time.sleep(5)





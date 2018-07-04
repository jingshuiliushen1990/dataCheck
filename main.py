#-*- coding:utf-8 -*-

from dataPreprocess.loadAllDictData import allExcelDictData
from checkCode.sceneCheck import sceneCheckResult
from checkCode.titleCheck import titleCheckResult
from checkCode.arenaCheck import areanCheckResult
from checkCode.growthFund import growthFundCheckResult
from checkCode.kingdomCheck import kingdomCheckResult
from checkCode.talentSkillCheck import talentSkillCheckResult
from checkCode.monsterAttributeCheck import monsterAttrCheckResult
from checkCode.shopCheck import shopCheckResult
from checkCode.npcChallengeCheck import npcChallengeCheckResult
from checkCode.roleLvCheck import roleLvCheckResult
from checkCode.tradeCheck import tradeCheckResult
from checkCode.payCheck import payCheckResult


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






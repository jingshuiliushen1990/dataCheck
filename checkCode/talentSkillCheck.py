# -*- coding:utf-8 -*-

from generalInterface.generalApi import *

# 天赋技能检查结果
def talentSkillCheckResult(allExcelDictData):
    result = []
    result = checkBuytalentSkill(allExcelDictData)
    return result


# 天赋技能购买时的技能点，序列，技能点消耗绑银，消耗经验的检查
def checkBuytalentSkill(allExcelDictData):
    result = []
    buytalentSkillData = allExcelDictData.get("天赋技能购买", None)
    if buytalentSkillData:
        count = 0
        tempData = createCheckDict(buytalentSkillData[0])
        usefulData = saveData2Dict(buytalentSkillData, tempData)
        for iKey in usefulData.keys():
            if iKey == "id":
                testList = [i for i in range(1, len(usefulData[iKey]) + 1)]
                if usefulData[iKey] != testList:
                    count += 1
                    location = findLvErrorLocation(usefulData[iKey])
                    wrongInfo = str(count)+". 技能点序列出现异常，问题出现在 "+str(location)+" 行，请检查确认。"
                    result.append(wrongInfo)
            if (iKey == "gold_amount" or iKey == "exp_amount"):
                newTestList = sorted(usefulData[iKey])
                if usefulData[iKey] != newTestList:
                    count += 1
                    location = findNoLvErrorLocation(usefulData[iKey])
                    wrongInfo = str(count)+". 列 "+iKey+" 出现问题, 在 "+str(location)+" 行，请检查确认。"
                    result.append(wrongInfo)
        return result
    else:
        return False



if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print("^^^^^^^^",talentSkillCheckResult(allExcelDictData))
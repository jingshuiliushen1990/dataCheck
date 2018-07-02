# -*- coding:utf-8 -*-

from generalInterface.generalApi import *

# 对王国纪元功能的检查
def kingdomCheckResult(allExcelDictData):
    result = {}
    result = checkLvProsperityResult(allExcelDictData)
    return result


# 检查王国纪元录中的消耗的繁荣值和玩家领奖等级检查
def checkLvProsperityResult(allExcelDictData):
    result = {}
    count = 0
    playerLvMax = getPlayerLvMax(allExcelDictData)
    kingdomCatalogData = allExcelDictData.get("王国纪元录", None)
    # print("$$$$$$$",kingdomCatalogData)
    keyDict = createCheckDict(kingdomCatalogData[0])
    usefulData = saveData2Dict(kingdomCatalogData, keyDict)
    prosperityData = usefulData.get("prosperity", None)
    playerLvData = usefulData.get("player_level", None)
    prosperityCheckResult = findNoLvErrorLocation(prosperityData)
    playerLvCheckResult = findNoLvErrorLocation(playerLvData)
    # print("*******", prosperityCheckResult)
    # print("&&&&&&&", playerLvCheckResult)
    tempList = []
    if prosperityCheckResult:
        count += 1
        wrongInfo = str(count)+". 升级需要繁荣值存在异常，错误位置在： "+str(prosperityCheckResult)+" 请确认。\n"
        tempList.append(wrongInfo)
    if playerLvCheckResult:
        count += 1
        wrongInfo = str(count) + ". 玩家领奖等级从低到高的顺序存在异常，错误位置在： " + str(playerLvCheckResult) + " 请确认。\n"
        tempList.append(wrongInfo)
    if playerLvData[-1] > playerLvMax:
        count += 1
        wrongInfo = str(count) + ". 玩家领奖等级存在异常，领奖等级大于玩家可以达到的最高等级，请确认。\n"
        tempList.append(wrongInfo)
    result["王国纪元录"] = tempList
    return result


# 检查王国时间抽取功能
def checkEventExtractResult(allExcelDictData):

    pass


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print("%%%%%%%%%", kingdomCheckResult(allExcelDictData))
    # kingdomCheckResult(allExcelDictData)
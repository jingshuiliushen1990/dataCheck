# -*- coding:utf-8 -*-

from generalInterface.generalApi import *

# 对王国纪元功能的检查
def kingdomCheckResult(allExcelDictData):
    result = {}
    tempResult1  = checkLvProsperityResult(allExcelDictData)
    tempResult2 = checkEventExtractResult(allExcelDictData)
    if tempResult1:
        result.update(tempResult1)
    if tempResult2:
        result.update(tempResult2)
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
        wrongInfo = str(count)+". 升级需要繁荣值存在异常，错误位置在： "+str(prosperityCheckResult)+" 请确认。"
        tempList.append(wrongInfo)
    if playerLvCheckResult:
        count += 1
        wrongInfo = str(count) + ". 玩家领奖等级从低到高的顺序存在异常，错误位置在： " + str(playerLvCheckResult) + " 请确认。"
        tempList.append(wrongInfo)
    if playerLvData[-1] > playerLvMax:
        count += 1
        wrongInfo = str(count) + ". 玩家领奖等级存在异常，领奖等级大于玩家可以达到的最高等级，请确认。"
        tempList.append(wrongInfo)
    if tempList:
        result["王国纪元录"] = tempList
        return result
    else:
        return False


# 检查王国时间抽取功能a
def checkEventExtractResult(allExcelDictData):
    result = {}
    tempDict = {}
    dayCheckList = []
    tempList = []
    kingdomEventData = allExcelDictData.get("王国事件抽取", None)
    for i in kingdomEventData:
        dayCheckList.append(i.get("open_day",None))
    # print("@@@@@@",dayCheckList)
    tempResult = checkOpenDay(dayCheckList)
    # print("&&&&&&",tempResult)
    if tempResult:
        count = 1
    else:
        count = 0
    for j in kingdomEventData:
        tempDict[j["open_day"]] = []
        for iKey, iValue in j.items():
            if iKey != "open_day":
                tempDict[j["open_day"]].append(iValue)
        if checkAllEqual(tempDict[j["open_day"]]):
            tempList.append(tempDict[j["open_day"]][0])
        else:
            count += 1
            wrongInfo = str(count)+". 开服天数为 "+str(j["open_day"])+" 的王国事件配置的event 1~~7 不是一样的，出现不一致，请检查。"
            tempResult.append(wrongInfo)
    if not checkTwoList(tempList[:-1], tempList[-1]):
        # print("$$$$$$$", tempList[:-1], " ******** ",tempList[-1])
        count += 1
        wrongInfo = str(count)+". 最后一行的的王国事件不是由前面几天的事件组成，请与策划确认。"
        tempResult.append(wrongInfo)
    if tempResult:
        result["王国事件抽取"] = tempResult
        return result
    else:
        return False


# 判断列表中的所有元素都是一样的
def checkAllEqual(iList):
    if (iList.count(iList[0]) == len(iList)):
        return True
    else:
        return False

# 判断两个列表中的元素都一样，元素顺序可能会不一样
def checkTwoList(iList1, iList2):
    if len(iList1) != len(iList2):
        return False
    else:
        for i in iList1:
            if i[0] not in iList2:
                return False
            else:
                continue
        return True


# 检查王国事件的开启时间是否存在重复或者间隔的现象
def checkOpenDay(dayList):
    result = []
    tempList = dayList[:-1]
    testList = [i for i in range(1, len(tempList)+1)]
    if ((tempList != testList) or (dayList[-1] != 999999)):
        wrongInfo = "1. 开服天数出现异常，出现天数不连续，或者最后一个配置的不是999999，请查证。"
        result.append(wrongInfo)
    return result


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print("%%%%%%%%%", kingdomCheckResult(allExcelDictData))
    # kingdomCheckResult(allExcelDictData)
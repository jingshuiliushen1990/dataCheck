#-*- coding:utf-8 -*-

from generalInterface.generalApi import *

# 得到检查结果，先判断是否有ID和等级异常的，有的话直接返回异常，没有的话在判断奖励数量是否存在异常
def checkGrowthFundResult(allExcelDictData):
    result = {}
    tempResult = []
    count = 0
    growthFundData = allExcelDictData.get("成长基金等级", None)
    keyDict = createCheckDict(growthFundData[0])
    usefulData = saveData2Dict(growthFundData, keyDict)
    # print("&&&&&&&&&", usefulData)
    checkKeyDict = {"id":"编号", "lv":"等级"}
    for ikey in checkKeyDict.keys():
        errorLocation = []
        testData = usefulData[ikey]
        if ikey == "id":
            errorLocation = findLvErrorLocation(testData)
        else:
            errorLocation = findNoLvNoEqualErrorLocation(testData)
        if errorLocation:
            count += 1
            wrongInfo = str(count) + ". 成长基金等级表中 "+str(checkKeyDict[ikey])+" 列中出现异常情况，位置是 "+str(errorLocation)+" 行，请策划确认是否正确。\n"
            tempResult.append(wrongInfo)

    rewardData = preprocessRewardList(usefulData["rewards"])
    secondKeyDict = createCheckDict(rewardData[0])
    secondUsefulData = saveData2Dict(rewardData, secondKeyDict)
    rewardIDErrorLocation = checkPointID(secondUsefulData["id"], 1002)
    if rewardIDErrorLocation:
        count += 1
        wrongInfo = str(count) + ". 成长基金等级 表中返还货币ID不是 1002 ，出现位置是: " + str(rewardIDErrorLocation) + " 行， 请策划确认是否正常。\n"
        tempResult.append(wrongInfo)
    rewardAmountErrorLocation = findNoLvErrorLocation(secondUsefulData["amount"])
    if rewardAmountErrorLocation:
        count += 1
        wrongInfo = str(count) + ". 成长基金等级 表中返还货币数量异常 ，出现位置是: " + str(rewardAmountErrorLocation) + " 行， 请策划确认是否正常。\n"
        tempResult.append(wrongInfo)

    if tempResult:
        result["成长基金等级"] = tempResult
        return result
    else:
        return False


# 预处理奖励列表
def preprocessRewardList(rewardList):
    result = []
    for i in rewardList:
        result.append(i[0])
    return result


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print(checkGrowthFundResult(allExcelDictData))
# -*- coding:utf-8 -*-

from generalInterface.generalApi import *

# 个人竞技场检查
def areanCheckResult(allExcelDictData):
    result = {}
    tempResult1 = robotCheckResult(allExcelDictData)
    tempResult2 = dailyRewardCheckResult(allExcelDictData)
    if tempResult1:
        result.update(tempResult1)
    if tempResult2:
        result.update(tempResult2)

    return result


# 检查个人竞技场机器人的等级和排名是否出现断点情况
def robotCheckResult(allExcelDictData):
    result = {}
    count = 0
    tempResult = []
    robotCheckData = allExcelDictData.get("个人竞技场_机器人", None)
    if robotCheckData:
        robotKeyDict = createCheckDict(robotCheckData[0])
        usefulRobotData = saveData2Dict(robotCheckData, robotKeyDict)
        rankCheck = checkRankResult(usefulRobotData['rank'])
        if rankCheck:
            count += 1
            wrongInfo = str(count)+". 个人竞技场_机器人 表中排名为 "+str(rankCheck)+" 的地方出现断点，请策划确认是否正常。\n"
            tempResult.append(wrongInfo)
        keyList = ["level", "real_lv"]
        for ikey in keyList:
            checkData = usefulRobotData[ikey]
            location = findReverseErrorLocation(checkData)
            # print("#########", checkData, " *********", location)
            if location:
                count += 1
                wrongInfo = str(count)+". 个人竞技场_机器人 表中 列名为 "+str(ikey)+" 的等级出现异常，异常位置在 "+ str(location)+\
                "行，请策划确认是否正常。\n"
                tempResult.append(wrongInfo)
            else:
                continue
        result["个人竞技场_机器人"] = tempResult
        return result
    else:
        return False


# 对排名进行检查，防止出现断点
def checkRankResult(rankList):
    result = []
    tempList = []
    for i in rankList:
        if ":" not in i:
            tempList.append(int(i))
        else:
            temp = list(map(int,i.split(":")))   # 把字符串列表转化为int列表，便于后面的比较计算
            tempList.extend(temp)

    for k in range(1,len(tempList)-1):
        if (tempList[k] - tempList[k-1]) != 1:
            if (tempList[k+1] - tempList[k] != 1):
                result.append(tempList[k])
            else:
                continue
        else:
            continue
    return result


# 检查个人竞技场每日奖励情况，还有检查排名是否出现断点情况
def dailyRewardCheckResult(allExcelDictData):
    result = {}
    tempResult = []
    count = 0
    rewardCheckData = allExcelDictData.get("个人竞技场_每日奖励", None)
    if rewardCheckData:
        rewardKeyDict = createCheckDict(rewardCheckData[0])
        usefulRewardData = saveData2Dict(rewardCheckData, rewardKeyDict)
        rankCheck = checkRankResult(usefulRewardData['rank'])
        if rankCheck:
            count += 1
            wrongInfo = str(count) + ". 个人竞技场_每日奖励 表中在排名为 " + str(rankCheck) + " 的地方出现断点，请策划确认是否正常。\n"
            tempResult.append(wrongInfo)
        tempList = []
        for i in rewardCheckData:
            tempList.append(i.get("points", None))
        pointsKeyDict = createCheckDict(tempList[0])
        usefulPointData = saveData2Dict(tempList, pointsKeyDict)
        pointId = usefulPointData['id']
        pointLocation = checkPointID(pointId, 2001)
        if pointLocation:
            count += 1
            wrongInfo = str(count) + ". 个人竞技场_每日奖励 表中积分奖励ID不是 2001 ，出现位置是: " + str(pointLocation) + "行， 请策划确认是否正常。\n"
            tempResult.append(wrongInfo)
        amountList = usefulPointData["amount"]
        amountLocation = findReverseErrorLocation(amountList)
        if amountLocation:
            count += 1
            wrongInfo = str(count) + ". 个人竞技场_每日奖励 表中积分奖励数量不是按照正常规则配置，出现位置是: " + str(amountLocation) + "行， 请策划确认是否正常。\n"
            tempResult.append(wrongInfo)
        if tempResult:
            result["个人竞技场_每日奖励"] = tempResult
            return result
        else:
            return False



if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print("%%%%%%%%%%", areanCheckResult(allExcelDictData))

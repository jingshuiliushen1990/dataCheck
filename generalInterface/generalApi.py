# -*- coding:utf-8 -*-

# 生成一个字典，其中key为每一张表的列名，value是有列中的数据组成的一个列表，
# 传入参数是每张表中第一个字典数据
def createCheckDict(singleDataDict):
    result = {}
    for i in singleDataDict.keys():
        result[i] = []

    return result


# 读取表格中的数据，然后把每列中的数据都保存到生成的字典中的value中
def saveData2Dict(singleSheetData, resultDict):
    for i in singleSheetData:
        for iKey, iValue in i.items():
            resultDict[iKey].append(iValue)

    return delInvalidData(resultDict)


# 对字典中的无效数据进行过滤
def delInvalidData(resultDict):
    return {iKey:iValue for iKey, iValue in resultDict.items() if not isAllZero(iValue)}


# 判断列表中的数据是否全部为0，是的话返回True，否者返回False
def isAllZero(iList):
    count = 0
    for i in iList:
        if i == 0:
            count += 1
        else:
            return False
    if (count == len(iList)):
        return True
    else:
        return False


# 比较两个列表，并查处两个列表的第一个不一样的地方，若全部一样，返回Fasle，反之，返回具体不一样的位置
def compare2List(dataList, testList):
    for i in range(len(dataList)):
        if (dataList[i] != testList[i]):
            return dataList.index(dataList[i])+1
        else:
            continue
    return False


# 查找除等级列表外的列表中（列表中可以出现相等的情况）出现错误的具体位置
def findNoLvErrorLocation(dataList):
    result = []
    for i in range(1,len(dataList)):
        # print("@@@@@@@@@  ",i, "  @@@@  ", dataList[i],"  @@@@ ", dataList[i-1])
        if (dataList[i] < dataList[i-1]):
            result.append(i + 4)
            # result.append(i)
        else:
            continue
    return result


# 查找除等级外列表外（并且列表中不能出现相等的情况）出现错误的具体位置
def findNoLvNoEqualErrorLocation(dataList):
    result = []
    for i in range(1, len(dataList)):
        if (dataList[i] <= dataList[i-1]):
            result.append(i + 4)
        else:
            continue
    return result


#查找等级列表中出现的错误位置
def findLvErrorLocation(dataList):
    result = []
    for i in range(len(dataList)):
        print("%%%",dataList[i], "####",i+1)
        if (dataList[i] != i+1):
            result.append(i + 4)
            # result.append(i)
        else:
            continue
    return result


# 查找从大到小排序的序列中的异常数据
def findReverseErrorLocation(dataList):
    result = []
    for i in range(len(dataList)-1):
        if(dataList[i] < dataList[i+1]):
            # result.append(i+2)
            result.append(i + 5)
        else:
            continue
    return result

# 获得当前游戏中玩家可以达到的最高等级
def getPlayerLvMax(allExcelDictData):
    serverLvData = allExcelDictData.get("服务器等级", None)
    if serverLvData:
        tempDict = createCheckDict(serverLvData[0])
        usefulData = saveData2Dict(serverLvData, tempDict)
        playerLvMax = usefulData.get("player_level_max", None)
        return playerLvMax[-1]
    else:
        return False

# 检查列表中的元素是否都与ID相等，不相等返回出错的位置
def checkPointID(pointList, ID):
    result = []
    for i in range(len(pointList)):
        if pointList[i] != ID:
            result.append(i+4)
        else:
            continue
    return result

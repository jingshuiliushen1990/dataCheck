# -*- coding:utf-8 -*-

from generalInterface.generalApi import *
import re

# 检查角色等级数据是否异常
def roleLvCheckResult(allExcelDictData):
    result = {}
    tempResult = []
    lvData = allExcelDictData.get("转生升级", None)
    if lvData:
        dataDict = createCheckDict(lvData[0])
        usefulLvData = saveData2Dict(lvData, dataDict)
        count = 0
        for iKey in usefulLvData.keys():
            testList = [i for i in range(1, len(usefulLvData["grade"])+1)]
            if (iKey == "grade" or iKey == "level"):
                if usefulLvData[iKey] != testList:
                    count += 1
                    location = findLvErrorLocation(usefulLvData[iKey])
                    wrongInfo = str(count) + ". 列 " + iKey + " 出现等级不连续异常， 具体位置是 " + str(location) + " 行"
                    tempResult.append(wrongInfo)

            if (iKey == "show_level_ch"):
                newTestList1 = handleTestShow_level_ch(testList)
                if usefulLvData[iKey] != newTestList1:
                    count += 1
                    location = findLvErrorLocation(handleShow_level_ch(usefulLvData[iKey]))
                    wrongInfo = str(count) + ". 列 " + iKey + " 出现显示等级不连续异常， 具体位置是 " + str(location) + " 行"
                    tempResult.append(wrongInfo)

            if (iKey == "max_exp"):
                newTestList2 = sorted(usefulLvData[iKey])
                if usefulLvData[iKey] != newTestList2:
                    count += 1
                    location = findNoLvErrorLocation(usefulLvData[iKey])
                    wrongInfo = str(count) + ". 列 " + iKey + " 出现升级经验消耗异常， 具体位置是 " + str(location) + " 行"
                    tempResult.append(wrongInfo)
    if tempResult:
        result["角色等级"] = tempResult
        return result
    else:
        return False


# 对显示等级进行特殊处理，每一个等级数值后面都添加一个汉字“级”，便于与原始数据比较
def handleTestShow_level_ch(iList):
    resultList = []
    for i in iList:
        resultList.append(str(i)+"级")
    return resultList

# 对显示等级数据进行处理，处理掉原始数据中的“级”，便于后面查找具体出错的位置：
def handleShow_level_ch(iList):
    resultList = []
    for i in iList:
        resultList.append(int(re.findall(r"\d+\.?\d*", i)[0]))
    return resultList


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print("%%%%%%%%%%",roleLvCheckResult(allExcelDictData))
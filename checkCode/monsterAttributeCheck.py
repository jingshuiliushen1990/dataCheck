# -*- coding:utf-8 -*-

from generalInterface.generalApi import *

# 获得可用数据
def getMonsterAttributeData(allExcelDictData):
    monsterAttributeData = allExcelDictData.get("怪物等级属性表", None)
    if monsterAttributeData:
        dataDict = createCheckDict(monsterAttributeData[0])
        usefulDataDict = saveData2Dict(monsterAttributeData, dataDict)
        return usefulDataDict
    else:
        return False


# 检查数据的合法性
def monsterAttrCheckResult(allExcelDictData):
    result = []
    usefulData = getMonsterAttributeData(allExcelDictData)
    if usefulData:
        count = 0
        for iKey, iValue in usefulData.items():
            if iKey == "lv":
                testList = [i for i in range(1,len(iValue)+1)]
                if testList != iValue:
                    count += 1
                    # print("*********** ikey = ", iKey, "iValue = ", iValue)
                    location = findLvErrorLocation(iValue)
                    wrongInfo = str(count)+ ". 怪物等级存在间隔等级，不连续，问题出现在第 " + str(location) + " 行"
                    result.append(wrongInfo)
                else:
                    continue
            else:
                testList = sorted(iValue)
                if testList != iValue:
                    count += 1
                    # print("*********** ikey = ", iKey, "iValue = ", iValue)
                    location = findNoLvErrorLocation(iValue)
                    wrongInfo = str(count) + ". 列 " + iKey + " 中出现高等级怪物的属性比低等级怪物的属性要差的情况，问题出现在第 " + str(location) + " 行"
                    result.append(wrongInfo)
                else:
                    continue
    return result



if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print("############",monsterAttrCheckResult(allExcelDictData))

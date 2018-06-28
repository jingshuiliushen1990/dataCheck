#-*- coding:utf-8 -*-


# 检查等级的唯一性
def checkLvUnique(growthFundData):
    result = []
    levelUnique = []
    for i in growthFundData:
        levelUnique.append(i["lv"])
    for j in levelUnique:
        if levelUnique.count(j) > 1:
            if j not in result:
                result.append(j)
            else:
                continue
        else:
            continue
    if result:
        return result
    else:
        return False


# 检查ID的唯一性
def checkIdUnique(growthFundData):
    result = []
    idUnique = []
    for i in growthFundData:
        idUnique.append(i["id"])
    for j in idUnique:
        if idUnique.count(j) > 1:
            if j not in result:
                result.append(j)
            else:
                continue
        else:
            continue
    if result:
        return result
    else:
        return False

# 获得等级列表
def getLvList(growthFundData):
    result = []
    for i in growthFundData:
        result.append(i["lv"])
    return result


# 比较两个字典中物品的数量是否满足高等级的奖励物品数量要不小于低等级的物品数量
def judgeAmount(iList1, iList2):
    len1 = len(iList1)
    len2 = len(iList2)
    if(len1 == len2):
        pass




# 获得每个等级配置的数据，格式为： {编号,等级}：[{物品ID，物品数量}]，然后检查数据是否异常
def checkReward(growthFundData):
    tempDict = {}
    for i in growthFundData:
        tempDict[i["lv"]] = i["rewards"]
    print("#####", tempDict)
    lvList = getLvList(growthFundData)
    print("&&&&&", lvList)
    for i in range(len(lvList)-1):
        temp1 = tempDict.get(lvList[i], None)
        temp2 = tempDict.get(lvList[i+1], None)
        if judgeAmount(temp1, temp2):
            pass




# 得到检查结果，先判断是否有ID和等级异常的，有的话直接返回异常，没有的话在判断奖励数量是否存在异常
def checkGrowthFundResult(allExcelDictData):
    result = []
    growthFundData = allExcelDictData.get("成长基金等级", None)
    checkReward(growthFundData)


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print(checkGrowthFundResult(allExcelDictData))
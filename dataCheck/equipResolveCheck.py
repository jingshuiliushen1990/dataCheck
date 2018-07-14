# -*- coding:utf-8 -*-

from generalInterface.generalApi import *

def checkEquipResolveResult(allExcelDictData):
    result = {}
    testData = getEquipData(allExcelDictData)
    uniEquipData = allExcelDictData.get("未鉴定装备", None)
    if uniEquipData:
        for i in uniEquipData:
            tempResult = []
            identifyPickList = getIDFromList(i.get("identify_pick", None))
            if not identifyPickList:
                tempResult.append("鉴定后可能获得的装备为空。")
            else:
                usageWay = checkEquipUsege(i.get("usage_ways", None))
                if not usageWay:
                    tempResult.append("装备的使用方式中没有可以分解。")
                else:
                    for id in identifyPickList:
                        idData = testData.get(id, None)
                        if not idData:
                            tempResult.append("鉴定后得到的装备ID "+str(id)+" 不存在。")
                        else:
                            # print("######## ", getIDFromList(i.get("gifts", None)), " **** ",idData["gifts"])
                            if not check2ListEqual(getIDFromList(i.get("gifts", None)), idData["gifts"]):
                                tempResult.append(("未鉴定装备分解得到的物品与鉴定后ID为 "+str(id)+" 的装备分解得到的物品不一样。"))
                            if not idData["isResolve"]:
                                tempResult.append("装备表中ID为 "+str(id)+" 的装备不可分解，请确认是否正确。")
                            if not idData["gifts"]:
                                tempResult.append("装备表中ID为 "+str(id)+" 的装备分解获得物品为空，请确认是否正确。")
            if tempResult:
                result[i["id"]] = tempResult
        return result
    return False


def getEquipData(allExcelDictData):
    result = {}
    allEquipData = allExcelDictData.get("装备", None)
    if allEquipData:
        for i in allEquipData:
            tempResult = {}
            usage = i.get("usage_ways", None)
            tempResult["isResolve"] = checkEquipUsege(usage)
            tempResult["gifts"] = getIDFromList(i.get("gifts", None))
            result[i.get("id", None)] = tempResult
        return result
    return False



# 判断物品的使用方式是否包含分解物品
def checkEquipUsege(useList):
    if not useList:
        return False
    else:
        if 'DECOMPOSE_ITEM' in useList:
            return True
        return False


# 从特定结构的数据中提取抽取编号，结构为[{'id':number, 'weight':number},{'id':number, 'weight':number}……]
def getIDFromList(ilist):
    if not ilist:
        return False
    else:
        result = []
        for j in ilist:
            result.append(j.get("id", None))
        return result



if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    # checkEquipResolveResult(allExcelDictData)
    print("$$$$$$$",checkEquipResolveResult(allExcelDictData))
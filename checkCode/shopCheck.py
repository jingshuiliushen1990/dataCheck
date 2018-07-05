# -*- coding:utf-8 -*-

from generalInterface.generalApi import *


checkSheetList = {"ShopGoods_钻石":1002, "ShopGoods_金币":7, "ShopGoods_杂货":1003}
#商店数据检查
def shopCheckResult(allExcelDictData):
    result = {}
    for iKey, iValue in checkSheetList.items():
        tempResult = currencyCheck(allExcelDictData, iKey)
        result.update(tempResult)
    return result


# 单价货币ID类型检查
def currencyCheck(allExcelDictData, sheetName):
    result = {}
    tempData = allExcelDictData.get(sheetName, None)
    if tempData:
        count = 0
        tempList = []
        for i in tempData:
            testKey = i.get("price_item_id", None)
            if testKey:
                if testKey != checkSheetList[sheetName]:
                    count += 1
                    wrongInfo = str(count)+". 商品ID为 "+str(i.get("good_id", None))+ " 的商品单价货币类型错误，错误值为： "+str(testKey)+", 请确认。"
                    tempList.append(wrongInfo)
                else:
                    continue
            else:
                count += 1
                wrongInfo = str(count) + ". 商品ID为 " + str(i.get("good_id", None)) + " 的商品单价货币类型有异常，为空，没有配置数据，请确认。"
                tempList.append(wrongInfo)
            result[sheetName] = tempList
        return result
    else:
        return False


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print("%%%%%%%%",shopCheckResult(allExcelDictData))
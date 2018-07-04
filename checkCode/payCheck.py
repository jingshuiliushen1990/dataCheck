# -*- coding:utf-8 -*-

import re
from generalInterface.generalApi import *

# 充值检查结果
def payCheckResult(allExcelDictData):
    result = {}
    tempResult1 = payGoodsCheckResult(allExcelDictData)
    if tempResult1:
        result.update(tempResult1)
    return result


# 充值商品列表检查
def payGoodsCheckResult(allExcelDictData):
    result = {}
    tempResult = []
    count = 0
    payGoodsData = allExcelDictData.get("充值商品列表", None)
    if payGoodsData:
        goodsKeyDict = createCheckDict(payGoodsData[0])
        usefulData = saveData2Dict(payGoodsData[:6], goodsKeyDict)
        if (len(usefulData["id"]) != len(set(usefulData["id"]))):
            count += 1
            wrongInfo = str(count)+". 充值商品表中 商品ID（字符串）列出现ID重复，请确认。\n"
            tempResult.append(wrongInfo)
        goodIDLocation = findLvErrorLocation(usefulData["good_id"])
        if goodIDLocation:
            count += 1
            wrongInfo = str(count)+". 充值商品表中 商品ID（数字）列出现ID异常，出错位置是 "+str(goodIDLocation)+" 行，请确认。\n"
            tempResult.append(wrongInfo)
        testList = [6,30,98,198,328,648]
        testList1 = [60,300,980,1980,3280,6480]
        checkList = ["goods_score", "rmb", "desc"]
        for ikey in checkList:
            checkData = usefulData[ikey]
            if (ikey in ["goods_score", "rmb"]):
                if checkData != testList:
                    count += 1
                    errorLocation = getErrorLocation(checkData, testList)
                    wrongInfo = str(count) +". 充值商品列表 "+str(ikey)+" 列出现配置问题，具体位置在 "+str(errorLocation)+" 行， 请与策划确认。\n"
                    tempResult.append(wrongInfo)
                else:
                    continue
            else:
                descCheckData = getDescNumber(checkData)
                # print("^^^^", descCheckData)
                if descCheckData != testList:
                    count += 1
                    errorLocation = getErrorLocation(descCheckData, testList1)
                    wrongInfo = str(count) + ". 充值商品列表 " + str(ikey) + " 列出现配置问题，具体位置在 " + str(
                        errorLocation) + " 行， 请与策划确认。\n"
                    tempResult.append(wrongInfo)
                else:
                    continue
        sellItemData = usefulData["sell_item"]
        sellItemKeyDict = createCheckDict(sellItemData[0])
        sellItemUsefulData = saveData2Dict(sellItemData, sellItemKeyDict)
        itemIdCheck = checkPointID(sellItemUsefulData["id"], 8)
        if itemIdCheck:
            count += 1
            wrongInfo = str(count) +". 充值商品列表 出售物品 列中物品ID配置有误，具体位置在 "+str(itemIdCheck)+" 行， 请与策划确认。\n"
            tempResult.append(wrongInfo)
        if (sellItemUsefulData["amount"] != testList1):
            count += 1
            errorLocation1 = getErrorLocation(sellItemUsefulData["amount"], testList1)
            wrongInfo = str(count) +". 充值商品列表 出售物品 列中物品数量配置有误，具体位置在 "+str(errorLocation1)+" 行， 请与策划确认。\n"
            tempResult.append(wrongInfo)
    if tempResult:
        result["充值商品列表"] = tempResult
        return result
    else:
        return False


# 拆分出商品描述中的数字，并且以列表形式返回
def getDescNumber(descList):
    result = []
    for i in descList:
        number = re.sub("\D","", i)
        if number:
            result.append(int(number))
        else:
            result.append(None)
    return result


# 确定出充值数额中出问题的数据的位置
def getErrorLocation(iList, testList):
    result = []
    for i in range(len(iList)):
        if iList[i] != testList[i]:
            result.append(i+4)
    return result


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print("#########",payCheckResult(allExcelDictData))
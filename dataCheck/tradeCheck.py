# -*- coding:utf-8 -*-

# 检查交易数据中的税率不能为0
def tradeCheckResult(allExcelDictData):
    result = {}
    tempResult = []
    tradeData = allExcelDictData.get("交易物品", None)
    if tradeData:
        count = 0
        for i in tradeData:
            taxRate = i.get("tax_rate", None)
            if not taxRate:
                count += 1
                wrongInfo = str(count)+". 道具ID为 "+str(i.get("id", None))+" 的交易物品的税率为 0，请确认是否正确。"
                tempResult.append(wrongInfo)
            else:
                continue
    if tempResult:
        result["交易检查"] =  tempResult
        return result
    else:
        return False


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print(tradeCheckResult(allExcelDictData))


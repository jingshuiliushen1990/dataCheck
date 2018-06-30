# -*- coding:utf-8 -*-

from generalInterface.generalApi import *

# 获得可用数据
def getPayInfoData(allExcelDictData, sheetName):
    payData = allExcelDictData.get(sheetName, None)
    if payData:
        dataDict = createCheckDict()
        pass






if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    pass
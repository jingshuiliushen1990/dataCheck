# -*- coding:utf-8 -*-

from generalInterface.generalApi import *

# 获得可用数据
def getMonsterAttributeData(allExcelDictData):
    monsterAttributeData = allExcelDictData.get("怪物等级属性表", None)
    if monsterAttributeData:
        dataDict = createCheckDict(monsterAttributeData[0])
        usefulDataDict = saveData2Dict(monsterAttributeData, dataDict)
        print("$$$$$$$$$ ", usefulDataDict)










if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    getMonsterAttributeData(allExcelDictData)

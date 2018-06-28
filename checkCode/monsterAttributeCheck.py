# -*- coding:utf-8 -*-

attributeList = ["skill_coe", "hp", "mp", "STR", "DEX", "INT", "SP", "VIT", ]

# 获得可用数据
def getMonsterAttributeData(allExcelDictData):
    monsterAttributeData = allExcelDictData.get("怪物等级属性表", None)
    if monsterAttributeData:
        for i in list(monsterAttributeData[0].keys()):
            i = []









if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    getMonsterAttributeData(allExcelDictData)

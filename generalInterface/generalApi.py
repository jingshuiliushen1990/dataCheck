# -*- coding:utf-8 -*-

# 生成一个字典，其中key为每一张表的列名，value是有列中的数据组成的一个列表，
# 传入参数是每张表中第一个字典数据
def createCheckDict(singleDataDict):
    result = {}
    for i in singleDataDict.keys():
        result[i] = []

    return result


# 读取表格中的数据，然后把每列中的数据都保存到生成的字典中的value中
def saveData2Dict(singleSheetData, resultDict):
    for i in singleSheetData:
        for iKey, iValue in i.items():
            resultDict[iKey].append(iValue)

    return delInvalidData(resultDict)


# 对字典中的无效数据进行过滤
def delInvalidData(resultDict):
    return {iKey:iValue for iKey, iValue in resultDict.items() if not isAllZero(iValue)}


# 判断列表中的数据是否全部为0，是的话返回True，否者返回False
def isAllZero(iList):
    count = 0
    for i in iList:
        if i == 0:
            count += 1
        else:
            return False
    if (count == len(iList)):
        return True
    else:
        return False


# 比较两个列表，并查处两个列表的第一个不一样的地方，若全部一样，返回Fasle，反之，返回具体不一样的位置
def compare2List(dataList, testList):
    for i in range(len(dataList)):
        if (dataList[i] != testList[i]):
            return dataList.index(dataList[i])+1
        else:
            continue
    return False


# 查找除等级列表外的列表中出现错误的具体位置
def findNoLvErrorLocation(dataList):
    for i in range(1,len(dataList)-2):
        if ((dataList[i] > dataList[i+1]) or (dataList[i] < dataList[i-1])):
            return i+2
        else:
            continue

#查找等级列表中出现的错误位置
def findLvErrorLocation(dataList):
    for i in range(1,len(dataList)-2):
        if ((dataList[i] >= dataList[i+1]) or (dataList[i] <= dataList[i-1])):
            return i+2
        else:
            continue




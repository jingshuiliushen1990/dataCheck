#-*- coding:utf-8 -*-

import os
import xlrd
import dataPreprocess.getFilePath
import datetime

filePath = dataPreprocess.getFilePath.getFilePath()
filePathExceptDescribe = ["你没有在filePath中配置excel数据所在的路径，请检查", "你配置的文件路径不存在，请检查",
                  "你配置的路径不包含excel数据，请检查"]

# 获得文件的名称字典，异常路径时的提示信息
def getFileInfo():
    if (filePath == -1):
        return filePathExceptDescribe[0]
    elif (filePath == -2):
        return filePathExceptDescribe[1]
    elif (filePath == -3):
        return filePathExceptDescribe[2]
    else:
        fileNameList = getFileName(filePath)
        return fileNameList

# 根据给的路径，获得路径下面所有的文件名，子文件夹以及子文件夹中的文件名，用字典的格式保存
def getFileName(iFilePath):
    tempNameList = os.listdir(iFilePath)
    fileNameDict = {}
    for iName in tempNameList:
        if iName.startswith('.'):
            continue
        else:
            path = os.path.join(iFilePath, iName)
            if os.path.isdir(path):
                fileNameDict[iName] = {}
            else:
                fileNameDict[iName] = None
    for ikey, ivalue in fileNameDict.items():
        if ivalue == {}:
            newPath = os.path.join(iFilePath, ikey)
            temp = getFileName(newPath)      #递归调用，可以解决文件夹中套文件夹的情况
            fileNameDict[ikey] = temp
        else:
            continue
    return fileNameDict


# 处理表格中的无用数据，当读取到一行全部为空的时候，就终止继续读数据
def judgeUsefulData(iList):
    count = 0
    for i in iList:
        if i != '':
            return False
        else:
            count += 1
    if count == len(iList):
        return True

# 获得单个excel表格中的数据，数据保存格式为{sheet名1：[sheet1数据], sheet名2：[sheet2数据],……}
def getSingleExcelData(iFilePath, iFileName):
    singleExcelData = {}
    excelFile = os.path.join(iFilePath, iFileName)
    # print("excelFile = ", excelFile)
    temp = xlrd.open_workbook(excelFile)
    for iSheet in temp.sheets():
        tempList = []
        for i in range(iSheet.nrows):
            if judgeUsefulData(iSheet.row_values(i)):
                break
            else:
                tempList.append(iSheet.row_values(i))
        singleExcelData[iSheet.name] = tempList

    return singleExcelData

# 获得excel表格中的数据，然后保存到字典中，保存格式为：  {文件名1：{sheet名1：[sheet1数据], sheet名2：[sheet2数据],……},
#                                                      文件名2：{sheet名1：[sheet1数据], sheet名2：[sheet2数据],……},……}
def getAllExcelData(fileNameDict):
    allExcelData = {}
    for ikey, ivalue in fileNameDict.items():
        if ivalue == None:
            allExcelData[ikey] = getSingleExcelData(filePath, ikey)
        else:
            newFilePath = os.path.join(filePath, ikey)
            for subKey, subValue in ivalue.items():
                newKey = ikey+'-'+subKey
                allExcelData[newKey] = getSingleExcelData(newFilePath, subKey)

    return allExcelData

def write2File(dictData):
    f = open("3.txt", 'w', encoding='utf-8')
    for ikey, ivalue in dictData.items():
        f.write(str(ikey))
        f.write('\n')
        if ivalue:
            for i, j in ivalue.items():
                f.write(str(i))
                f.write('\n')
                if j:
                    for k in j:
                        f.write(str(k))
                        f.write('\n')

    f.close()


if __name__ == "__main__":
    start = datetime.datetime.now()
    # print(filePath)
    # print(getFileInfo())
    # print(getAllExcelData(getFileInfo()))
    write2File(getAllExcelData(getFileInfo()))
    end = datetime.datetime.now()
    print("程序执行共使用： ",end-start," 秒！")
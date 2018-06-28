# -*- coding:utf-8 -*-

import dataPreprocess.xls2lua
import dataPreprocess.getSearchData
import datetime

# 通过xlrd直接处理excel表格数据，得到说有的数据，用于功能中关键字查询的数据池
getAllExcelData = dataPreprocess.getSearchData.getAllExcelData(dataPreprocess.getSearchData.getFileInfo())


if __name__ == "__main__":
    start = datetime.datetime.now()
    # print("vvvvv", allExcelDictData)
    # print("vvvvv", allExcelData)
    # print(get1Data(getAllExcelDictData()))
    print(dataPreprocess.xls2lua.getAllExcelDictData(dataPreprocess.getFilePath.getFilePath()))
    end = datetime.datetime.now()

    print("执行计算共用了 ",end-start," 秒！")


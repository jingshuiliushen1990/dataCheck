#-*- coding:utf-8 -*-

from dataPreprocess.loadAllDictData import allExcelDictData
from checkCode.sceneCheck import sceneCheckResult
from checkCode.titleCheck import titleCheckResult

print("#################")
print(sceneCheckResult(allExcelDictData))
print(titleCheckResult(allExcelDictData))

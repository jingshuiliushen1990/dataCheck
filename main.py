#-*- coding:utf-8 -*-

from dataPreprocess.loadAllDictData import allExcelDictData
from checkCode.sceneCheck import sceneCheckResult
from checkCode.titleCheck import titleCheckResult
from checkCode.arenaCheck import areanCheckResult
from checkCode.growthFund import growthFundCheckResult
from checkCode.kingdomCheck import kingdomCheckResult
from checkCode.talentSkillCheck import talentSkillCheckResult
from checkCode.monsterAttributeCheck import monsterAttrCheckResult
from checkCode.shopCheck import shopCheckResult
from checkCode.npcChallengeCheck import npcChallengeCheckResult
from checkCode.roleLvCheck import roleLvCheckResult
from checkCode.tradeCheck import tradeCheckResult
from checkCode.payCheck import payCheckResult


print(sceneCheckResult(allExcelDictData))
print(titleCheckResult(allExcelDictData))

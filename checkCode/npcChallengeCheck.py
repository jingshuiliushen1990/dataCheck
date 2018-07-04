#-*- coding:utf-8 -*-

# npc的召唤场景检查
def npcChallengeCheckResult(allExcelDictData):
    result = []
    npcChallengeData = allExcelDictData.get("npc挑战", None)
    if npcChallengeData:
        result = checkCallScene(npcChallengeData)
        return result
    else:
        return False


# 检查召唤场景是332101
def checkCallScene(npcChallengeData):
    result = {}
    tempResult = []
    count = 0
    for i in npcChallengeData:
        callScene = i.get("call_scene", None)
        if (callScene and callScene != 332101):
            count += 1
            wrongInfo = str(count)+". npc ID为 "+str(i.get("npc_id", None))+" 的npc召唤场景不是 332101，请确认是否正常。"
            tempResult.append(wrongInfo)
        else:
            continue
    if tempResult:
        result["npc挑战"] = tempResult
        return result
    return False


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print(npcChallengeCheckResult(allExcelDictData))
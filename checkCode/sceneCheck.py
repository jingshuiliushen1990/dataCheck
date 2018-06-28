#-*- coding:utf-8 -*-


def sceneCheckResult(allExcelDictData):
    result = []
    sceneData = allExcelDictData.get("场景列表", None)
    if sceneData:
        for i in sceneData:
            temp = []
            min_lv = i.get("min_lv", None)
            open_pvp = i.get("open_pvp", None)
            if (min_lv != 0 or open_pvp != 0):
                temp.append("场景ID = " + str(i["id"]))
                temp.append("场景名称 = " + i["name"])
                if (min_lv != 0 and open_pvp != 0):
                    temp.append("最小限制等级 = " + str(i["min_lv"]))
                    temp.append("开放PVP = " + str(i["open_pvp"]))
                elif (min_lv ==0 and open_pvp != 0):
                    temp.append("开放PVP = " + str(i["open_pvp"]))
                else:
                    temp.append("最小限制等级 = " + str(i["min_lv"]))
            if temp:
                result.append(temp)
    return result


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print(sceneCheckResult(allExcelDictData))



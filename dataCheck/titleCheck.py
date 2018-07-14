#-*- coding:utf-8 -*-


def titleCheckResult(allExcelDictData):
    result = {}
    tempResult = []
    titleData = allExcelDictData.get("称号列表", None)
    if titleData:
        for i in titleData:
            temp = []
            name = i.get("name", None)
            type = i.get("type", None)
            level = i.get("level", None)
            desc = i.get("desc", None)
            obtain_method = i.get("obtain_method", None)
            # print("%%%%%%%%",name, "^^^^^",type, "****",level, "&&&&",desc, "$$$$",obtain_method)
            if(name == '' or type == '' or level == 0 or desc == '' or obtain_method == ''):
                temp.append("名字 = "+ i["name"])
                temp.append("所属类别 = " + i["type"])
                temp.append("品质等级 = " + str(i["level"]))
                temp.append("称号描述 = " + i["desc"])
                temp.append("获取方式描述 = " + i["obtain_method"])
                # print("GGGGGGG", temp)

            if temp:
                tempResult.append(temp)
    if tempResult:
        result["称号检查"] = tempResult
        return result
    return False


if __name__ == "__main__":
    from dataPreprocess.loadAllDictData import allExcelDictData
    print(titleCheckResult(allExcelDictData))
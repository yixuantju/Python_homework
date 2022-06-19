
def For_maohao(words,wrong):
    a = ""
    wrong_for = 0  
    if len(words) == 4 and words[3][len(words[3])-1] != ":":  # 该行只有四个元素，且第四个元素的末尾不是冒号
            wrong_for = wrong + 1 
            a = " 在该行后添加冒号 "

    elif len(words) == 5 :  # 该行有不止四个元素
        if words[4] == ":" :# 第五个元素不是冒号 
            wrong_for = wrong + 1
            a = " 在该行后添加冒号 "
    return a, wrong_for

def ForCheck(i,line):
    tips_for = {}
    wrong = 0
    wrong_for = 0
    words = str(line).split() #字符串以空格为分割转为列表

    if "for" == words[0]: #如果for是该行第一个元素
        if len(words) > 5 or len(words) < 4:
            wrong_for = wrong_for + 1     
            tips_for[wrong_for] = " 检查是否有缺少的部分 或 检查是否有粘连的字符 "
        if words[2] != "in": #查询第三个元素是否为in
            wrong = wrong + 1
            tips_for[wrong] = " 将“in”放在合适的位置，即变量之后，遍历结构之前 "
        tip, wrong = For_maohao(words,wrong)
        tips_for[wrong] = tip
    else: #如果for不是该行前三个字符的话
        wrong_for = wrong_for + 1
        tips_for[wrong_for] = " 将“for”放在首位 或 检查是否有粘连的字符 "
    if wrong:
        print("第{}行有{}处错误，建议：{}".format(i,wrong,tips_for))
        return 1
    else:
        return 0
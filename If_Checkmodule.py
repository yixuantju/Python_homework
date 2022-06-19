

def If_maohao(words):
    a = ""
    wrong_if = 0 
    if words[len(words)-1] != ":" and words[len(words)-1][len(words[len(words)-1])-1] != ":" :  # 该行最后一个元素不是冒号 且 最后一个元素的最后一个字符不是冒号 and words[len(words)-2][len[words[len(words)-2]-1]] != ":"
            wrong_if = 1 
            a = " 在该行后添加冒号 "
    return a, wrong_if

def Elif_maohao(words):
    a = ""
    wrong_elif = 0  
    if words[len(words)-1] != ":" and words[len(words)-1][len(words[len(words)-1])-1] != ":" :  # 该行最后一个元素不是冒号 且 倒数第二个元素的最后一个字符不是冒号
            wrong_elif = 1 
            a = " 在该行后添加冒号 "
    return a, wrong_elif

def Else_maohao(words):
    a = ""
    wrong_else = 0  
    if len(words) == 1 and words[0][len(words[0])-1] != ":":  # 该行只有一个元素，且第一个元素的末尾不是冒号
            wrong_else = 1 
            a=" 在else后添加冒号 "
    elif len(words) != 1 :  # 该行有不止一个元素
        if words[1] != ":" and words[0][len(words[0])-1] != ":":# 第二个元素不是冒号 并且 第一个元素的末尾不是冒号
            wrong_else = 1
            a = " 在else后添加冒号 "
    return a, wrong_else

def IfCheck(i,line,text):
    j=i
    tips_if = {}
    tips_elif = {}
    tips_else = {}
    wrong_if = 0
    wrong_elif = 0
    wrong_else = 0
    words = str(line).split() #字符串以空格为分割转为列表 
    tip, wrong_if = If_maohao(words)
    if wrong_if:
        tips_if[wrong_if] = tip
    for line in text[i:len(text)]: #从i行(不算第i行)向下运行:
        j = j + 1
        if "elif" in line :
            words_elif = str(line).split()
            if "elif" == words_elif[0][0:4]:
                tip, wrong_elif = Elif_maohao(words_elif)
                if wrong_elif:
                    tips_elif[wrong_elif] = tip
            else:
                wrong_elif = wrong_elif + 1
                tips_elif[wrong_elif] = " 将“elif”放在该行首位 "

        if "else" in line :
            words_else = str(line).split()
            if "else" == words_else[0][0:4]:
                tip, wrong_else = Else_maohao(words_else)
                if wrong_else:
                    tips_else[wrong_else] = tip
            else:
                wrong_else = wrong_else + 1
                tips_else[wrong_else] = " 将“else”放在该行首位 "

        if  "if" in line:
            break
            
            

    if wrong_if or wrong_elif or wrong_else :
        if wrong_if:
            print("第{}行有{}处错误，建议：{}".format(i,wrong_if,tips_if))
        if wrong_elif:                         
            print("第{}行有{}处错误，建议：{}".format(j,wrong_elif,tips_elif))
        if wrong_else:
            print("第{}行有{}处错误，建议：{}".format(i,wrong_else,tips_else))
        return 1
    else:
        return 0


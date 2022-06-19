

from csv import QUOTE_ALL #??这什么自动生成


def Try_maohao(words, wrong):
    a = ""
    wrong_try=0  
    if len(words) == 1 and words[0][len(words[0])-1] != ":":  # 该行只有一个元素，且第一个元素的末尾不是冒号
            wrong_try = wrong + 1 
            a=" 在try后添加冒号 "
    elif len(words) != 1 :  # 该行有不止一个元素
        if words[1] != ":" and words[0][len(words[0])-1] != ":":# 第二个元素不是冒号 并且 第一个元素的末尾不是冒号
            wrong_try = wrong + 1
            a = " 在try后添加冒号 "
    return a, wrong_try

def Except_maohao(words, wrong):
    a = ""
    wrong_except = 0
    if len(words) == 1 and words[0][len(words[0])-1] != ":":# 该行只有一个元素，且该元素长度为6，也就是没有冒号
        wrong_except = wrong + 1 
        a = " 在except后添加冒号 "
    elif len(words) != 1: # 该行有不止一个元素
        if words[1] != ":" and words[0][len(words[0])-1] != ":":# 第二个元素不是冒号 并且 第一个元素的末尾不是冒号
            wrong_except = wrong + 1
            a = " 在except后添加冒号 " 
    return a, wrong_except

def Try_exceptCheck(i,line_init,text): #引用了这个函数就已知这行肯定有try
    wrong_try = 0
    wrong_except = 0
    j = i
    num_try = 0
    num_except = 0 
    tips_try = {}
    tips_except = {}
    words = str(line_init).split() #按空格分单词
    if "try" == words[0][0:3]: #如果try在该行第一个元素中   
        num_try = num_try + 1  #记一次try出现的个数
        tip, wrong_try = Try_maohao(words, wrong_try)
        if wrong_try:   #如果出错
            tips_try[wrong_try] = tip
        for line in text[i:len(text)]: #从i行(不算第i行)向下运行
            j = j + 1          #从j=i+1开始递增计数
            if "try" in line:
                words_try = str(line).split()
                if "try" == words_try[0][0:3]:
                    num_try = num_try + 1 #这是为了处理 try try except except 的结构
            if "except" in line:
                words_except = str(line).split()
                if "except" == words_except[0][0:6]:
                    num_except = num_except + 1
                    if num_except == num_try:
                        tip, wrong_except = Except_maohao(words_except, wrong_except)
                        if wrong_except:
                            tips_except[wrong_except] = tip
                        break #执行break可以结束这之后的循环，使j == len(text)没有机会成立
                else:
                    wrong_except = wrong_except + 1
                    tips_except[wrong_except] = " 将“except”放在首位 "
            if j == len(text):
                wrong_try = wrong_try + 1
                tips_try[wrong_try] = " 缺少对应的except "           
    else: #如果try不是该行前三个字符的话
        wrong_try = wrong_try + 1
        tips_try[wrong_try] = " 将“try”放在首位 "
    if wrong_try or wrong_except :
        if wrong_try:
            print("第{}行有{}处错误，建议：{}".format(i,wrong_try,tips_try))
        if wrong_except:
            print("第{}行有{}处错误，建议：{}".format(j,wrong_except,tips_except))
        return 1
    else:
        return 0


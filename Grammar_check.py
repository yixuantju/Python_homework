from For_Checkmodule import ForCheck
from Try_except_Checkmodule import Try_exceptCheck
from If_Checkmodule import IfCheck

keywords = ('for','try','if')

def getInput():
    file_name = input("请输入需要检查的文本：")
    while 1 :
        try:
            file_txt=open(file_name, 'r', encoding="UTF-8").read()     #以一个字符串的形式读出整个文件，        
            break                          
        except FileNotFoundError:
            file_name = input("找不到该文件，请输入可查询的文件名：") 
    return file_name, file_txt

def getText(file_txt):                       #定义函数读取文件    
    for p in file_txt:
        if not (ord("a")<=ord(p)<=ord("z") or ord("A")<=ord(p)<=ord("Z")):#根据编码值和if not去掉非字母字符
            p=" "

    return file_txt

def Num_keyword(words):
    counts = {}
    for_num = 0
    try_except_num = 0
    if_num = 0
    for word in words:                           
        if word in keywords:   
            counts[word] = counts.get(word,0)+1       #生成字典的内容:若该键存在则取其值并+1
    items = list(counts.items())                      #返回所有键值对信息，生成列表
    for i in range(len(counts)):                    
        word, count = items[i]
        if word == "for":
            for_num = count
        if word == "try":
            try_except_num = count
        if word == "if":
            if_num = count
    return for_num, try_except_num, if_num


def EnableCheck(for_num, try_except_num, if_num):
    if for_num: 
        from For_Checkmodule import ForCheck
    if try_except_num:
        from Try_except_Checkmodule import Try_exceptCheck
    if if_num:
        from If_Checkmodule import IfCheck


def Output_grammarCheck(file_name):
    i = 0
    a = 0
    b = 0
    c = 0
    text = open(file_name, 'r', encoding="UTF-8").readlines() #读成以行为元素的列表
    for line in text:       
        i = i+1
        if "for" in line:
            a = ForCheck(i, line) + a
        if "try" in line:
            b = Try_exceptCheck(i, line, text) + b
        if "if" in line:
            c = IfCheck(i, line, text) + c
    if a+b+c == 0:
        print("该代码无错误")        

def GrammarCheck():
    file_name, file_txt = getInput()
    letterWords_with_pace_for_seeking = getText(file_txt)
    for_num, try_except_num, if_num = Num_keyword(letterWords_with_pace_for_seeking)
    EnableCheck(for_num, try_except_num, if_num)
    Output_grammarCheck(file_name)

GrammarCheck()
keyword=('Fasle','def','if','raise','None','del','import','return',
         'True','elif','in','try','and','else','is','while',
         'as','except','lambda','with','assert','finally','nonlocal',
         'yield','break','for','not','class','from','or','continue','global','pass')

def getinput():
    a = input("请输入需要检测的文件：")
    return a

def getText(text):                             #定义函数读取文件
    txt = open(text,"r",encoding="UTF-8").read()
    for p in txt:
     if not (ord("a") <= ord(p) <= ord("z") or ord("A") <= ord(p) <= ord("Z")):#根据编码值和if not去掉非字母字符
       p = " "
    return txt

def Output_keyword(Code_txt):
    words = str(Code_txt).split()                  #用空格分隔文本并生成列表
    counts = {}
    for word in words:                           
        if word in keyword:   
            counts[word] = counts.get(word,0)+1   #生成字典的内容:若该键存在则取其值并+1
    items = list(counts.items())                  #返回所有键值对信息，生成列表
    items.sort(key = lambda x:x[1],reverse=True)  #对列表反排序:降序排列
    for i in range(len(counts)):                #counts里有多少个就打印多少个
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count)) #打印counts里有的元素和数量/左对齐 右对齐



def Show_keyword():
    text = getinput()
    Code_txt = getText(text)
    Output_keyword(Code_txt)








def getInput():
    h = eval(input("请输入需要转换为哈希值的数："))
    return h

def myhash_output(arKey):
   try:
     h = 0xF1000100
     g = h & 0xF0100100
     h = arKey^g
     print(h)
   except: print("输入错误，请输入数字")
   
def Myhash():     
     para_get = getInput()
     myhash_output(para_get)


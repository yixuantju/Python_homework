import turtle
import Progressbar as Pb
import importlib

def getInputs():
    a = input("请输入‘大’字的颜色：")
    b = eval(input("请输入‘大’字的字号："))
    return a, b 

def Pen_Move(x,y):#右上为正
    turtle.penup()
    turtle.seth(0)
    turtle.fd(x)
    turtle.seth(90)
    turtle.fd(y)

def Pen_Initialize(color,size):
    try:
        turtle.penup()
        turtle.fd(-130*size/10)
        turtle.pendown()
        turtle.pensize(25*size/10)
    except: print("输入错误，请输入颜色英文名称")
    try:turtle.pencolor(color)
    except: print("输入错误，请输入字号数值")

#并列的四个笔画函数  
def Heng_chinese(size):
    turtle.fd(260*size/10)
    turtle.fd(-130*size/10)
    
def Shu_chinese(size):
    Pen_Move(0,110*size/10)
    turtle.pendown()
    turtle.seth(-90)
    turtle.fd(110*size/10)

def Pie_Left_chinese(size):
    turtle.circle(-150*size/10,75)
    turtle.penup()
    turtle.home()
    
def Pie_Right_chinese(size):
    turtle.seth(-90)
    turtle.pendown()
    turtle.circle(150*size/10,75)


#输出“大”的函数
def DaOutput(color, size):
    importlib.reload(turtle)
    turtle.setup(0.99,0.99)
    Pen_Initialize(color,size)
    Pb.ProgressBar_begin(5)
    Heng_chinese(size)
    Pb.ProgressBar_inter(2,5)
    Shu_chinese(size)
    Pb.ProgressBar_inter(4,2)
    Pie_Left_chinese(size)
    Pb.ProgressBar_inter(3,4)
    Pie_Right_chinese(size)
    Pb.ProgressBar_end(3,3)

 
def Write_da_chinese():
    color, size = getInputs()
    DaOutput(color, size)   

 

 


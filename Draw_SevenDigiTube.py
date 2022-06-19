import math
import turtle
import time
import importlib

#math.sqrt(2)#根号2

def Show_menu_Draw(): 
    print(''' 
请选择你需要的功能(默认字体为Arial，默认大小为1，默认颜色为黑)：
                 1.显示输入的日期
                 2.显示当前系统时间
                 3.显示任意数字
                 4.调整字体
                 5.调整画笔格式
                 6.返回主菜单     ''')
    choose_next = eval(input("请输入对应功能前的编号："))
    return choose_next

def getInput():
    global color_in, size_in, digit_in, typeface_in
    color_in = input("请输入数码管颜色：")
    size_in = eval(input("请输入数码管大小：") )
    digit_in = eval(input("请输入一个整数："))
    typeface_in = input("请输入字体类型：")
    return color_in, size_in, digit_in, typeface_in


#定义一个方便移笔的函数
def pen_move(x,y):#右上为正
    try:
        turtle.penup()
        turtle.seth(0)
        turtle.fd(x)
        turtle.seth(90)
        turtle.fd(y)
    except: print("输入错误，请输入表示大小的数值")

#定义两个画边框的函数
def space_horizon(size):
    turtle.pendown()
    turtle.seth(45)
    turtle.fd(math.sqrt(8*size*size))
    turtle.seth(0)
    turtle.fd(42*size)
    turtle.seth(-45)
    turtle.fd(math.sqrt(18*size*size))
    turtle.seth(-135)
    turtle.fd(math.sqrt(8*size*size))
    turtle.seth(180)
    turtle.fd(42*size)
    turtle.seth(135)
    turtle.fd(math.sqrt(18*size*size))

def space_斜(size):
    turtle.pendown()
    turtle.seth(-45)
    turtle.fd(math.sqrt(8*size*size))
    turtle.seth(-math.atan(4)-90)
    turtle.fd(math.sqrt(1700*size*size))
    turtle.seth(-135)
    turtle.fd(math.sqrt(32*size*size))
    turtle.seth(135)
    turtle.fd(math.sqrt(8*size*size))
    turtle.seth(-math.atan(4)+90)
    turtle.fd(math.sqrt(1700*size*size))
    turtle.seth(45)
    turtle.fd(math.sqrt(32*size*size))

#定义两个向边框里填色的函数
def draw_horizon(size):
    turtle.begin_fill()
    space_horizon(size)
    turtle.end_fill()

def draw_斜(size):
    turtle.begin_fill()
    space_斜(size)
    turtle.end_fill()


def drawDigit(digit, fillcolor, size): #画数码管单个数字
    
    try:
        turtle.fillcolor(fillcolor)
    except:
        print("输入错误，请输入颜色英文名称")
    try:
        if digit in [2,3,4,5,6,8,9]:
            draw_horizon(size)
            pen_move(-2*size,-2*size)
        else:
            space_horizon(size)
            pen_move(-2*size,-2*size)
            
        if digit in [0,2,6,8]:
            draw_斜(size)
            pen_move(0,-48*size)
        else:
            space_斜(size)
            pen_move(0,-48*size)
            
        if digit in [0,2,3,5,6,8,9]:
            draw_horizon(size)
            pen_move(50*size,48*size)
        else:
            space_horizon(size)
            pen_move(50*size,48*size)

        if digit in [0,1,3,4,5,6,7,8,9]:
            draw_斜(size)
            pen_move(2*size,50*size)
        else:
            space_斜(size)
            pen_move(2*size,50*size)

        if digit in [0,1,2,3,4,7,8,9]:
            draw_斜(size)
            pen_move(-48*size,2*size)
        else:
            space_斜(size)
            pen_move(-48*size,2*size)

        if digit in [0,2,3,5,6,7,8,9]:
            draw_horizon(size)
            pen_move(-2*size,-2*size)
        else:
            space_horizon(size)
            pen_move(-2*size,-2*size)  
    
        if digit in [0,4,5,6,8,9]:   
            draw_斜(size)  
        else:
            space_斜(size)  
    
        turtle.seth(0)
        turtle.penup()
        pen_move(64*size,-48*size)
    except NameError:
        print("输入错误，请输入一个整数")
    except:
        print("其他错误")

def drawDigit_iso(fillcolor, size, digit):
    importlib.reload(turtle)
    turtle.setup(0.99,0.99)
    try:           
        drawDigit(digit, fillcolor, size)
    except NameError:
        print("输入错误，请输入一个整数")
    except:
        print("其他错误")

def drawDate_Now(fillcolor, size, typeface, date):   #date为日期，格式为‘%Y-%m=%d+’
    importlib.reload(turtle)
    turtle.setup(0.99,0.99)
    turtle.fillcolor(fillcolor)     
    pen_move(-300,0)
    try:
        for i in date:
            if i == '-':
                turtle.write('年',font = (typeface,18,"normal"))           
                pen_move(64*size,0)
            elif i == '=':
                turtle.write('月',font = (typeface,18,"normal"))
                pen_move(64*size,0)
            elif i == '+':
                turtle.write('日',font = (typeface,18,"normal"))
            else:
                drawDigit(eval(i),fillcolor,size)
    except:
        print("输入错误，请输入字体类型：")
            
def drawDate_Input(fillcolor, size, typeface):      
        date = input("请输入日期，如2001/7/2/：") #这个不适合放在统一的输入函数里，因为日期的功能要单独使用
        importlib.reload(turtle)
        turtle.setup(0.99,0.99)
        pen_move(-300,0)
        Time = "年月日"
        a = 0
        try:
            for i in date:
                if i == "/":
                    try:
                        turtle.write(Time[a], font = (typeface,18,"normal"))
                        a = a + 1
                        pen_move(64*size, 0)   
                    except:
                        print("输入错误，请输入字体类型：")
                        break
                else:
                    drawDigit(eval(i), fillcolor, size)
        except NameError:
                    print("输入错误，请输入日期，如2001/7/2/")
        except:
                    print("其他错误") 

def run_menu_Draw(fillcolor, size, digit, typeface, choose_next):
    try:
        while 1 :    
            while choose_next == 1:         
                drawDate_Input(fillcolor, size, typeface)
                break 
            while choose_next == 2:
                drawDate_Now(fillcolor, size, typeface, time.strftime('%Y-%m=%d+', time.gmtime())) 
                break 
            while choose_next == 3:         
                drawDigit_iso(fillcolor, size, digit)
                break
            while choose_next == 4:
                typeface = input("请输入字体类型：")
                break 
            while choose_next == 5:
                size = eval(input("请输入数码管大小："))
                fillcolor = input("请输入数码管颜色：")                
                break
            if choose_next == 6:
                break
    except: 
        print("输入错误，请输入对应功能前的编号")


def Draw_SevenDigiTube():
    fillcolor, size, digit, typeface = getInput()
    choose_next = Show_menu_Draw()
    run_menu_Draw(fillcolor, size, digit, typeface, choose_next)


















    





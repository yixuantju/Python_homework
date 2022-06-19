from Myhash_module import Myhash
from Da_chinese import Write_da_chinese
from Draw_SevenDigiTube import Draw_SevenDigiTube
from Check_keyword import Show_keyword
from SportsSimulation import SportSim
from URLreRead import OutputHTML
from Grammar_check import GrammarCheck

def Show_menu():
    global choose
    print(''' 
请选择你需要的功能：
                 1.哈希函数
                 2.写“大”字程序
                 3.七段数码管显示
                 4.显示文本中的保留字
                 5.模拟A和B的竞技比赛
                 6.读同一个页面中的多个URL
                 7.语法检测器
                 8.退出程序     ''')
    choose = eval(input("请输入对应功能前的编号："))
    


def run():
    while 1 :
        try:  
            Show_menu()
            while choose == 1:
                Myhash()
                break
            while choose == 2:
                Write_da_chinese()
                break
            while choose == 3:
                Draw_SevenDigiTube()
                break 
            while choose == 4:
                Show_keyword()
                break
            while choose == 5:
                SportSim()
                break
            while choose == 6:
                OutputHTML()
                break
            while choose == 7:
                GrammarCheck()
                break
            if choose == 8:    
                break 
        except: print("输入错误，请输入对应功能前的编号")

def main():
    run()

main()

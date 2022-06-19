from random import uniform

def printIntro():
    print("该程序模拟两个选手A和B的竞技比赛")
    print('''

程序运行需要用户输入：
    A和B的能力值（以0到10之间的整数表示）
    A和B的基础失误值（以0到10之间的整数表示）
    晴天、阴天、雨天、雪天四种天气发生的概率值（以0到10之间的整数表示）
    A和B竞技的局数（以整数表示） 
    选择A和B更适应的天气种类 

    ''' )

def getInputs():
    a = eval(input("请输入选手A的能力值(0-10): "))
    b = eval(input("请输入选手B的能力值(0-10): "))
    a_f = eval(input("请输入选手A的基础失误值(0-10): "))
    b_f = eval(input("请输入选手B的基础失误值(0-10): "))
    sunny = eval(input("请输入比赛时为晴天的概率值(0-10): "))
    cloudy = eval(input("请输入比赛时为阴天的概率值(0-10): "))
    rainy = eval(input("请输入比赛时为雨天的概率值(0-10): "))
    snowy = eval(input("请输入比赛时为雪天的概率值(0-10): "))
    weatherPreffer = input("请分别输入在晴天、阴天、雨天、雪天更擅长的选手名字(“A”或“B”)(如输入: ABBA ):")
    n = eval(input("模拟比赛的场次: "))
    return a, b, a_f, b_f, sunny, cloudy, rainy, snowy, weatherPreffer, n

def weather(sunnyChance, cloudyChance, rainyChance, snowyChance, weatherPreffer, faultA, faultB): 
    if   weatherPreffer[0] == "A":
        sunnyF_A = sunnyChance*0.4*faultA #更适应晴天表明在晴天犯错值更小
        sunnyF_B = sunnyChance*0.6*faultB #不适应晴天表明在晴天犯错值更大
    elif weatherPreffer[0] == "B":
        sunnyF_B = sunnyChance*0.4*faultB
        sunnyF_A = sunnyChance*0.6*faultA  

    if   weatherPreffer[1] == "A":
        cloudyF_A = cloudyChance*0.4*faultA
        cloudyF_B = cloudyChance*0.6*faultB
    elif weatherPreffer[1] == "B":
        cloudyF_B = cloudyChance*0.4*faultB
        cloudyF_A = cloudyChance*0.6*faultA      

    if   weatherPreffer[2] == "A":
        rainyF_A = rainyChance*0.4*faultA
        rainyF_B = rainyChance*0.6*faultB
    elif weatherPreffer[2] == "B":
        rainyF_B = rainyChance*0.4*faultB
        rainyF_A = rainyChance*0.6*faultA 

    if   weatherPreffer[3] == "A":
        snowyF_A = snowyChance*0.4*faultA
        snowyF_B = snowyChance*0.6*faultB
    elif weatherPreffer[3] == "B":
        snowyF_B = snowyChance*0.4*faultB
        snowyF_A = snowyChance*0.6*faultA

    a = (sunnyF_A + cloudyF_A + rainyF_A + snowyF_A)/40
    b = (sunnyF_B + cloudyF_B + rainyF_B + snowyF_B)/40 #除40是为了控制该值小于10
    return a, b     

def mixAllfactors(probA, probB, sunnyChance, cloudyChance, rainyChance, snowyChance, weatherPreffer, faultA, faultB):
    faultA_Weather,faultB_Weather = weather(sunnyChance, cloudyChance, rainyChance, snowyChance, weatherPreffer, faultA, faultB) #返回带有天气偏好的失误值
    a = probA*0.7 + (10 - faultA_Weather)*0.3 #基础能力值占70%，不失误值（10-失误值）占30%
    b = probB*0.7 + (10 - faultB_Weather)*0.3
    return a, b

def gameOver(a, b):        #打15下为一局
    return a==15 or b==15

def simOneGame(probA, probB, faultA, faultB, sunnyChance, cloudyChance, rainyChance, snowyChance, weatherPreffer):    
    probA_mixed, probB_mixed = mixAllfactors(probA, probB, sunnyChance, cloudyChance, rainyChance, snowyChance, weatherPreffer, faultA, faultB)
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB): #规定打多少次为一局结束
        if serving == "A":
            if uniform(0,10) < probA_mixed: #uniform(a,b)在a和b之间随机生成一个小数
                scoreA += 1
            else:
                serving = "B"
        else:
            if uniform(0,10) < probB_mixed:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def simNGames(probA, probB, faultA, faultB, sunnyChance, cloudyChance, rainyChance, snowyChance, weatherPreffer, n):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, faultA, faultB, sunnyChance, cloudyChance, rainyChance, snowyChance, weatherPreffer)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))

def SportSim():
    printIntro()  #必要性说明
    probA, probB, faultA, faultB, sunnyChance, cloudyChance, rainyChance, snowyChance, weatherPreffer, n = getInputs() #输入量   
    winsA, winsB = simNGames(probA, probB, faultA, faultB, sunnyChance, cloudyChance, rainyChance, snowyChance, weatherPreffer, n) #输出双方获胜局数  
    printSummary(winsA, winsB) #输出文本











import time
import sys
from random import randint

#玩家
class Player():
    def __init__(self,stoneNumber):
        self.stoneNumber=stoneNumber#灵石数量
        self.warriors={}#拥有的战士，包括弓箭兵和斧头兵

#战士
class Warrior():
    def __init__(self,strength):#生命值
        self.strength=strength
    def healing(self,stoneCount):#灵石疗伤
        self.strength += stoneCount
        if self.strength == self.maxStrength:
            return
        elif self.strength>self.maxStrength:#战士的生命值不能超过最大生命值
            self.strength=self.maxStrength
        
        

#弓箭兵
class Archer(Warrior):
    typeName="弓箭兵"      #名称
    price=100       #雇佣价
    maxStrength=100           #最大生命值
    def __init__(self,strength=maxStrength):    #生命值，名字
        Warrior.__init__(self,strength)
        
    def fightWithMonster(self,monster):
        if monster.typeName=='鹰妖':
            self.strength-=20
        elif monster.typeName=='狼妖':
            self.strength-=80
        else:
            print('!!!出现未知类型的妖怪！！！')

    def if_vic():
        if self.strength < 0:
            return False
        else:
            return True

#斧头兵
class Axemen(Warrior):
    typeName='斧头兵'  #名称  
    price=120       #雇佣金
    maxStrength=120      #最大生命值
    def __init__(self, strength=maxStrength):  # 生命值，名字
        Warrior.__init__(self, strength)
        

    def fightWithMonster(self, monster):       #和妖怪战斗
        if monster.typeName == '鹰妖':
            self.strength -= 80
        elif monster.typeName == '狼妖':
            self.strength -= 20
        else:
            print('!!!出现未知类型的妖怪！！！')
    def if_vic():
        if self.strength<0:
            return False
        else:
            return True

#鹰妖
class Eagle():
    typeName='鹰妖'

#狼妖
class Wolf():
    typeName='狼妖'

#森林
class Forest():
    def __init__(self,monster):#森林里的怪物
        self.monster=monster

print('*****************************    游戏开始     ******************')
#森林数量
forest_num=7

#森林列表
forestList=[]
#随机产生鹰妖和狼妖

for i in range(forest_num):
    typeName=randint(0,1)
    if typeName==0:
        forestList.append(Forest(Eagle()))
    else:
        forestList.append(Forest(Wolf()))
#显示妖怪信息    
    print('第', i+1,'座森林，里面是',forestList[i].monster.typeName)    
time.sleep(10)
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
stoneNumber=1000

#购买战士
Archer_num=int(input('弓箭兵数量：'))
Axemen_num=int(input('斧头兵数量：'))
stoneNumber -= (Archer_num+Axemen_num)*100
print('yuhewei',stoneNumber)
warrior_name = input('为您的战士命名：')
warriors_list = list(warrior_name)
print('命名完成，3秒后游戏开始，进入第一个森林')
time.sleep(3)
#11111111
print('*****1*****')
r1=input('第一场战士：')
for i in warriors_list[:Archer_num-1]:
    if i == r1:
        r1=Archer()
        r1.strength=100
        g1 = forestList[0].monster
        r1.fightWithMonster(g1)
        print(r1.strength)
    else:
        r1=Axemen()
        r1.strength=100
        r1.fightWithMonster(forestList[0].monster)
        print(r1.strength)
print('over')
healing1=int(input('1_buchong:'))
r1.healing(healing1)
stoneNumber-=healing1
print('yuhewei:',stoneNumber,'shengmingzhi:',r1.strength)
#######
print('**********')
for i in range(2,8):
    r2 = input('该场战士：')
    if r1==r2:
        r2=r1()
        r2.fightWithMonster(forestList[i-1].monster)
        print(r2.strength)
    else:   
        for i in warriors_list[:Archer_num-1]:

            if i == r2:
                r2= Archer()
                r2.strength = 100
                r2.fightWithMonster(forestList[i-1].monster)
                print(r2.strength)
            else:
                r2 = Axemen()
                r2.strength = 100
                r2.fightWithMonster(forestList[i-1].monster)
                print(r2.strength)
    print('over')
    if r2.if_vic:
        print('该场战斗胜利！')
    else:
        print('战斗失败，游戏结束。')
        break
    healing2 = int(input('对该战士的温养值:'))
    r2.healing(healing2)
    stoneNumber -= healing2
    print('灵石余额:', stoneNumber, '生命值:', r2.strength)

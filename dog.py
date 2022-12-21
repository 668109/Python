import time
import random
import os
import sys

class Dog:
    def __init__(self, name):
        self.__name = name
        self.__age = None
        print("你好，我是",self.__name)

    def set_age(self, age):
        self.__age = age
        
    def cakan(self):
        print("名字：",self.__name)
        print("年龄：",self.__age)
        print("状态:",jt,"(通过玩耍增加)")
        print("饱食度：",food,"(通过吃饭增加)")
        if sleeping:
            h = list(open("ptime.txt","r"))
            qwert = time.time() - float(str(h[0]))
            sleepdc = (28800 - (time.time() - float(str(h[0])))) / 3600.0
            print("是否睡觉:",sleeping,"小狗还有",sleepdc,"小时醒来")
        else:
            print("是否睡觉:",sleeping)
    def play(self):
        global jt
        if jt >= 90 or sleeping:
            print("小狗不想玩或正在睡觉")
        else:
            a = random.randint(1,3)
            if a == 1:
                print("你摸了摸小狗，小狗很高兴，状态+5")
                jt += 5
            elif a == 2:
                print("你挠了挠小狗的肚皮，小狗很高兴，状态+5")
                jt += 5
            elif a == 3:
                print("你和小狗玩了一会儿，小狗很高兴，状态+10")
                jt += 10

    def eat(self):
        global food
        if food >= 90 or sleeping:
            print("小狗不想吃或小狗正在睡觉")
        else:
            print("你喂食了小狗，小狗吃饱了，饱食度+15")
            food += 15

    def sleep(self):
        global sleeping
        if sleeping == False:
            print("小狗睡着了")
            sleeping = True
            f = open("ptime.txt","w")
            f.write(str(time.time()))
        else:
            print("小狗正在睡觉中")


    def quit(self):
        print("正在保存中")
        v = open("dog.txt","w")
        j2 = str(self.__name)  + "\n" + str(self.__age) + "\n" + str(time.time())
        j3 = str(jt) + "\n" + str(food) + "\n" + str(int(sleeping)) + "\n" + j2
        print(v.write(j3))
        sys.exit()
    
folder = os.path.exists("dog.txt")
if folder:
    print("loading......")
    time.sleep(5)
    q = list(open("dog.txt","r"))
    e1 = str(q[0]);e2 = str(q[1]);e3 = str(q[2]);e8 = str(q[3]);e9 = str(q[4])
    quittime = float(str(q[5]))
    sleeping = bool(int(e3[0:2]))
    jt = int(e1[0:-1])
    food = int(e2[0:-1]) 
    dog = Dog(e8[0:-1])
    dog.set_age(int(e9[0:-1]))
    print("加载成功")
    timetime = int((time.time() - quittime) // 3600)
    jt -= timetime * 3
    food -= timetime * 5
    time.sleep(1)
    if os.path.exists("ptime.txt"):
        filetime = list(open("ptime.txt","r"))
        if time.time() - float(filetime[0]) >= 28800.0:
            sleeping = False

else:
    print("loading......")
    jt = 40
    food = 40
    sleeping = False
    dogname = input("小狗的名字是：")
    while True:
        age1 = input("小狗的年龄是：")
        a = age1.isdigit()
        if a:
            if int(age1) > 0 and int(age1) < 20:
                break
            else:
                print("错误，请重试")
        else:
            print("错误，请重试")
    dog = Dog(dogname)
    dog.set_age(age1)
    print("加载成功")
    time.sleep(2)

while True:
    while True:
        try:
            print("""\

汪汪汪，我是小狗。
你想给想给小狗做什么?
1.查看小狗资料   2.和小狗玩  3.喂小狗吃饭
4.让小狗睡觉     5.退出      6.关闭电脑(请输入数字)""")
            number = int(input("请输入选项:"))
            break
        except ValueError:
            print("您输入的不是数字，请重试!!!")
    if number == 1:
        dog.cakan()
        time.sleep(3)
    elif number == 2:
        dog.play()
        time.sleep(3)
    elif number == 3:
        dog.eat()
        time.sleep(3)
    elif number == 5:
        dog.quit()
    elif number == 4:
        dog.sleep()
    elif number == 6:
        print("你的电脑将在30秒后关闭")
        os.system("shutdown -s")
        input()
        os.system("shutdown -a")
    elif number == 10:
        print("彩蛋!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        os.system("python maths.py")
    else:
        print("数字太大了!!!")

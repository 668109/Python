import random
print("欢迎来到猜数字小游戏，我是小狗。提示：请输入数字，否则会报错")
while True:
    a1 = int(input("设置范围，第一个数字是多少？"))
    a2 = int(input("设置范围，第二个数字是多少？"))
    a = random.randint(a1,a2)
    print("设置成功！数字的范围是",a1,"—",a2)
    maths = int(input("你猜的数字是多少？"))
    if maths == a:
        print("恭喜！你猜对了！")
    elif maths > 100000000:
        print("你有病吧，SB")
    else:
        print("很遗憾，你猜错了")


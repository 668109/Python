
a=input("今天星期几？")

if a == "1" or a=="3" or a=="5":
     print("今天吃米饭")
elif a == "2" or a == "4" or a == "6":
    print("今天吃面")
elif a == "7":
    print("今天吃包子")
else:
    print("没有星期"+a)
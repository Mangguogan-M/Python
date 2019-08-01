import random
times = 3
scr = random.randint(1, 100)
while times:
    num = input("请输入1-100之间的整数：")
    if num.isdigit():
        temp = int(num)
        if temp == scr:
            print("恭喜你，猜对了")
        elif temp < scr:
            print("你的数字太小了")
            times -= 1
        else:
            print("你的数字太大了")
            times -= 1
    else:
        print("让你输入数字的")
print("你的机会都用完了")
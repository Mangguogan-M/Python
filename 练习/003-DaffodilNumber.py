# 水仙花数
for i in range(100, 1000):
    temp = list(str(i))
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    if a**3 + b**3 + c**3 == i:
        print(i)
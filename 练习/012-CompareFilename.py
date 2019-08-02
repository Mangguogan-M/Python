file1 = input("请输入要比较的第一个文件名：")
file2 = input("请输入要比较的第二个文件名：")


def file_compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)

    count = 0
    differ = []

    for line1 in f1:
        line2 = f2.readline()

        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()

    return differ


differ = file_compare(file1, file2)

if len(differ) == 0:
    print("两个文件完全相同")
else:
    print("两个文件有%d处不同"%len(differ))
    for each in differ:
        print("第%d行不同" % each)
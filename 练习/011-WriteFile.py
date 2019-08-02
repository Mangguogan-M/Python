file_name = input("请输入文件名：")

def file_write(file_name):
    f = open(file_name, "w")
    print("请输入内容，（单独输入:w保存退出）")
    while True:
        write_something = input()
        if write_something != ":w":
            f.write("%s\n" % write_something)
        else:
            break
    f.close()
file_write(file_name)
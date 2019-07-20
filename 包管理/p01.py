class Student():
    def __init__(self, name="noName", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print("Hi,nihao a ")

# 此判断语句建议一直作为程序的入口
if __name__ == '__main__':
    print("我是模块P01")
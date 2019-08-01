class ListInfo(object):
    def __init__(self, list_value):
        self.listt = list_value

    def add_key(self, key_name):
        if isinstance(key_name, (str, int)):
            self.listt.append(key_name)
            print(self.listt)
            return "OK"
        else:
            return "我要的是数字"

    def get_key(self, index):
        if index >= 0 and index < len(self.listt):
            return self.listt[index]
        return "你输入的太多了"

    def update_list(self, new_list):
        self.listt.extend(new_list)
        return self.listt

    def del_key(self):
        if len(self.listt) >= 0:
            return self.listt.pop(-1)
        else:
            return "列表是空的"

list_info = ListInfo([1,2,3,4,5])
print(list_info.add_key(6))
print(list_info.get_key(3))
print(list_info.update_list([7,8,9]))
print(list_info.del_key())

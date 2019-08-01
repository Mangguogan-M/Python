class SecInfo(object):
    def __init__(self, my_set):
        self.sett = my_set

    def add_setInfo(self, keyname):
        self.sett.add(keyname)
        return self.sett

    def get_intersection(self, uniomInfo):
        return self.sett & uniomInfo

    def get_uniom(self, uniomInfo):
        return self.sett | uniomInfo

    def del_difference(self, uniomInfo):
        return self.sett - uniomInfo

A = set([1,2,3,4,5])
B = set([6,7,8,3,5])
myset = SecInfo(A)
print(myset.add_setInfo(10))
print(myset.get_intersection(B))
print(myset.get_uniom(B))
print(myset.del_difference(B))
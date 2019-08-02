class Ticket():
    def __init__(self, weekend = False, child = False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1

        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def cal_price(self, num):
        return self.exp * self.inc * num * self.discount


adult = Ticket()
child = Ticket(child=True)

print("两个大人和一个小孩子平日里的价格是{}".format(adult.cal_price(2) + child.cal_price(1)))            
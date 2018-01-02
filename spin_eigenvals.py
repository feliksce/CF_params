import math
import pandas as pd
# from fractions import Fraction as F
class Operator:

    def __init__(self, S, M):
        self.S = S
        self.M = M

    def s_x(self):
        return 0.5*(self.s_plus()+self.s_minus())

    def s_y(self):
        return -0.5 * complex(0, 1) * (self.s_plus() - self.s_minus())

    def s_z(self):
        return self.M

    def s_plus(self):
        return math.sqrt(self.s_squared()-self.m_squared())

    def s_minus(self):
        return math.sqrt(self.s_squared() - self.m_squared(False))

    # S(S+1)
    def s_squared(self):
        return self.S*(self.S+1)

    # when plus=True: M(M+1), else: M(M-1)
    def m_squared(self, plus=True):
        if plus: return self.M*(self.M+1)
        else: return self.M*(self.M-1)

#
if __name__ == "__main__":
    S = 1.5
    M = [each/10 for each in range(int(-S*10), int((S+1)*10), 10)]
    ran_x = [round(Operator(S, each).s_x(), 2) for each in M]
    ran_x2 = [round(Operator(S, each).s_x() ** 2, 2) for each in M]
    # ran_y = [Operator(S, each).s_y() for each in M]
    # ran_z = [Operator(S, each).s_z() for each in M]

    print("___\t{}".format(M))
    print("S_x^2\t{}".format(ran_x2))
    print("S_x\t{}".format(ran_x))
    # # print("S_x\t{}".format(ran_x_frac))
    # print("S_x\t{}\tCaution! This calculation yields rounded numbers!".format(ran_x_frac_round))
    # print("S_y\t{}".format(ran_y))
    # print("S_z\t{}".format(ran_z))

# TODO trzeba uwzględnić, że operatory wznoszące i opadające manifestują się dla wartości własnych pośrednich względem m_s, więc zwykłą suma nie wystarczy do ogarnięcią


# def print_table(S, **kwargs):
#     M = [each / 10 for each in range(int(-S * 10), int((S + 1) * 10), 10)]
#     print("___\t{}".format(M))
#     for each in kwargs:
#         print("{}\t{}".format(each.__name__, each))
#
# def calculate_ran():
#     ran_x = [round(Operator(S, each).s_x() ** 2, 2) for each in M]
#     ran_x_frac = [F.from_float(Operator(S, each).s_x()) for each in M]
#     ran_x_frac_round = [F.from_float(Operator(S, each).s_x()).__round__(2) for each in M]
#     ran_y = [Operator(S, each).s_y() for each in M]
#     ran_z = [Operator(S, each).s_z() for each in M]
#     return ran_x, ran_x_frac, ran_x_frac_round, ran_y, ran_z
#
# a = calculate_ran()
#
# print_table(1, a)
#
# if __name__ == "__main__":
#     S = 0.5
#     M = [each/10 for each in range(int(-S*10), int((S+1)*10), 10)]
#     print("xxx\ts+\ts-\ts tot")
#     # print("sx\t{}\t{}\t{}").format(Operator.s_plus, Operator.s_minus, Operator.s_x)
#     # print("sy\t{}\t{}\t{}").format(Operator.s_plus, Operator.s_minus, Operator.s_y)
#     print("sx\t{}\t{}\t{}").format(0, 0, Operator.s_x)
#     print("sy\t{}\t{}\t{}").format(0, 0, Operator.s_y)
#     print("sz\t-\t-\t{}").format(Operator.s_z)

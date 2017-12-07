import math


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

    def s_squared(self):
        return self.S*(self.S+1)

    def m_squared(self, plus=True):
        if plus: return self.M*(self.M+1)
        else: return self.M*(self.M-1)


if __name__ == "__main__":
    S = 20
    M = [each/10 for each in range(int(-S*10), int((S+1)*10), 10)]
    ran_x = [Operator(S, each).s_x()**2 for each in M]
    ran_y = [Operator(S, each).s_x()**2 for each in M]
    ran_z = [Operator(S, each).s_x()**2 for each in M]

    print("___\t{}".format(M))
    print("S_x\t{}".format(ran_x))
    print("S_y\t{}".format(ran_y))
    print("S_z\t{}".format(ran_z))

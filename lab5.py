from math import sin, pi

from matplotlib import pyplot as plt

Umax = 100

f = 50

R1, R2, R3, R4 = 5, 4, 7, 2

L1, L2, L3 = 0.01, 0.02, 0.015

C1, C2, C3 = 0.0003, 0.00015, 0.0002

t_int = 0.2

h = 0.00001

U1 = lambda t: Umax * sin(2 * pi * f * t)




F = [

    lambda x, t: -U1(t) + x[0]*R1 + x[0]*R2 - (x[0]*(R2 - R3) - x[1])/(R2 - R3)*R2 + x[0]*R3 - (x[0]*(R2 - R3) - x[1])/(R2 - R3)*R3/L1,

    lambda x, t: x[0]/C1,

]

X = [0, 0]

t = 0

res = []

times = [h * i for i in range(int(t_int / h))]

temp = [0, 0]

while t < t_int:

    res.append((temp[0]-(temp[0]*(R2 - R3) - temp[1])/(R2 - R3))*R3)

    for i in range(2):

        temp = []

        for i in range(len(X)):
            temp.append(X[i] + h * F[i](X, t))

        for i in range(len(X)):
            X[i] += h * F[i](temp, t)

    t += h


if __name__ == '__main__':
    print(X)
    plt.plot(times, res)
    plt.ylabel('U2')
    plt.xlabel('t')
    plt.show()
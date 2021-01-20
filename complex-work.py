from matplotlib import pyplot as plt


def gauss(A=None):
    n = len(A)
    det = 1
    V = []
    C = []
    for column in range(0, n):
        V.append([])
        C.append([])

    for i in range(0, n):
        for j in range(0, n):
            V[i].append(A[i][j])

    for i in range(0, n):
        for j in range(0, n):
            if j > i:
                C[i].append(0)
            else:
                C[i].append(A[i][j])

    for k in range(0, n):
        max = abs(V[k][k])
        w = k
        for l in range(k+1, n):
            if max < abs(V[l][k]):
                max = abs(V[l][k])
                w = l
        for d in range(0, n):
            value = V[k][d]
            V[k][d] = V[w][d]
            V[w][d] = value
        det = det * pow((-1), w) * V[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                C[k][j] = V[k][j] / V[k][k]
                V[i][j] = V[i][j] - V[i][k] * C[k][j]

    return det


def U1(t):
    T = 4 * a
    while t > T:
        t -= T
    if t < a:
        U1 = t * 10 / a
    elif t < 2 * a:
        U1 = -(t * 10 / a) + 20
    else:
        U1 = 0
    return U1

def L1(i1):
    if abs(i1) <= i_min:
        return L_max
    if abs(i1) >= i_max:
        return L_min
    A = [
        [1, i_min, i_min ** 2, i_min ** 3],
        [1, i_max, i_max ** 2, i_max ** 3],
        [0, 1, 2 * i_min, 3 * i_min ** 2],
        [0, 1, 2 * i_max, 3 * i_max ** 2]
    ]
    B = [L_max, L_min, 0, 0]
    a = gauss(A, B)

    return a[0] + a[1] * abs(i1) + a[2] * i1 ** 2 + a[3] * abs(i1 ** 3)


if __name__ == '__main__':

    C1 = 0.048
    C2 = 0.016
    R1, R2, R3, R4 = 8, 3, 170, 13
    L_max = 74
    L_min = 7.4
    i_min = 1
    i_max = 2

    a = 0.05
    t_int = 2
    h = 0.00025


    F = [
        lambda X, U, t: X[1] / C1,
        lambda X, U, t: (U - X[0] - X[1] * R1 - (((X[1] * R4) + X[2])*R3 / ( R3 + R4))) / L1(X[1]),
        lambda X, U, t: (((X[1] * R3 * R4) - X[2] * (R2 + R3 + R4)) / R2 * ( R3 + R4)* C2)
    ]

    t = 0.000025
    X = [0, 0, 0]
    U = []
    U2 = []
    UC1 = []
    i1 = []
    UC2 = []
    times = []

    for i in range(int(t_int / h)):
        times.append(h * i)

    while t < t_int:
        U.append(U1(t))
        U2.append((((X[1] * R3) - X[2]) / (R2 + R3 + R4)) * R4)
        UC1.append(X[0])
        i1.append(X[1])
        UC2.append(X[2])

        for i in range(len(X)):
            K1 = h * F[i](X, U[-1], t)
            K2 = h * F[i]([x + 0.5 * h for x in X], U[-1] + 0.5 * K1, t)
            K3 = h * F[i]([x + 0.5 * h for x in X], U[-1] - (0.5 - 1/(2**0.5)) * K1 + (1 - 1/(2**0.5)) * K2, t)
            K4 = h * F[i]([x + h for x in X], U[-1] - (1/(2**0.5))*K2 + (1 + 1/(2**0.5)) * K3, t)
            X[i] = X[i] + (K1 + (2 - (2**0.5))*K2 + (2 + (2 ** 0.5)) * K3 + K4) / 6
        t += h

    print(X)
    print('U2 = ' + str(X[2]))

    plt.figure(1)
    plt.plot(times, U)
    plt.xlabel('t')
    plt.ylabel('U1')

    plt.figure(2)
    plt.plot(times, U2)
    plt.xlabel('t')
    plt.ylabel('U2')

    plt.figure(3)
    plt.plot(times, UC1)
    plt.xlabel('t')
    plt.ylabel('UC1')

    plt.figure(4)
    plt.plot(times, UC2)
    plt.xlabel('t')
    plt.ylabel('UC2')

    plt.figure(5)
    plt.plot(times, i1)
    plt.xlabel('t')
    plt.ylabel('i1')

    plt.show()





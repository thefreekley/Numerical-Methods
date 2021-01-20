import numpy as np




def _rectangle_rule(func, a, b, nseg, frac):
    dx = 1.0 * (b - a) / nseg
    sum = 0.0
    xstart = a + frac * dx
    for i in range(nseg):
        sum += func(xstart + i * dx)

    return sum * dx

def right_rectangle_rule(func, a, b, nseg):
    return _rectangle_rule(func, a, b,nseg, 1.0)



def func(x):
    return x*(2**(2*x))


def F(x):
    return (x * (2 ** (2 * x))) / (2 * np.log(x)) - (2 ** (2 * x)) / (2 * ((np.log(2)) ** 2))




if __name__ == '__main__':

    a = 0.8
    b = 2

    print("right rectangle: " + str(right_rectangle_rule(func,a,b,30)))
    print("newton leibniz: " + str(F(b)-F(a)))


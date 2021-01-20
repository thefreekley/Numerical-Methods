import math
a,b=-2.5,0
h=0.000001
find_k=0
iteration_k=0

def f(x):
    return x**2 - math.cos(x)

def F(x):
    return  2*x + math.sin(x)


b=a+h
fa=f(a)
fb=f(b)
x=a
if abs(fb)>abs(fa) and fa*fb>0:
    h=(-1)*h
b=a+h
fb=f(b)

while fa*fb>0:
    a=b
    b=a+h
    fa=f(a)
    fb=f(b)
    find_k+=1


x=a

while True:
    e = 0
    x_old=x
    fa=f(a)
    fb=f(b)
    x=a-fa*((b-a)/(fb-fa))
    fx=f(x)
    if fx*fa>0:
        a=x
    else: b=x
    if(abs((x-x_old)/x)*100 > e):
        e=abs((x-x_old)/x)*100
    iteration_k+=1

    if e<0.00000001:
        print(f"x={x}\n"
              f"F(x)={f(x)}\n"
              f"Iteration process: {iteration_k}\n"
              f"Site search localization:{find_k}")
        break



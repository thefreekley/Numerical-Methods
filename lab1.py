k_=15
p_=22
B_=0.02*p_
s_=0.02*k_


B=[30.24,(40.95-B_),42.81]

A=[[(24.21+s_),2.42,3.85],
   [2.31,31.49,1.52],
   [3.49,4.84,(28.72+s_)]]
n=len(A)
P,Y,V,X=[0]*n,[0]*n,([[0] * n for i in range(n)]),[0]*n
k=0

for i in range(n):
   for j in range(n):
       if i!=j:
           V[i][j]=-(A[i][j]/A[i][i])
       else:
           V[i][j]=0
   P[i] = B[i] / A[i][i]
   Y[i] = B[i]


while True:
    e = 0
    for i in range(n):
        S=0
        for j in range(n):
            S=S+V[i][j]*Y[j]
        X[i]=P[i]+S
    for i in range(n):
        if((abs((X[i]-Y[i])/Y[i]))*100>e):
            e=(abs((X[i]-Y[i])/Y[i]))*100
        Y[i]=X[i]

    k+=1
    if e<0.000001 or k>1000:
        for i in range(n):
            print("X"+str(i)+" = "+ str(X[i]))
        print("Iterations = " + str(k))
        print("E = " + str(e))
        break








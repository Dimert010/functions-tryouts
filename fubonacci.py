def fibo(n):
    A = 0
    B = 1
    
    if 'n' == 1:
        print(A)
    
    else:
        print(A)
        print(B)
 
    for o in range(2, n):
        C = A + B
        A = B
        B = C
        print(C)

fibo(144)


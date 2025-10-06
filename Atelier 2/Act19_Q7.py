def F7(n):
    if n==1 :
        return 1
    if n == 0 :
        return 0
    return F7(n-1)+F7(n-2)
n = int(input("donner le nombre a utilitser dans la suite de fibonacci : "))
print(f"la suite de fibonacci de {n} est {F7(n)}")
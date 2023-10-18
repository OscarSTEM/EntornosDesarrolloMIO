#Funcion 
def abcde(a,b,c,d,e):
    s = a+b+c+d+e
    t = s/5
    return t
def abcd(a,b,c,d):
    s = a+b+c+d
    t = s/4
    return t
def abc(a,b,c):
    s = a+b+c
    t = s/3
    return t
def ab(a,b):
    s = a+b
    t = s/2
    return t   
# Codigo Principal
x = int(input())
if x==1:
    a = int(input())
    print(1)
elif x==2:
    a = int(input())
    b = int(input())
    print(ab(a,b))
elif x==3:
    a = int(input())
    b = int(input())
    c = int(input())
    print(abc(a,b,c))
elif x==4:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(abcd(a,b,c,d))
elif x==5:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(abcde(a,b,c,d,e))
else:
    print("no")

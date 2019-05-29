def f():
    return 42

def f1(x):
    return x * 2

def f2(x,y):
    return x - y

def f3(a,b,c):
    a = a + b
    a = a - c
    return -a

def f4(a,b,c,d):
    return a*b + c*d

def f5(a,b,c,d,e):
    x = a + 1
    y = b + 2
    z = c + 3
    aa = d + 4
    bb = e + 5
    cc = f4(x,x,y,y)
    dd = f3(cc, z, aa)
    ee = f2(bb, cc)
    return dd + ee

x = f()
y = f1(x)
print f5(0, x, y, x+y, 0)

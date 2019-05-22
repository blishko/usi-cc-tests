x = [True, 1, {}, []]
print x
y = {1 : 2, False : 1}
print y
z = [1, [1, 2], [[[1]]]]
print z
x[1] = z if x[0] and x[1] else z[2][0]
print x
# comment
print x[0] and x[1]
if not x[1] or x[2]:
    print y[False]
else:
    print y[1]
a = y[1]
while a != 0:
    x[a] = 1
    a = a - 1
print x


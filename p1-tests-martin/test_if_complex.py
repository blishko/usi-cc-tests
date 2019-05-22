x = [42,42,42]
y = input()
print y
if y == x[1] and input() or y == x[0]:
    z = input()
    print z
    print x
    if y != z:
        x[1] = z
    else:
        x[0] = y + 1
    print x
else:
    x[2] = {1 : y}
    print x

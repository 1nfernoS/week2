x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1+y1)%2 != 0 or (x2+y2)%2 != 0:
    print('NO')
elif x2-x1 < y2-y1:
    print('NO')
else:
    print('YES')

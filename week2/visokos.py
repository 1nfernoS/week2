i = int(input())
if i%400 == 0 or (i%4 == 0 and not i%100 == 0):
    print('YES')
else:
    print('NO')

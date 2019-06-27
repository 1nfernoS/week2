a = int(input())
b = int(input())
c = int(input())
ch = False
nech = False
if a%2 == 0 or b%2 == 0 or c%2 == 0:
    ch = True
if a%2 == 1 or b%2 == 1 or c%2 == 1:
    nech = True
if ch and nech:
    print('YES')
else:
    print('NO')

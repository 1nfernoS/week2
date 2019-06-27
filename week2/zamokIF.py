a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
if (a<=d and b<=e) or (b<=d and a<=e) or (a<=d and c<=e) or (c<=d and a<=e) or (b<=d and c<=e) or (c<=d and b<=e):
    print('YES')
else:
    print('NO')

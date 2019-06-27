a = int(input())
b = int(input())
c = int(input())
g = max(a,b,c)
k1 = min(a,b,c)
k2 = a+b+c-k1-g
if k1+k2 <= g:
    print('impossible')
elif k1**2 + k2**2 == g**2:
    print('rectangular')
elif k1**2 + k2**2 < g**2:
    print('acute')
else:
    print('obtuse')

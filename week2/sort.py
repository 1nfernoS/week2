a, b, c = int(input()), int(input()), int(input())
if a > b:
    b += a
    a = b - a
    b -= a
if b > c:
    c += b
    b = c - b
    c -= b
if a > c:
    c += a
    a = c - a
    c -= a
if a > b:
    b += a
    a = b - a
    b -= a
print(a,b,c)

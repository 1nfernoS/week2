a1, b1, c1, a2, b2, c2 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
ab1 = max(a1,b1,c1)
cb1 = min(a1,b1,c1)
bb1 = a1+b1+c1-ab1-cb1
ab2 = max(a2,b2,c2)
cb2 = min(a2,b2,c2)
bb2 = a2+b2+c2-ab2-cb2
if ab1==ab2 and bb1==bb2 and cb1==cb2:
    print('Boxes are equal')
elif ab1>=ab2 and bb1>=bb2 and cb1>=cb2:
    print('The first box is larger than the second one')
elif ab1<=ab2 and bb1<=bb2 and cb1<=cb2:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')

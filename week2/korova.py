i = int(input())
if i%10 == 1 and i//10!=1:
    print(i, 'korova')
elif i%10<5 and i//10!=1 and i%10!=0:
    print(i, 'korovy')
else:
    print(i, 'korov')

a=int(input('enter 1^st no: '))
b=int(input('enter the 2^nd no:'))
c=int(input('enter the 3^rd no:'))
if a>b and a>c:
    print('greatest no:',a)
elif b>a and b>c:
    print('greatest no:',b)
else:
    print('greatest no:',c)
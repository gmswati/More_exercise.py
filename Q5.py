num=int(input('enter a Positive no:'))
if num>0:
    product=1
    i=num
    while i>0:
        product*=i
        i-=1
    print('Factorial=',product)

# l=list('swati')
# print(l)

def is_harsad_number(x):

    x_digits = list(str(x))
    # print(x_digits)
    sum=0
    for digit in x_digits:
        sum+=int(digit)
    if x%sum==0:
        print(x,'is a harsad no.')
    else:
        print(x,'is not a harsad no.')
is_harsad_number(int(input('enter the no:\n')))

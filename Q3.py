from cgitb import strong


password=input('enter the password:')
if len(password)>=6 and  len(password)<=16:
    if '$' in password:
        if '2' in password or '8' in password:
            if ('A' or 'Z') in password:
                print('your password is strong!')
            else:
                print('weak pwd')
        else:
            print('weak pwd')
    else:
        print('weak pwd')
else:
    print('weak pwd')
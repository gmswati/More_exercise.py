def encrypt():
  message = input("Enter the message you want to encrypt: \n")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(encrypt_message))


def decrypt():
  message = input("Enter the message you want to decrypt: \n")
  ascii_message = [ord(char)-3 for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))

flag = True
while flag:
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!: \n").lower()
    if choice == 'e':
        encrypt()
    elif choice == 'd':
        decrypt()
# else
    play_again = input("Do you want to try agian or Do you want to exit? (Y/N) : ").lower()
    if play_again == 'y':
      continue
    elif play_again == 'n':
      print('okay!Bye.\nHave a good day.')
      flag=False
      # break

# Bug is fixed now...,good job :)
      
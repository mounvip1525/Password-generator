import readable,unreadable
import random

print('Hey! This program used for generating random passwords')
while(1):
    choice=int(input("\n Choose \n 1. Unreadable password \n 2. Readable password \n 3. 4-digit OTP: \n 4. Exit \n"))
    if(choice==1):
        print("Your password: ",unreadable.unreadable())
    elif(choice==2):
       print("Your password: ",readable.readable())
    elif(choice==3):
        print("Your OTP: ", random.randint(1000,9999))
    else:
        print('Bye!')
        exit()
    
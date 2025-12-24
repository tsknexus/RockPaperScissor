import random

random = random.randint(1,3)

Num = int(input("Enter the number of rounds: "))


lista = ['''                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  ''' , '''    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/''', '''       _
               _  / |
              / \ | | /\
               \ \| |/ /
                \ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
         jgs    |     |''']



roundss = 1

while(roundss <= Num ):
    print(''' 1-Rock 2-Paper 3-Scissor''')

    user = int(input("Enter the number :"))

    if(user<=3 and user>=1):
        if(user == random ):
           
            print(f"user:\n{lista[user-1]} \n Computer:\n{lista[random-1]}")

            roundss +=1
            print(".........Draw...........")

        elif(user == 1 and random == 3):
            print(f"user:\n{lista[user-1]} \n Computer:\n{lista[random-1]}")
            roundss +=1
            print("Computer Won")

        
        elif(user == 2 and random == 3):
            print(f"user:\n{lista[user-1]} \n Computer:\n{lista[random-1]}")
            roundss +=1
            print("User Won")

            
        elif(user == 3 and random == 2):
            print(f"user:\n{lista[user-1]} \n Computer:\n{lista[random-1]}")
            roundss +=1
            print("User Won")

        
        elif(user == 1 and random == 2):
            print(f"user:\n{lista[user-1]} \n Computer:\n{lista[random-1]}")
            roundss +=1
            print("User Won")

        
        elif(user == 3 and random == 1):
            print(f"user:\n{lista[user-1]} \n Computer:\n{lista[random-1]}")
            roundss +=1
            print("User Won")

        
        elif(user == 2 and random == 1):
            print(f"user:\n{lista[user-1]} \n Computer:\n{lista[random-1]}")
            roundss +=1
            print("User Won")

        
        else:
            print("There is a Confution")
    else:
        print("Enter the Correct Number")    

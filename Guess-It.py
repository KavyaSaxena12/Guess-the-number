import random
x=random.randint(0,100)
count=0
while(True):
    if count is 10:
        print("GAME OVER!!!!!")
        print("The number was",x)
        break
    num =int(input("Enter a number"))
    if num == x:
        print("You have guessed the number")
        break
    elif num > x:
        count=count+1
        print("Go a bit Low\n",count,"chance taken")
        continue
    elif num < x:
        count=count+1
        print("Go a bit higher\n",count,"chance")
        continue

        
    


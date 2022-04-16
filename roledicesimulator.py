import random

from pyparsing import counted_array
sami=0
point=0
counter=0


while True:
    print("hey the target is 50 point and you have 10 changes DO OR DIE")
    sam=int(input("same press 1 to roll the dice"))
    if sam==1:
        randome=random.randint(1,6)
        print(randome)
        point=point+randome
        print(f"you point is {point}")
        counter=counter+1
        if  point>50:
         print("congrats! you win the target point of today")
         exit()


        if counter>20:
         print("Changes are over you die")
         exit()

    


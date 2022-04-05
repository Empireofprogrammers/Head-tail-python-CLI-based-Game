import random
name = str(input("Who will take head your name:- "))
name2 = str(input("Who will take tail your name:- "))
head_or_tail = random.randint(0,1)
if head_or_tail == 1:
    print(name,"you won it's Head")
elif head_or_tail == 0:
    print(name2,"You won it's tail")

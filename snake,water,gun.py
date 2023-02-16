import random

def check(comp,user):
  if(comp==user):
    return 0
  
  if(comp==0 and user==1):
    return -1
  if(comp==1 and user==2):
    return -1
  if(comp==2 and user==0):
    return -1
    
  return 1


name=input("enter your name:")
print(f"Welcome to our snake,water,gun game Mr/Ms{name} lets start playing our beautiful game")
comp=random.randint(0 ,2)
user=int(input("0 for snake,1 for Water and 2 for Gun:\n"))




score=check(comp,user)

print("You",user)
print("computer",comp)


if(score==0):
  print(f"sorry {name} it a draw")
elif(score== -1):
  print(f"its a loose {name}")
else:
  print(f"You won {name}")

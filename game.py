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
        

comp=random.randint(0,2)
user=int(input("Enter 0 for snake 1 for water and 2 for gun:"))

print("You ",user)
print("computer ",comp)

score=check(comp,user)
if(score==0):
    print("its a draw")
if(score==-1):
    print("You looose")
elif(score==1):
    print("You won")


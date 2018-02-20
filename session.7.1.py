import random
a=["rock","paper","scissor"]
comp=random.choice(a)
print("Rock paper Scissors")
user=input("enter ur choice")

print("user turn is",user)
print("comp turn is",comp)
v= user.lower()
if v=="rock" or "paper" or "scissor":
    if v==comp:
        print("tie")
    elif (v=="rock"):
        if(comp=="paper"):
            print("comp wins")
        else:
            print("user wins")
    elif (v=="paper"):
        if(comp=="scissor"):
            print("comp wins")
        else:
            print("user wins")
    elif(v=="scissor"):
        if(comp=="rock"):
            print("comp wins")
        else:
            print("user wins")
           
   

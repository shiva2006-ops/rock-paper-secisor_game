import random
a= 1
win = 0
loss = 0
draw = 0
print("let's play best of three") 
print("enter r for rock, p for paper and s for scissor")     
while(a<=3):
    computer =random.choice([1,0,-1])
    
    you= input("enter your choise : ")
    yourdict = {"r":1,"p":0,"s":-1}
    rivdict = {1:"rock",0:"paper",-1:"sessior"}
    comnum=rivdict[computer]
    youchoose = yourdict[you]
    younum=rivdict[youchoose]
    print("you choose :",younum)
    print("computer choose : ",comnum)
    if (youchoose-computer==2 or youchoose-computer==-1 or youchoose-computer==1):
        win+=1
        print("you win ")
    elif(computer==youchoose):
        draw+=1
        print("draw")
    else:
        loss+=1
        print("you loss")
    a+=1
print("your points:---","win",win,"loss",loss,"draw",draw)   
if(win>=2):
    print("you are the winner")
elif(draw==3):
    print("it's a draw")
    # if (youchoose==1 and computer==0):               #1
    #     print("you loss")
    # elif (youchoose==1 and computer==-1):         #2
    #     print("you win")
    # elif (youchoose==0 and computer==-1):         #1
    #     print("you loss")
    # elif( youchoose==0 and computer==1):          #-1
    #     print("you win")
    # elif( youchoose==-1 and computer==1):          #-2
    #     print("you loss")
    # elif( youchoose==-1 and computer==0):          #-1
    #     print("you win")
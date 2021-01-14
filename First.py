import random
cout,coutp=0,0
print("**sank water gun game**")
list=['snak','water','gun']
i=0
while(i<4):
    i+=1
    x=random.choice(list)
    y=input("Enter the choice")
    print(x)
    if x==y:
        print("tie")
    elif x=='snak' and y=='water':
        cout=cout+1
                    #print("you loss")
    elif x=='water'  and y == 'gun':
        cout = cout+1
                   # print("you loss")
    elif x=='gun' and y=='snak':
        cout = cout + 1
                  #  print("you loss")
    else:
        coutp+=1



print("Number try PC: ",cout)
print("Number try player : ",coutp)

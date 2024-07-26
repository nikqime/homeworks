balance=input("Enter your balance here: ")

if balance>1000:
    print("okey, do u want to withdraw some?")
    qs_1=input("yes/no")
    if qs_1=="yes":
        an_1=input("how much: ")
        if an_1>=balance:
            print("ok")
    elif qs_1=="no":
        print("ok")
elif balance<=0:
    print("you can not withdraw")
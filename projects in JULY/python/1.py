balance=0
def creating_acc():
    questionN1 = input("For whom do you want to create an account? (child) / (student) / (18+ person): ")
    if questionN1 == "child":
        print("Creating account for child.")
        print("show personal number or pasport")
        qs_1=input("u can show something from this? (yes/no)")
        if qs_1=="yes":
            print("choose what u want to do now")
            choice=("deposit / withdraw / show-personal-info / LOG OUT / piggy bank")                                #dasamtavrebelia amis gagrdzeleba
        else:
            print("sorry but we can not create account without this")

    elif questionN1 == "student":
        print("Creating account for student.")
        print("show personal number or pasport")
        qs_1=input("u can show something from this? (yes/no)")
        if qs_1=="yes":
            print("choose what u want to do now")
            choice=("deposit / withdraw / show-personal-info / LOG OUT / piggy bank")
        else:
            print("sorry but we can not create account without this")

    elif questionN1 == "18+ person":
        print("Creating account for 18+ person.")
        print("show personal number or pasport")
        qs_1=input("u can show something from this? (yes/no)")
        if qs_1=="yes":
            print("choose what u want to do now")
            choice=("deposit / withdraw / show-personal-info / LOG OUT / piggy bank")
        else:
            print("sorry but we can not create account without this")

    else:
        print("Invalid option selected. Please try again.")
def log_in():
    Email = input("Enter your email here: ")
    password = input("Enter your password here: ")
    
    if not Email.endswith("@gmail.com"):
        return False
    
    if len(password) < 8:
        return False
#selector
print("choose what u want to do now")
choice=("deposit / withdraw / show-personal-info / LOG OUT / piggy bank")    
    
    
def deposit():
    global balance

    balance=0
    balance_remember=(f"I remind you that your balance is {balance}$")
    qs_dep=input("how much u want to deposit? (0-1M)")
    card_info=input("can u enter card inro if we ask? (yes/no)")
    if card_info=="yes":
        balance+=qs_dep
    else:
        print("we can not deposit because u can not say card details. sorry")
    
def withdraw():
    global balance
    

    print (f"your balance is {balance}$")
    print(f'you can withdraw maximum {balance}$')
    withdraw_question_1=input("how much you want to withdraw?: ")
    if withdraw_question_1<=balance:
        print("you sucsesfully withdrawed ")
    elif withdraw_question_1>balance:






















 



question0 = input("Do you want to create a bank account? (yes/no): ")
if question0.lower() == "no":
    creating_acc()
elif question.lower()=="yes":
    
else:
    print("No account will be created.")
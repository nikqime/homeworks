def i_v_m(email):
    return email.endswith("@gmail.com")
def i_v_p(password):
    return len(password) >= 8 

def reg():
    email=input("Enter your Gmail address: ")
    password=input("enter password: ")

    if i_v_m(email) and i_v_p(password):
        print("ok")
    else:
        if not i_v_m(email): 
            print("error")
if __name__=="__main__":
    reg()
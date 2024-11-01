def aguri(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

#aguri(5)

def guli(n):
    for i in range(n // 2, n, 2):
        print(" " * (n - i - 1) + "*" * i + " " * (n - i - 1) + "*" * i)
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

guli(6)

def jvari(n):
    for i in range(n):
        if i == n // 2:
            print("*" * n)
        else:
            print(" " * (n // 2) + "*")

jvari(7)

def yvavi():
    print("   ♣   ")
    print("  ♣♣♣  ")
    print(" ♣♣♣♣♣ ")
    print("   ♣   ")
    print("   ♣   ")

yvavi()



print("bratuxia varketilshi xar da amoirchie swori pasuxi an aqve gagipent mteli ubani")
choose=input("amoirchie brat-----aguri----guli----jvari----yvavi--:   ")
if choose=="aguri":
    aguri(5)
    print("arasworia amoatriale jibeebi")
elif choose=="jvari":
    jvari(5)
    print("arasworia amoatriale jibeebi")
elif choose=="guli":
    guli(6)
    print("arasworia amoatriale jibeebi")
elif choose=="yvavi":
    yvavi()
    print("GILOCAV BRATUXIA")
else:
    print("arasworia amoatriale jibeebi")









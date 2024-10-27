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
        if i == n // 2:  # ჰორიზონტალური ხაზი
            print("*" * n)
        else:  # ვერტიკალური ხაზი
            print(" " * (n // 2) + "*")

jvari(7)

def yvavi():
    print("   ♣   ")
    print("  ♣♣♣  ")
    print(" ♣♣♣♣♣ ")
    print("   ♣   ")
    print("   ♣   ")

yvavi()



print("bratuxia varketilshi xar dzma da amoirchie swori pasuxi an aqve gagipent mteli ubani brat")
choose=input("amoirchie brat-----aguri----guli----jvari----yvavi--:   ")
if choose=="aguri":
    aguri(5)
    print("arasworia brat amoatriale jibeebi an dagerxeva")
elif choose=="jvari":
    jvari(5)
    print("arasworia brat amoatriale jibeebi an dagerxeva")
elif choose=="guli":
    guli(6)
    print("arasworia brat amoatriale jibeebi an dagerxeva")
elif choose=="yvavi":
    yvavi()
    print("GILOCAV BRATUXIA SAXES AR DAGALEWAVT")










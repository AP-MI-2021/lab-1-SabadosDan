def prim(x):
    '''
    verifica daca x este prim
    :param x: nr. natural
    :return: True/False
    '''
    if x<2:
        return False
    for i in range (2,x//2+1):
        if x % i == 0:
            return False
    return True
assert prim(5)==True
assert prim(1)==False
assert prim(4)==False
def produsNnumere(lst):
    '''
    calculeaza si returneaza produsul celor n elemente din lista lst
    :param lst: lista de numere naturale
    :return: p
    '''
    p=1
    for i in range(n):
        p=p*lst[i]
    return p
def cmmdc1(a,b):
    '''
    calculeaza cmmdc prin scaderi repetate
    :param a: 
    :param b: 
    :return: b
    '''
    while a != b :
        if a>b:
            a=a-b
        else:
            b=b-a
    return b
def cmmdc2(a,b):
    '''
    calculeaza cmmdc prin impartiri repetate
    :param a: nr. natural
    :param b: nr. natural
    :return: a
    '''
    while b!=0:
        r=a%b
        a=b
        b=r
    return a


stop=False
while stop!=True:
    print(" -Alege optiunea 1 pentru a verifica daca un numar este prim")
    print(" -Alege optiunea 2 pentru a calcula produsul a n numere citite de la tastatura")
    print(" -Alege optiunea 3 pentru a calcula cel mai mare divizor comun dintre 2 numere citite de la tastatura")
    print(" -Alege optiunea x pentru a iesi din program")
    optiune=input("    Alege optiunea:  ")
    if optiune=="1":
        n = int(input("Introdu numarul:  "))
        if prim(n)==True:
            print(" DA, ",n," este prim.")
        if prim(n)==False:
            print(" NU, ",n," nu este prim.")
    elif optiune=="2":
        lst=[]
        n = int(input("Introdu n:  "))
        print("   Introdu numerele:")
        for i in range(n):
            x=int(input())
            lst.append(x)
        print("Produsul celor n numere este ", produsNnumere(lst))
    elif optiune=="3":
        print("  Metoda 1: scaderi repetate")
        print("  Metoda 2: impartiri repatate")
        metoda=int(input("     Alege metoda prin care sa se afle cmmdc-ul celor 2 numere:  "))
        if metoda==1:
            a=int(input("Primul numar: "))
            b=int(input("Al doilea numar: "))
            print("CMMDC dintre ", a," si ", b," este ", cmmdc1(a,b))
        elif metoda==2:
            a = int(input("Primul numar: "))
            b = int(input("Al doilea numar: "))
            print("CMMDC dintre ", a, " si ", b, " este ", cmmdc2(a, b))
        else:
            print(" *Ai introdus o metoda gresita! Te rog sa o iei de la inceput.")
    elif optiune=="x":
        stop=True
    else:
        print("Nu exista aceasta optiune!!! Te rog sa introduci una din cele precizate mai sus.")
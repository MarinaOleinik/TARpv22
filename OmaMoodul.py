from datetime import date, datetime
#13/02/23
def Kustuta(i:list,p:list,):
    kesk_palk=sum(p)/len(p)
    print(kesk_palk)
    v=int(input("Kellel palk 1- on suurem,2-on väiksem?"))
    if v==1:
        for palk in p:
            if palk>kesk_palk:
                ind=p.index(palk)
                print(ind)
                p.remove(palk)
                i.pop(ind)
    else:
        pass
    return i,p



#8/02/23
def Lisa_andmed(i:list,p:list):
    """Kirjeldus....
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    n=int(input("Mitu inimest:"))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p
def Kustutamine(i:list,p:list):
    """Kirjeldus....
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi: ")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)

    return i,p
def Suurim_palk(i:list,p:list):
    """Kirjeldus....
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    # ise kirjutada, kui mitu palka
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]

    return palk,nimi

def Sorteerimine(i:list,p:list):
    """Kirjeldus....kirjuta ise!!!
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    v=int(input("palk 1-kahaneb,2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi

    return i,p
def Vordsed_palgad(i:list,p:list):
    """Kirjeldus....kirjuta ise!!!
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid)) #[1200,2500,750,750,1200]->[1200,750]
    for palk in dublikatid: 
        n=p.count(palk) #1200, n=2; 750, n=2
        k=-1 #-----
        print(f"{palk} saavad kätte järgmised inimesed:")
        for j in range(n):            
            k=p.index(palk,k+1)#-----
            nimi=i[k]
            print(nimi)


#6/02/23

def pikkus(ikood:str)->bool:
    """Funktsioon tagastab True, kui pikkus on 11 sümbolid
    :param str ikood: Inimese isikukood
    :rtype: bool
    """
    if len(ikood)==11:
        flag=True
    else:
        flag=False
    return flag

def sugu(ikood:str)->str:
    """Kui esimene täht on [1,2,3,4,5,6], siis määrame sugu
    :param str ikood: Isikukood
    :rtype: str
    """
    ikood_list=list(map(int,ikood)) #[1,2, ...]
    if ikood_list[0] in [1,3,5]:
        s="mees"
    elif ikood_list[0] in [2,4,6]:
        s="naine"
    else:
        s="viga"
    return s
def sunnipaev(ikood:str)->str:
    ikood_list=list(map(int,ikood)) 
    y=str(ikood_list[1])+str(ikood_list[2])
    m=str(ikood_list[3])+str(ikood_list[4])
    d=str(ikood_list[5])+str(ikood_list[6])
    if (int(m)>0 and int(m)<13) and (int(d)>0 and int(d)<32):
        if ikood_list[0] in [1,2]:
            yy="18"
        elif ikood_list[0] in [3,4]:
            yy="19"
        else:
            yy="20"
        spaev=d+"."+m+"."+yy+y
    else:
        spaev="viga"
    return spaev

def sunnikoht(ikood: str)->str:
    ikood_list=list(ikood)
    tahed_8910=ikood_list[7]+ikood_list[8]+ikood_list[9]
    t=int(tahed_8910)
    if 1<t<10:
        haigla="Kuressaare Haigla"
    elif 11<t<19:
        haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21<t<220:
        haigla=" Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221<t<270:
        haigla=" Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    else:
        haigla="Välismaal"
    return haigla

def lause(ikood: str)->str:
    print(f"See on {sugu(ikood)} ta on sündinud {sunnipaev(ikood)}, tema sünnikoht on {sunnikoht(ikood)}")

def kontrollnr(ikood:str)->int:
    astme1=[1,2,3,4,5,6,7,8,9,1]
    astme2=[3,4,5,6,7,8,9,1,2,3]
    ik_list=list(ikood)
    ik_list=list(map(int,ik_list))
    summa=0
    for i in range(0,10,1):
        summa+=ik_list[i]*astme1[i]
    s=(summa//11)*11
    jaak=summa-s
    if jaak==int(ik_list[10]):
        return jaak
    elif jaak==10:
        return 0
    else:
        summa=0
        for i in range(0,10,1):
            summa+=ik_list[i]*astme2[i]
        s=(summa//11)*11
        jaak=summa-s
        return jaak

def naised_mehed(ikoodid:list)->list:
    naised=[]
    mehed=[]
    for kood in ikoodid:
        kood_=list(kood)
        if int(kood_[0])%2==0:
            naised.append(kood)
        else:
            mehed.append(kood)
    naised.extend(mehed)
    ikoodid=naised
    return ikoodid

def arvud_sorted(arvud:list)->list:
    arvud=list(map(int,arvud)) #[111,3333,2222,3444,222,7]
    arvud.sort()
    return arvud
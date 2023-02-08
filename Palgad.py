from OmaMoodul import *
palgad=[1200,2500,750,750,1200]
inimesed=["A","B","C","D","A"]
while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n1-Lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Min palk kellel\n5-Sort\n6-Võrdsed palkad kellel on\n"))
    if menu==0:
        break
    elif menu==1:
        inimesed,palgad=Lisa_andmed(inimesed,palgad)
    elif menu==2:
        inimesed,palgad=Kustutamine(inimesed,palgad)
    elif menu==3:
        palk,nimi=Suurim_palk(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}´l")
    elif menu==5:
        inimesed,palgad=Sorteerimine(inimesed,palgad)
    elif menu==6:
        Vordsed_palgad(inimesed,palgad)
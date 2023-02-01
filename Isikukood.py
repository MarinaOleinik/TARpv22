from xmlrpc.client import DateTime
from OmaMoodul import *
ikood=""
while True:
    ikood=input("Sisesta isikukood: ")
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
    else:
        s=sugu(ikood)
        if s=="viga":
            print("Esimene täht ei ole õige")
        else:
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on valesti sisestatud")
            else:
                lause(ikood)

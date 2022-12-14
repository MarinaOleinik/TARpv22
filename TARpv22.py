from math import * # * - kõik funktsioonid moodulist 
from random import *
#14/12/22
#Ülesanne "Ema roobot". 
#Ema küsib "Mis hinde sa koolis said?", laps vastab ja ootab ema reaktsioon
print("Ema roobot")
a=input("Sisesta: ")
print(a.isalpha(), a.isdigit())
if a.isdigit() and int(a)>0 and int(a)<=5:
    a=int(a)
    if a==5:
        pass
    elif a==4:
        pass
    elif a==3:
        pass
    elif a==2 or a==1:
        pass

else:
    print("Sa valesti vastas")

#import math      math.funktsioon()
#12/12/22
#1.
print("Puu läbimõõdu arvutamine")
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
try:
    C=float(input("Anna ümbermõõt: "))
    if C>0:
        d=round(C/pi,2)
        print(f"Puu läbimõõt = {d}")
    else:
        print("C peab olema suurem kui 0")
except:
    print("Andmetüüp on vale")

#2.
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
try:
    N=float(input("Sisesta N: "))
    M=float(input("Sisesta M: "))
    if M>0 and N>0:
        d=round(sqrt(N**2+M**2),2)
        print(f"Ristkülikukujulise maatüki diagonaal on {d}")
except:
    print("M ja N vaja sisestada float formaadis")
#3
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus/aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")

#4
print("Aritmeetiline keskmine")
A1=int(input("Esimene arv: "))
A2=int(input("Teine arv: "))
A3=int(input("Kolmas arv: "))
A4=int(input("Neljas arv: "))
A5=int(input("Viies arv: "))
K=(A1+A2+A3+A4+A5)/5
print(f"Kesknime on {K}")

#5
print("Joonista samasugune konn")
print("    @..@")
print("   (----)") 
print("  ( \__/ )")
print("^^ "'""'" ^^")  

#6
a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
P=a+b+c
print(f"Ümbermõõt on {P}")

#7
P=randint(1,6)
summa=(12.9*1.1)/P
print(f"{P}-st, Igaüks maksab {summa} ")

#8
print("Kütusekulu arvutamine")
l=float(input("Kütuse liitride kogus: "))
km=float(input("Läbitud kilomeetrid: "))
kulu=(l/km)*100
print(f"Kütusekulu {kulu}")

#9
print("Rulluisutajad")
M=int(input("Minutid:"))
M=M/60
tee=M*29.9
print(f"Jõuab {tee} km")

#10
print("Ajateisendus")
M=int(input("Sisesta aja minutites")) #1h=60min
H=M//60 #h
M=M%60  #min
print(f"{H}:{M}")




# 08/12/2022

print("Tere tulemast!") # info ekraanile, väljundlause
nimi=input("Mis sinu nimi on? ") #Sisend lugemine jaoks input()->str
print() #tühi rida
print(f"{nimi}, sul on väga ilus nimi!")
print(nimi,", sul on väga ilus nimi!") #,->tühik
print(nimi+", sul on väga ilus nimi!") # str+str 
vanus=int(input("Kui vana sa oled? ")) # int(str)
print(nimi,"sa oled",vanus,"aastat vana")
vanus+=10
print(nimi+", 10 aasta pärast sa oled"+str(vanus)+"aastat vana")
print()
print("Võrdse pindalaga ristkülik ja ring")
a=float(input("Anna laius: "))
b=float(input("Anna kõkgus: "))
S=a*b #-,+,**,/,//,%
P=2*a+2*b
d=round(sqrt(a**2+b**2),2) #ümardamine 2 numbrit koma pärast
print(f"Pindala = {S}\nLäbimõõt = {P}\nDiagonaal = {d}")
print("Ringi raadius ")

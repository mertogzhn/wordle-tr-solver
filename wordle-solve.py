from tkinter.filedialog import Open
import enDegerliKelimeler as deger
import json

def start():
    with open("Dogru-Yerde-Harfler.txt","w",encoding="utf-8") as f:
        f.close()
    with open("Olan-Harfler.txt","w",encoding="utf-8") as f:
        f.close() 
    with open("Yanlis-Harfler.txt","w",encoding="utf-8") as f:
        f.close()
    with open("besharf.txt","r",encoding="utf-8") as f:
        icerik=f.read()
        f.close()
    with open("besharfHafiza.txt","w",encoding="utf-8") as fh:
        fh.write(icerik)
        fh.close()

def cozum():
    girdi=input("girdiniz ne oldu: ")
    print("Doğru yerdekiler için *\nYanlış yerdekiler için +\nOlmayanlar için -")
    sira=0
    for i in girdi:
        donus=input(f"{i} harfi geri dönüsü: ")
        if donus=="*":
            with open("Dogru-Yerde-Harfler.txt","a",encoding="utf-8") as f:
                f.write(f"{i},{str(sira)}\n")
                f.close()
        elif donus=="+":
            with open("Olan-Harfler.txt","a",encoding="utf-8") as f:
                f.write(f"{i},{str(sira)}\n")
                f.close() 
        else:
            with open("Yanlis-Harfler.txt","a",encoding="utf-8") as f:
                f.write(f"{i}\n")
                f.close()
        sira+=1
    sira=0
    with open("Yanlis-Harfler.txt","r",encoding="utf-8") as f:
        icerik=f.readlines()


    sozluk=besHarfliler()
    for i in range(len(icerik)):
        silinecekler=[]
        for j in sozluk:
            if icerik[i][0] in j:
                silinecekler.append(sozluk.index(j))
        silinecekler.reverse()
        #print(silinecekler)
        for j in silinecekler:
            sozluk.pop(j)

    with open("besharfHafiza.txt","w",encoding="utf-8") as fh:
        for i in range(len(sozluk)):
            fh.write(sozluk[i])

    #yanlisYerler()

    dogruYerler()

def besHarfliler():            
    with open("besharfHafiza.txt","r",encoding="utf-8") as f:
        kelimeler = f.readlines()
        f.close()
    return kelimeler

def yanlisYerler():
    with open("Olan-Harfler.txt","r",encoding="utf-8") as f:
        yerler=f.readlines()

    sozluk=besHarfliler()
    for i in range(len(yerler)):
        silinecekler=[]
        for j in sozluk:
            if yerler[i][0]==j[i]:
                silinecekler.append(sozluk.index(j))
        if silinecekler!=[]:
            silinecekler.reverse()
        #print(silinecekler)
            for j in silinecekler:
                sozluk.pop(j)
    
    with open("besharfHafiza.txt","w",encoding="utf-8") as fh:
        for i in range(len(sozluk)):
            fh.write(sozluk[i])

def dogruYerler():
    with open("Dogru-Yerde-Harfler.txt","r",encoding="utf-8") as f:
        yerler=f.readlines()

    sozluk=besHarfliler()
    for i in range(len(yerler)):
        silinecekler=[]
        for j in sozluk:
            if yerler[i][0]!=j[i]:
                silinecekler.append(sozluk.index(j))
        if silinecekler!=[]:
            silinecekler.reverse()
        #print(silinecekler)
            for j in silinecekler:
                sozluk.pop(j)
    
    with open("besharfHafiza.txt","w",encoding="utf-8") as fh:
        for i in range(len(sozluk)):
            fh.write(sozluk[i])
      
start()
print('HOŞ GELDİNİZ'.center(50,'*'))
while True:
    print("Senin için en değerli kelimeleri buldum")
    deger.degerli()
    cozum()

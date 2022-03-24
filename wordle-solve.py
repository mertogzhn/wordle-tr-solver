from re import M
import enDegerliKelimeler as deger
def start():
    with open("Dogru-Yerde-Harfler.txt","w",encoding="utf-8") as f:
        f.close()
    with open("Olan-Harfler.txt","w",encoding="utf-8") as f:
        f.close() 
    with open("Yanlis-Harfler.txt","w",encoding="utf-8") as f:
        f.close()

def cozum():
    girdi=input("girdiniz ne oldu: ")
    print("Doğru yerdekiler için *\nYanlış yerdekiler için +\nOlmayanlar için -")

    for i in girdi:
        donus=input(f"{i} harfi geri dönüsü: ")
        if donus=="*":
            with open("Dogru-Yerde-Harfler.txt","a",encoding="utf-8") as f:
                f.write(f"{i}\n")
                f.close()
        elif donus=="+":
            with open("Olan-Harfler.txt","a",encoding="utf-8") as f:
                f.write(f"{i}\n")
                f.close() 
        else:
            with open("Yanlis-Harfler.txt","a",encoding="utf-8") as f:
                f.write(f"{i}\n")
                f.close()

    with open("Yanlis-Harfler.txt","r",encoding="utf-8") as f:
        icerik=f.readlines()

    print(icerik[0])

def besHarfliler():            
    with open("besharf.txt","r",encoding="utf-8") as f:
        kelimeler = f.readlines()
        f.close()
    return kelimeler

      
start()
print('HOŞ GELDİNİZ'.center(50,'*'))
print("Senin için en değerli kelimeleri buldum")
deger.degerli()
cozum()
#pri

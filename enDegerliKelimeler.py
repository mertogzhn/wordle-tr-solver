#dosya açılır ve kelimeler listesitene atanır
def degerli():
    with open("besharfHafiza.txt","r",encoding="utf-8") as f:
        kelimeler = f.readlines()
        f.close()

    harfTekrari={'a': 3527, 'b': 635, 'c': 381, 'ç': 514, 'd': 640, 'e': 2324, 'f': 402, 'g': 417, 'ğ': 156, 'h': 550, 'i': 1967, 'ı': 868, 'j': 51, 'k': 1801, 'l': 1422, 'm': 1331, 'n': 1229, 'o': 779, 'ö': 267, 'p': 488, 'r': 1540, 's': 1130, 'ş': 538, 't': 1253, 'u': 946, 'ü': 682, 'v': 404, 'y': 661, 'z': 659}

    kelimeSayisi=len(kelimeler)
    puanListesi=[]
    for i in range(kelimeSayisi):
        kelime=[]
        puan=0
        for harf in kelimeler[i]:
            if harf!="\n" and kelime.count(harf)==0 and harf!=" ":
                puan+=harfTekrari[f"{harf}"]
                kelime.append(harf)
        
        puanListesi.append(puan)

    #print(puanListesi)

    enDeğerliler=[]

    for i in range(10):
        degerli=[]
        degerli.append(kelimeler[puanListesi.index(max(puanListesi))])
        degerli.append(puanListesi.index(max(puanListesi)))

        enDeğerliler.append(degerli)
        kelimeler.pop(puanListesi.index(max(puanListesi)))
        puanListesi.pop(puanListesi.index(max(puanListesi)))

    print(enDeğerliler)

degerli()
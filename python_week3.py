import statistics
import random
import numpy as np

#Soru 1 – Liste Metotları
notlar = [85, 92, 76, 92, 100, 76, 85, 92]
tekrar = []
maks = notlar[0]
mini = notlar[0]
for i in notlar:
    if i not in tekrar:
        tekrar.append(i)
print(tekrar)
for n in notlar:
    if n > maks:
        maks = n
    if n < mini:
        mini = n
print("En yüksek not:",maks)
print("En düşük not:",mini)

#Soru 2 – Sayılar
sayi = int(input("Bir sayı girin:"))
birler = sayi % 10
onlar = (sayi // 10) % 10
yuzler = (sayi // 100) % 10
total = (birler**3 + onlar**3 + yuzler**3)
def armstrong(sayi):
    if total == sayi:
        print(sayi, "bir Armstrong sayısıdır.")
    else:
        print(sayi, "bir Armstrong sayısı değildir.")
armstrong(sayi)

#Soru 3 – Kümeler
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}
A.intersection(B)
A.difference(B)
birlesim = A.union(B)
sirala = sorted(birlesim)
print(sirala)

#Soru 4 – Modüller
sayilar = []
for i in range(10):
    sayilar.append(random.randint(0, 100))
print(sayilar)
ortalama = statistics.mean(sayilar)
stdsapma = statistics.stdev(sayilar)
print("Ortalama:", ortalama)
print("Standart Sapma:", stdsapma)

#Soru 5 – Fonksiyonlar
#"Yapay zeka düşünür, düşünür, düşünür… İnsan hayal eder, hayal eder, hayal eder. Gelecek, hayal ve düşüncenin birleşiminde şekillenir."
metin = (input("Size ilham veren bir sözü yazınız."))
metinliste = metin.split()
metinlist = []
encokgecen = max(metinliste, key=metinliste.count)
def kelime_sayac(metin):
    maxlen = metinliste[0]
    for m in metinliste:
        metinlist.append(m)
    print("Toplam kelime sayısı:", len(metinlist))
    for l in metinliste:
        if len(l) > len(maxlen):
            maxlen = l
    print("Metindeki en uzun kelime:", maxlen)
print("Metinde en çok geçen kelime:",encokgecen)
kelime_sayac(metin)

#Soru 6 – Gömülü Fonksiyonlar

numbers = [5, 12, 7, 18, 24, 3, 16]
numbers_kare = []
sira = sorted(numbers_kare, reverse = True)
even = list(filter(lambda e: e % 2 == 0, numbers))
print("Çift sayılar:",even)
for i in numbers:
    i = i**2
    numbers_kare.append(i)
print("Elemanların kareleri",numbers_kare)
print("Azalan sıraya göre:",sira)

#Soru 7 – Lambda İfadeleri
kelimeler = ["veri", "bilim", "analiz", "yapayzeka", "python"]
uzunluk = sorted(kelimeler, key=lambda x: len(x))
print(uzunluk)

#Soru 8 – Metodlar
girdi = (input("Girdi yapınız."))
def sayitoplam(girdi):
    total = 0
    for i in girdi:
        if i.isdigit():
            total += int(i)
    return total
sayitoplam(girdi)

#Soru 9 – (Ekstra) Numpy 1
arr = np.random.randint(0,51,10)
print(arr)
ort = np.mean(arr)
stddev = np.std(arr)
enbuyuk = np.max(arr)
print("Dizinin ortalaması:",ort)
print("Dizinin standart sapması:",stddev)
print("En büyük değer:",enbuyuk)

#Soru 10 – (Ekstra) Numpy 2
mtrs = np.random.rand(5,5)
print(mtrs)
ort1 = np.mean(mtrs,axis = 0)
print("Sütunların ortalaması:",ort1)
binmatris = (mtrs > 0.5).astype(int)
print("Oluşan yeni matris:\n",binmatris)
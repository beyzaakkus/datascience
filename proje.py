import statistics
import random
#Proje – “Kitap Satış Analiz Sistemi”
kitaplar = [
{"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
{"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil":
2020},
{"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
{"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
{"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
{"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500,
"yil": 2021},
{"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

#1. Fonksiyon Yazma:
def yazar_satislari(kitaplar):
    dict1 = {}
    for ktp in kitaplar:
        yazar = ktp["yazar"]
        satis = ktp["satis"]
        if yazar in dict1:
            dict1[yazar] += satis
        else:
            dict1[yazar] = satis
    return dict1
yazar_satislari(kitaplar)

def en_cok_satan(kitaplar):
    encok = kitaplar[0]
    for i in kitaplar:
        if i["satis"] > encok["satis"]:
            encok = i
    return encok
en_cok_satan(kitaplar)

#2. Liste ve Küme İşlemleri:

turler = {i["tur"] for i in kitaplar}
print(turler)

list1000 = []
for i in kitaplar:
    isim = i["isim"]
    if i["satis"] > 1000:
        list1000.append(isim)
print(list1000)

#3. Lambda / Filter / Map Kullanımı:

cikis = list(filter(lambda k:k["yil"] > 2020, kitaplar))
print("2020'den sonra çıkanlar:",cikis)
guncelsatis = list(map(lambda k:k["satis"]*1.10, kitaplar))
print("Güncel satış adetleri:",guncelsatis)
stis = list(sorted(kitaplar, key=lambda k:k["satis"], reverse = True))
print("Satış adetlerinin azalan şekilde sıralanışı:",stis)

#4. İstatistiksel Analiz:

satisliste = []
for i in kitaplar:
    satis = i["satis"]
    satisliste.append(satis)
print(satisliste)
ortalamasatis = sum(satisliste) / len(satisliste)
print("Ortalama Satış:",ortalamasatis)

ortalamas = sum(i["satis"] for i in kitaplar) / len(kitaplar)
print("Ortalama satış:", ortalamas)

makstur = kitaplar[0]
dict5 ={}
for i in kitaplar:
    tur = i["tur"]
    satis = i["satis"]
    if i["satis"] > makstur["satis"]:
        makstur = i
    if tur in dict5:
        dict5[tur] += satis
    else:
        dict5[tur] = satis
en_cok_tur = max(dict5, key=dict5.get)
print("Türlere göre satış adetleri:",dict5)
print("Toplamda en çok satış yapılan tür:",en_cok_tur)
print("Tekil olarak en çok satış adedi:",makstur)
print("Tekil olarak en çok satış yapılan tür:",makstur["tur"])
stdevsatis = statistics.stdev(satisliste)
#satısliste = [1200, 950, 700, 1800, 400, 1500, 600]
print("Satışların standart sapması:",stdevsatis)

#5. Ekstra (Zorlayıcı): Train/Test Simülasyonu

testdata = int(0.3 * len(kitaplar))
test = random.sample(kitaplar, testdata)
egitim = [x for x in kitaplar if x not in test]
print("Test Seti:", test)
print("Eğitim Seti:", egitim)

ortsatis = sum(s["satis"] for s in egitim) / len(egitim)
print("Eğitim verisindeki ortalama satış miktarı:",ortsatis)
ortsatistest = sum(s["satis"] for s in test) / len(test)
print("Test verisindeki ortalama satış miktarı:",ortsatistest)

testsatis = []
for t in test:
    if t["satis"] > ortsatis: #ortsatıs = 1210
        testsatis.append(t)

if testsatis:
    print("Eğitim verisindeki ortalama satışın üstünde satışlar:", testsatis)
else:
    print("Test verisinde, Eğitim verisindeki ortalama satış miktarının üstünde satış bulunmamaktadır.")

#Test verisi, eğitim verisinin satış ortalamasının çok altında satışlara sahip. Test setinin eğitim seti dağılımına benzer olması modelin doğru yorumlanması için türlerin dengeli dağılması gerekir.
#Bilim türündeki kitaplar eğitim setinde baskın ve yüksek satış sağlıyor. Bilim veya akademik türdeki kitaplar test verisine eklenebilir.

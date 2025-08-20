#Veri Tipleri ve Operatörler

#Bölüm 1.1
isim = input("ADINIZ ve SOYADINIZ: ")
print("Merhaba", isim)
yas = int(input("YAŞINIZ: "))
print(yas)
boy = float(input("BOYUNUZ: "))
print("Boyunuz", boy, "cm'dir.")

#Bölüm 1.2
mat = 90
kimya = 55
fizik = 73
ort = (mat + kimya + fizik) / 3
print(float(ort))

#Bölüm 1.3
word = "veribilimi"
len(word)
word[0]
word[9]
ters = word[::-1]

#Bölüm 2.4
num1 = int(input("1.sayıyı giriniz: "))
num2 = int(input("2.sayıyı giriniz: "))
toplam = num1 + num2
cikarma = num1 - num2
carpim = num1 * num2
bolum = num1 / num2
mod = num1 % num2
print("TOPLAM", toplam)
print("ÇIKARMA", cikarma)
print("ÇARPIM", carpim)
print("BÖLÜM", bolum)
print("MOD", mod)

#Bölüm 2.5
not1 = int(input("1.notu giriniz: "))
not2 = int(input("2.notu giriniz: "))
ort = (not1 + not2) / 2

if ort < 50:
    print("Maalesef" , float(ort) , "ortalama ile dersten kaldınız.")
else:
    print("Tebrikler!" , float(ort) , "ortalama ile dersten geçtiniz.")

#Bölüm 2.6
yas = int(input("Yaşınızı giriniz:"))
if yas >= 18:
    print("Yaşınız ehliyet almak için uygundur.")
else:
    print("Yaşınız ehliyet almak için uygun değildir.")

#Bölüm 2.7
fiyat = float(input("Ürünün fiyatını giriniz: "))
indirim = float(input("İndirim oranını giriniz (%): "))
yenifiyat = fiyat - (fiyat * (indirim/100))
print("İndirimli fiyat:",yenifiyat)

#Bölüm 2.8
odev_check = input("Ödevini bitirdin mi? (evet/hayır): ").lower() == "evet"
odev_yukleme_check = input("Ödevini sisteme yükledin mi? (evet/hayır): ").lower() == "evet"
if not odev_check and not odev_yukleme_check:
    print("Lütfen ödevini yapıp sisteme yükle.")
elif odev_check and not odev_yukleme_check:
    print("Ödevi bitirmişsin ama sisteme yüklememişsin.")
elif not odev_check and odev_yukleme_check:
    print("Sisteme yüklemişsin ama ödev bitmemiş görünüyor, kontrol et.")
else:
    print("Her şey tamam, yapman gereken başka bir şey yok!")

#Bölüm 3.9
fiyat1 = int(input("1. ürünün fiyatını giriniz: "))
fiyat2 = int(input("2. ürünün fiyatını giriniz: "))
fiyat3 = int(input("3. ürünün fiyatını giriniz: "))
toplam = fiyat1 + fiyat2 + fiyat3
if toplam > 200:
    print("Ara toplam=" , toplam - (toplam*0.1))
else:
    print("Ara toplam=", toplam)

#Bölüm 3.10
dogumyil = int(input("Doğum yılınızı giriniz:"))
yas = 2025 - dogumyil
if 0 < yas < 12:
    print("Çocuksunuz.")
elif 13 < yas < 17:
    print("Ergensiniz.")
else:
    print("Yetişkinsiniz.")



#Soru 1 – Sayı Analizi

syi = int(input(" Bir sayı giriniz: "))
if syi < 0 :
    sonuc = "negatif"
elif syi == 0:
    sonuc = "sıfır"
else:
    sonuc = "pozitif"

if syi % 2 == 0:
    snc = "çift"
else:
    snc = "tek"
print(snc, sonuc)

# Soru 2 – Harf Frekansı (String)

sozcuk = str(input(" Bir kelime giriniz: "))
dict = {}
for i in sozcuk:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
print(dict)

#Soru 3 – Şifre Kontrolü (String Metotları)

sifre = input(" Şifrenizi oluşturun: ")
if not any(s.isupper() for s in sifre):
    print("Şifreniz en az 1 büyük harf içermelidir.")
elif not any(s.isdigit() for s in sifre):
    print("Şifreniz en az 1 rakam içermelidir.")
elif len(sifre) < 8:
    print("Şifreniz en az 8 karakter uzunluğunda olmalıdır.")
else:
    print("Şifreniz başarılı şekilde oluşturulmuştur.")

#Soru 4 – Liste İşlemleri

list1 = [12, 4, 9, 25, 30, 7, 18]
list2 = []
total = sum(list1)
ortalama = total / len(list1)
for i in list1:
    if i > ortalama:
        list2.append(i)
print("Ortalama:",int(ortalama))
print("Ortalamadan büyük elemanların oluşturduğu liste:",list2)

#Soru 5 – Nested Loop (Desen)

for i in range (1,10):
    for j in range(i):
        print("*", end = "")
    print()

#Soru 6 – While Döngüsü

list4 = []
while True :
    number = int(input(" Bir sayı giriniz: "))
    if number == 0:
        break
    list4.append(number)
listtotal = sum(list4)
listortalama = listtotal / len(list4)

print("Oluşan liste:",list4)
print("Toplam:",listtotal)
print("Ortalama:",listortalama)

#Soru 7 – Palindrom Kontrolü

girdi = input(" Kelime girin: ")
if girdi == girdi[::-1]:
    print("Palindromdur.")
else:
    print("Palindrom değildir.")

#Soru 8 – List Comprehension

lst = [i**2 for i in range(1,100) if i % 3 == 0 and i % 5 == 0]
print(lst)

#Soru 9 – String İşlemleri

sentence = "techcareer.net ile veri bilimi yaz kampı"
splittedsentence = sentence.split()
upperfirstletter = [i.capitalize() for i in splittedsentence]
newsentence = " ".join(upperfirstletter)
print(newsentence)

#Mini Proje – Film Yorumu Analizi

sayac = 5
commentlist = []
commentlen = []

for s in range(sayac):
    comment = input("Yorumunuzu yazın:")
    commentlist.append(comment)

maxlen = commentlist[0]
minlen = commentlist[0]
wordsayi = sum("iyi" in word.lower() for word in commentlist)


for i in commentlist:
    commentlen.append(len(i))
    if len(i) > len(maxlen):
        maxlen = i
    if len(i) < len(minlen):
        minlen = i

allcommentlen = sum(commentlen)
ortallcommentlen = allcommentlen / len(commentlen)


print("---------------------------------------")
print("Tüm Yorumlar:",commentlist)
print("---------------------------------------")
print("Toplam yorum sayısı:",len(commentlist))
print("word:",wordsayi)
print("Herbir yorumun karakter sayısı:",commentlen)
print("Ortalama uzunluk:", ortallcommentlen,"karakter")
print("En uzun yorum:", maxlen)
print("En kısa yorum:", minlen)



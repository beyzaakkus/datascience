import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1.	1. Numpy ile Matris İşlemleri

#5x5 boyutunda rastgele (0-100 arasında) tam sayılardan oluşan bir matris oluşturun.
matris = np.random.randint(0,100, (5,5))
print(matris)

#Ortalama, standart sapma ve varyansını hesaplayın.
ortalama = np.mean(matris)
matris.mean()

stdsapma = np.std(matris)
matris.std()

varyans = np.var(matris)
matris.var()

#En büyük ve en küçük değerlerini bulun.
maxi = np.max(matris)
matris.max()
mini = np.min(matris)

#Köşegenindeki elemanların toplamını bulun.
total = np.diag(matris).sum()

print("Matrisin Ortalaması:",ortalama)
print("Matrisin Standart Sapması:",stdsapma)
print("Matrisin Varyansı:",varyans)
print("Matrisin En Büyük Elemanı:",maxi)
print("Matrisin En Küçük Elemanı:",mini)
print("Köşegen toplamı",total)

#2.	2. Numpy ile Veri Simülasyonu

notlar = np.random.normal(50,5,1000).astype(int)
ort = np.mean(notlar)
med = np.median(notlar)
st = np.std(notlar)
dusuknot = np.sum(notlar < 50).tolist()
print("Notların Ortalaması:", ort)
print("Medyan:",med)
print("Standart Sapma:",st)
print("Ortalama altında kalan öğrenci sayısı:",dusuknot)

#2. Pandas Bölümü

grade = pd.read_excel("GRADES.xlsx")
print(grade)

#Her ders için ortalama puanı bulun.
matort = grade["Matematik"].mean()
fzkort = grade  ["Fizik"].mean()
kmyort = grade["Kimya"].mean()
print("Matematik dersi için ortalama puan:",matort)
print("Fizik dersi için ortalama puan:",fzkort)
print("Kimya dersi için ortalama puan:",kmyort)

#En yüksek matematik notunu alan öğrenciyi bulun.
matmax = grade.loc[grade["Matematik"].idxmax(), "Öğrenci"]
print("Matematik en yüksek puan alan öğrenci:",matmax)

#Her öğrencinin not ortalamasını hesaplayan yeni bir sütun ekleyin.
grade["Genel Ortalama"] = grade[["Matematik", "Fizik", "Kimya"]].mean(axis=1)
print(grade)

#Bölümlere göre gruplayarak her bölümün ortalama başarılarını hesaplayın.
bolmat = grade.groupby("Bölüm")["Matematik"].mean()
bolfzk = grade.groupby("Bölüm")["Fizik"].mean()
bolkmy = grade.groupby("Bölüm")["Kimya"].mean()
print("Bölümlere göre Matematik dersindeki ortalama başarı puanı:",bolmat)
print("----------------------")
print("Bölümlere göre Fizik dersindeki ortalama başarı puanı:",bolfzk)
print("----------------------")
print("Bölümlere göre Kimya dersindeki ortalama başarı puanı:",bolkmy)

#Ortalaması 70’in üzerinde olan öğrencileri filtreleyin.
basarili_ogrenciler = grade[grade["Genel Ortalama"] > 70]
print("Genel ortalaması 70 üzeri olan öğrenciler:\n",basarili_ogrenciler)

#Her dersin dağılımının histogram ile gösterilişi

dersler = ["Matematik", "Fizik", "Kimya"]
for i, ders in enumerate(dersler):
    plt.subplot(1, 3, i+1)
    sns.histplot(grade[ders])
    plt.title(f"{ders} Not Dağılımı")
    plt.xlabel("Not")
    plt.ylabel("Öğrenci Sayısı")
plt.show()


plt.subplot(1, 3, 1)
sns.histplot(grade["Matematik"])
plt.title("Matematik Not Dağılımı")
plt.xlabel("Not")
plt.ylabel("Öğrenci Sayısı")
plt.show()

plt.subplot(1, 3, 2)
sns.histplot(grade["Fizik"])
plt.title("Fizik Not Dağılımı")
plt.xlabel("Not")
plt.ylabel("Öğrenci Sayısı")
plt.show()

plt.subplot(1, 3, 3)
sns.histplot(grade["Kimya"])
plt.title("Kimya Not Dağılımı")
plt.xlabel("Not")
plt.ylabel("Öğrenci Sayısı")
plt.show()

#Bölümlere göre ortalamaların bar grafikte görselleştirilmesi

bolum_ortalama = grade.groupby("Bölüm")["Genel Ortalama"].mean().reset_index()
sns.barplot(data=bolum_ortalama, x="Bölüm", y="Genel Ortalama")
plt.title("Bölümlere Göre Ortalama")
plt.ylabel("Ortalama")
plt.xlabel("Bölümler")
plt.show()
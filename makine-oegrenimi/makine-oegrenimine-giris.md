---
description: Çok hevesle yaklaşılan makine öğreniminin ne olduğuna basitçe bir yaklaşım.
---

# 🔰 Makine Öğrenimine Giriş

## 👀 Kavramlara Göz Atalım

* Öğrenmeyi, daha önceki tecrübelerimizden yola çıkarak, yeni olaylar için öngörüde bulunmak olarak nitelendirebiliriz
  * Örneğin otobüse her seferinde geç kalma durumunda, biraz daha erken çıkmamız gerektiğini öğrenebiliriz
* Genelde insanların öğrenme hususunda makinelerden daha hızlı olduğu söylense de, makineler çok yüksek miktardaki verileri daha iyi öğrenirler
  * Bu veriler `csv` dosyaları veya resimler olabilir

## 🎯 Makine Öğreniminin Amacı

* Daha önceden sahip olduğumuz verileri analiz etme ve anlama
* Bu anlayışı kullanarak anlamsız verileri mantıksal olarak anlamlandırma
* Örnek olarak "Kedi resimlerini öğrenip, kedileri bulan bir model" verilebilir

{% hint style="warning" %}
Verilerin aynı dağıtımdan olması gerektiğini unutmayalım. Kedileri öğretip, köpekleri bulması beklenilemez.
{% endhint %}

## 💪 Makine Öğreniminin Gücü

Makine öğreniminin gücü iki temel sebebe dayanır

* Günümüzde, çok yüksek miktarda üretilen verilere
* Gelişen bilgisayar teknolojisi işlem gücünün artmasına

## 🌟 Makine Öğrenimi Uygulamalarına Örnekler

### 📈 Grafiksel Bir Örnek

Soldaki tablo verilerinden oluşan bir seti makineye öğrettiğimizde:

* Sağdaki yeşil çizgi makinenin öngördüğü sınırdır
  * Bu sınırın altında kalanlar Kedi, üstünde kalanlar Köpek olarak nitelendirilebilir
* Sağdaki kırmızı çizgi ise gerçek sınır çizgisini temsil eder

![](../.gitbook/assets/image%20%2840%29.png)

{% hint style="info" %}
Bu öğrenme yönetimi **Lineer Regression** olarak adlandırılmaktadır.
{% endhint %}

### 🚢 Online Bir Örnek

Alttaki uygulama verilen tablodaki verileri öğrenen bir modelin çalışmasına örnektir

![](../.gitbook/assets/image%20%2825%29.png)

![](../.gitbook/assets/image%20%285%29.png)

## 🌌 Makine Öğrenimi Öğrenme Tipleri

| Supervised | Unsupervised |
| :--- | :--- |
| Daha önceden anlamlandırılmış verileri öğrenme | Anlamlandırılmamış verilerden anlam ve benzerlik bulma |
| Fotoğrafların kedi olduğu bilinir | Fotoğrafların ne olduğu bilinmez |
| Temel amacı öğrenmektir | Temel amacı gruplamaktır |
| Öğrendiği verilerin ne olduğunu bilir | Verilerin ne olduğunu bilmez sadece benzer olanları gruplar |

{% hint style="info" %}
Bizim odaklanacağımız teknik **Supervised Learning** tekniğidir.
{% endhint %}

### 👨‍🏫 Supervised Learning

Temel amaç, verilen $$X$$ ile istenen $$Y$$verisini bulmaktır.

$$f(x) \approx y$$

* $$X$$, **feature matrix** olarak adlandırılan özellik matrisi
* $$Y$$, **labels** olarak adlandırılan x'in anlamlandırılmış halidir

## 🐞 Makine Öğrenimindeki Sıkıntılar

Makine öğrenimi sonucunda oluşan modeller verileri genelleştirmede yeteri kadar başarılı olmayabilmekte

* Sadece verilen bilgilerden öğrendikleri için sınırlı tahminler yapabilmekteler
* Ayrıca verilen bilgileri aşırı öğrenmeleri \(**over-fitting**\) durumunda genelleştirmede zayıf kalmaktadır

![](../.gitbook/assets/image%20%282%29.png)

## 🔗 Harici Bağlantılar

* [📜 Intro to Machine Learning](https://github.com/yedhrab/YArtificalIntelligent/tree/71a0ba6331737b9e2a8bbf80ccd5ed08f5e1564a/0.2%20-%20Machine%20Learninig%20Notebooks/1%20-%20Eğitici%20Notebooklar/0%20-%20Intro%20to%20Machine%20Learning.ipynb)
* [📺 WQU ML lecture 01](https://www.youtube.com/watch?v=9J6FNvil6Gw&feature=youtu.be)
* [📊 WQU Data Science](https://wqu.org/programs/data-science)


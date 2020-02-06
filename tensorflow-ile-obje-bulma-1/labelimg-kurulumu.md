# 💷 LabelImg Kurulumu

## 🔰 Temel Bilgiler

* LabelImg tensorflow modelleri için etiketleme amaçlı kullanılmaktadır
* Derlenmiş sürümünü indirmek için [buraya](http://tzutalin.github.io/labelImg/) tıklayabilirsin
* Derlenmiş sürümü çalışmazsa alttaki yönerge ile derleyebilirsin

{% hint style="info" %}
İndirilen dosyayı `%TENSORFLOW%\addons` dizinine atmanız daha verimli bir çalışma sağlayacaktır.
{% endhint %}

## 🌆 Sanal Ortam Oluşturma

Tensorflow ortamının alt paketlerini etkilememesi için ek bir sanal ortamda kurulum sağlamalıyız.

```text
conda create -n labelImg pyqt # QT grafik kütüphanesiconda activate labelImgconda install -c anaconda lxml
```

## 📦 Paketlerini Kurma ve Derleme

Paketlerin kurulumu için alttaki talimatları sırayla uygulayın:

* LabelImg dosyalarını indirmek için [buraya](https://github.com/tzutalin/labelImg/archive/master.zip) tıklayın
* Diğer işlemler için indirdiğiniz dosya dizininde cmd açıp alttaki komutları yazın

```text
# labelImg-master.zip dizinindepowershell.exe Expand-Archive labelImg-master.zip .ren labelImg-master labelImgmkdir %TENSORFLOW%\addonsmove labelImg %TENSORFLOW%\addonscd %TENSORFLOW%\addons\labelImgpyrcc5 -o resources.py resources.qrc # QT grafiklerinin oluşturulması
```

{% hint style="warning" %}
_'pyrcc5' is not recognized as an internal or external command_ hatası gelirse, yüklediğiniz `pyqt` sürümüne göre komutu kullanın \(`pyrcc<pyqt_sürümü_ilk_basamağı>`\)
{% endhint %}

## ✅ Kurulumu Test Etme

```text
conda activate tensorflow-cpucd %TENSORFLOW%\addons\labelImgpython labelImg.py# python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```


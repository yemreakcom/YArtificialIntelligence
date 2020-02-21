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

```bash
conda create -n labelImg pyqt # QT grafik kütüphanesi
conda activate labelImg
conda install -c anaconda lxml
```

## 📦 Paketlerini Kurma ve Derleme

Paketlerin kurulumu için alttaki talimatları sırayla uygulayın:

* LabelImg dosyalarını indirmek için [buraya](https://github.com/tzutalin/labelImg/archive/master.zip) tıklayın
* Diğer işlemler için indirdiğiniz dosya dizininde cmd açıp alttaki komutları yazın

{% tabs %}
{% tab title="✴️ Windows" %}

```bash
# labelImg-master.zip dizininde
powershell.exe Expand-Archive labelImg-master.zip .
ren labelImg-master labelImg
mkdir %TENSORFLOW%\addons
move labelImg %TENSORFLOW%\addons
cd %TENSORFLOW%\addons\labelImg
pyrcc5 -o resources.py resources.qrc # QT grafiklerinin oluşturulması
```

{% endtab %}

{% tab title="🐧 Linux" %}

🙄

{% endtab %}
{% endtabs %}



{% hint style="warning" %}
_'pyrcc5' is not recognized as an internal or external command_ hatası gelirse, yüklediğiniz `pyqt` sürümüne göre komutu kullanın \(`pyrcc<pyqt_sürümü_ilk_basamağı>`\)
{% endhint %}

## ✅ Kurulumu Test Etme

{% tabs %}
{% tab title="✴️ Windows" %}

```bash
conda activate tensorflow-cpu
cd %USERPROFILE%\Tensorflow\addons\labelImg
python labelImg.py
# python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

{% endtab %}

{% tab title="🐧 Linux" %}

```bash
conda activate tensorflow-cpu
cd %USERPROFILE%/Tensorflow/addons/labelImg
python labelImg.py
# python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

{% endtab %}
{% endtabs %}



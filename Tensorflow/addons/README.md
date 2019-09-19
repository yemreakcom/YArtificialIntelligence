# Addons <!-- omit in toc -->

Burada LabelImg ve benzeri yardımcı programların dosyaları bulunur.

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Temel Yapı](#temel-yap%C4%B1)
- [LabelImg Kurulumu](#labelimg-kurulumu)
  - [Derlenmiş LabelImg Kurulumu](#derlenmi%C5%9F-labelimg-kurulumu)
  - [Kaynak Kodları ile LabelImg Kurulumu](#kaynak-kodlar%C4%B1-ile-labelimg-kurulumu)
    - [LabelImg için Sanal Ortam Oluşturma](#labelimg-i%C3%A7in-sanal-ortam-olu%C5%9Fturma)
    - [LabelImg Paketlerini Kurma ve Derleme](#labelimg-paketlerini-kurma-ve-derleme)
    - [LabelImg Kurulumunu Test Etme](#labelimg-kurulumunu-test-etme)

## Temel Yapı

```sh
+ addons
    + labelimg
    ...
```

## LabelImg Kurulumu

LabelImg tensorflow modelleri için etiketleme amaçlı kullanılmaktadır

### Derlenmiş LabelImg Kurulumu

Derlenmiş sürümünü indirmek için [buraya](http://tzutalin.github.io/labelImg/) tıklayabilirsin

### Kaynak Kodları ile LabelImg Kurulumu

Sadece derlenmiş sürümlerde uyumsuzluk söz konusu olduğunda bu kısma bakmanız tavsiye edilir.

#### LabelImg için Sanal Ortam Oluşturma

Tensorflow ortamının alt paketlerini etkilememsi için ek bir sanal ortamda kurulum sağlamalıyız.

```sh
conda create -n labelImg pyqt # QT grafik kütüphanesi
conda activate labelImg
conda install -c anaconda lxml
```

#### LabelImg Paketlerini Kurma ve Derleme

Paketlerin kurulumu için alttaki talimatları sırayla uygulayın:

- LabelImg dosyalarını indirmek için [buraya](https://github.com/tzutalin/labelImg/archive/master.zip) tıklayın
- Diğer işlemler için indirdiğiniz dosya dizininde cmd açıp alttaki komutları yazın

```sh
# labelImg-master.zip dizininde
powershell.exe Expand-Archive labelImg-master.zip .
ren labelImg-master labelImg
mkdir %USERPROFILE%\Tensorflow\addons
move labelImg %USERPROFILE%\Tensorflow\addons
cd %USERPROFILE%\Tensorflow\addons\labelImg
pyrcc5 -o resources.py resources.qrc # QT grafiklerinin oluşturulması
```

> *'pyrcc5' is not recognized as an internal or external command* hatası gelirse, yüklediğiniz `pyqt` sürümüne göre komutu kullanın (`pyrcc<pyqt_sürümü_ilk_basamağı>`)

#### LabelImg Kurulumunu Test Etme

```sh
conda activate tensorflow-cpu
cd %USERPROFILE%\Tensorflow\addons\labelImg
python labelImg.py
# python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```
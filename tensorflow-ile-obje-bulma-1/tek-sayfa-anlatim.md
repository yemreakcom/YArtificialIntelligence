---
description: >-
  Tensorflow Object Detection API ile Obje Bulma ve kullanımı için gerekli
  talimatlarım
---

# 📃 Tek Sayfa Anlatım

## 🚧 Tensorflow Kurulumu

* Tensorflow anaconda üzerinden daha sağlıklı, taşınabilir ve verimli çalışabilmekte
* Anaconda'nın sanal ortamları, paketlerin çakışmasını engelleyecektir
* Anaconda'nın Tensorflow'daki avantajı için [buraya](https://www.anaconda.com/tensorflow-in-anaconda/) göz atabilirsin.

{% tabs %}
{% tab title="💚 Anaconda Kurulumu" %}
{% embed url="https://python.yemreak.com/anaconda/anacondaya-giris" %}
{% endtab %}

{% tab title="💛 Tensorflow CPU veya GPU Kurulumu" %}
* Bu kurulum CPU kurulumu olarak da geçmekte
* GPU kurulumu CPU'ya nazaran oldukça hızlı eğitim seçeneği sağlar
* GPU kurulumu için gereksinimleri sağlıyorsanız GPU kurulumu \(tensorflow-gpu\) yapmanız tavsiye edilir

#### Sanal Ortam Oluşturma ve Üzerine Kurma

```text
conda create -n tensorflow tensorflow # CPU kurulumu
conda create -n tensorflow tensorflow-gpu # GPU kurulumu
```
{% endtab %}

{% tab title="✅ Kurulumu Test Etme" %}
Alttaki komut ile 'Hello, TensorFlow!' çıktısını almanız gerekmektedir.

```text
python -c
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
>>> print(sess.run(hello))
```
{% endtab %}
{% endtabs %}

## 🚧 Tensorflow Algılama Modellerinin Kurulumu

* Algılama modelleri tabloma erişmek için [buraya](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/detection_models/tensorflow_algılama_modelleri.pdf) tıklayabilirsin
  * Resmi sitesi için [buraya](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) bakabilirsin
* Video üzerinden açıklama için [buraya](https://youtu.be/COlbP62-B-U) bakabilirsin

{% hint style="info" %}
Resmi açıklamalar `models/research/object_detection/g3doc` dizinindedir.
{% endhint %}

{% tabs %}
{% tab title="📦 Paketler" %}
Tensorflow modellerini kullanabilmek için alttaki kurulumlara da ihtiyaç olabilmekte:

```text
conda install opencv pillow matplotlib pandas jupyter
```

{% hint style="info" %}
Modül bulunamaması gibi durumlarda `lxml`, `protobuf` paketlerini yüklemeyi deneyebilirsin.
{% endhint %}

### 🐧 Linux için OpenCv Kurulumu

GTK ve FFMPEG hatasını engellemek için pip ile kurulum yapın

```bash
pip install opencv-contrib-python
```

### 🍱 Script Dosyaları için Gerekli Modüller

```text
pip install pynput # detect_from_desktop
```
{% endtab %}

{% tab title="🤖 Modeller" %}
Alttaki talimatler ve komutlar yardımıyla tensorflow modellerini kurun:

* Modelleri indirmek için [buraya](https://github.com/tensorflow/models/archive/master.zip) tıklayabilirsin
* İstersen [buraya](https://github.com/tensorflow/models) tıklayarak github linkine erişebilirsin
* İndirdiğiniz dosyanın içindekileri `models` dizinine koymanız gerekmektedir.

{% hint style="warning" %}
Bu adından sonrası `models/research/` dizininde gerçekleştirilmelidir.
{% endhint %}

```text
powershell.exe Expand-Archive models-master.zip .
ren models-master models
move models %TENSORFLOW%
cd %TENSORFLOW%\models\research\
```

#### Models Klasörü Yapısı

```text
+ models
    + offical
    + research
    + sample
    ...
```
{% endtab %}

{% tab title="✨ Protobuff\'ların İşlenmesi" %}
Protobuf dosyaları \(`.proto` uzantılı olan dosyalar\) python kodlanı oluşturmak için kullanılan dosyalardır. `TensorFlow/models/research/` dizininde

Windows:

```text
for /f %i in ('dir /b object_detection\protos\*.proto') do protoc object_detection\protos\%i --python_out=.
```

Linux:

```bash
protoc object_detection/protos/*.proto --python_out=.
```

{% hint style="info" %}
Protobuflarların işlenmesiyle `.py` uzantılı dosyalar oluşacaktır
{% endhint %}
{% endtab %}

{% tab title="🧐 Obje Algılama Kütüphaneleri" %}
```bash
# TensorFlow/models/research/ dizininde
python setup.py build
python setup.py install
```
{% endtab %}

{% tab title="🌃 Ortam Değişkenleri" %}
Eğer daha önceden tanımlı `PYTHONPATH` ortam değişkeniniz **yoksa ilk olan**, **varsa ikinci olan** komutu kullanın.

{% hint style="warning" %}
Bu ortam değişkenlerinin **terminalin her açılışında yazılması** gerekmektedir.
{% endhint %}

```text
set PYTHONPATH=%TENSORFLOW%\models\research;%TENSORFLOW%\models\research\slim;%TENSORFLOW%\models\research\object_detection
```

```text
set PYTHONPATH=%PYTHONPATH%;%TENSORFLOW%\models\research;%TENSORFLOW%\models\research\slim;%TENSORFLOW%\models\research\object_detection
```

### 💫 Anaconda Ortamı için Otomatik Tanımlama

* Her `conda activate <ortam_ismi>` komutu yazıldığında ortamlar dahil edilir
* Her `conda deactivate` yazıldığında ortamlar kaldırılır

#### **🎇 Windows için Otomatik Tanımlama**

```text
cd <conda_ortamı_yolu>
mkdir .\etc\conda\activate.d
echo set PYTHONPATH=%TENSORFLOW%\models\research;%TENSORFLOW%\models\research\slim;%TENSORFLOW%\models\research\object_detection > .\etc\conda\activate.d\env_vars.bat
```

#### **🐧 Linux için Otomatik Tanımlama**

Resmi kaynak için [buraya](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#macos-and-linux) bakabilirsin.

```bash
cd <conda_ortamı_yolu>
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
echo export PYTHONPATH=${PYTHONPATH}:${TENSORFLOW}/models/research:${TENSORFLOW}/models/research/slim:${TENSORFLOW}/models/research/object_detection > etc/conda/activate.d/env_vars.sh
echo unset PYTHONPATH > etc/conda/deactivate.d/env_vars.sh
```

* `<conda_ortamı_yolu>` Conda ortamının kurulduğu yol
  * _Örn: %USERPROFILE%\Anaconda3\envs\tensorflow-cpu_
{% endtab %}

{% tab title="✅ Kurulumları Test Etme" %}
Jupyter notebook ile API'ları test etmemiz gerekmekte.

```bash
cd object_detection
jupyter notebook
```

{% hint style="info" %}
Jupyter notebook hakkında bilgi sahibi değilsen [buraya](https://www.youtube.com/watch?v=COlbP62-B-U&feature=youtu.be&t=7m23s) tıklayarak ne yapman gerektiğini öğrenebilirsin.
{% endhint %}
{% endtab %}
{% endtabs %}

## 💷 LabelImg Kurulumu

* LabelImg tensorflow modelleri için etiketleme amaçlı kullanılmaktadır
* Derlenmiş sürümünü indirmek için [buraya](http://tzutalin.github.io/labelImg/) tıklayabilirsin
* Derlenmiş sürümü çalışmazsa alttaki yönerge ile derleyebilirsin

{% hint style="info" %}
İndirilen dosyayı `%TENSORFLOW%\addons` dizinine atmanız daha verimli bir çalışma sağlayacaktır.
{% endhint %}

{% tabs %}
{% tab title="🌆 Sanal Ortam Oluşturma" %}
Tensorflow ortamının alt paketlerini etkilememsi için ek bir sanal ortamda kurulum sağlamalıyız.

```bash
conda create -n labelImg pyqt # QT grafik kütüphanesi
conda activate labelImg
conda install -c anaconda lxml
```
{% endtab %}

{% tab title="📦 Paketlerini Kurma ve Derleme" %}
Paketlerin kurulumu için alttaki talimatları sırayla uygulayın:

* LabelImg dosyalarını indirmek için [buraya](https://github.com/tzutalin/labelImg/archive/master.zip) tıklayın
* Diğer işlemler için indirdiğiniz dosya dizininde cmd açıp alttaki komutları yazın

```bash
# labelImg-master.zip dizininde
powershell.exe Expand-Archive labelImg-master.zip .
ren labelImg-master labelImg
mkdir %TENSORFLOW%\addons
move labelImg %TENSORFLOW%\addons
cd %TENSORFLOW%\addons\labelImg
pyrcc5 -o resources.py resources.qrc # QT grafiklerinin oluşturulması
```

> _'pyrcc5' is not recognized as an internal or external command_ hatası gelirse, yüklediğiniz `pyqt` sürümüne göre komutu kullanın \(`pyrcc<pyqt_sürümü_ilk_basamağı>`\)
{% endtab %}

{% tab title="✅ Test Etme" %}
```bash
conda activate tensorflow-cpu
cd %TENSORFLOW%\addons\labelImg
python labelImg.py
# python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```
{% endtab %}
{% endtabs %}

## 📂 Dizin Yapısını Oluşturma

### 🌃 Tensorflow Dizininizi Geçici Ortam Değişkenlerine Ekleme

{% tabs %}
{% tab title="⚡ Hızlı İşlem" %}
Alttaki komut yardımıyla açık olan cmd ekranına ortam değişkeni tanımlayabilirsiniz.

```text
set TENSORFLOW=<dizin_yolu>
```

* `<dizin_yolu>` Tensorflow'u kurmak istediğiniz dizin
  * _Örn: "C:\Tensorflow"_
{% endtab %}

{% tab title="🚀 Kalıcı İşlem" %}
* Bilgisayarıma sağ tıklayın `Ayarlar` kısmına girin
* Sol alanda `Gelişmiş Sistem Ayarları`'na tıklayın
* Açılan ekranda `Ortam Değişkenleri` butonuna tıklayın
* Üst kısımdaki kullanıcı değişkenleri alanında `Yeni` butonuna tıklayın
* Değişken ismine: `Tensorflow` Değerine: 'dizin yolunuzu' yazın
{% endtab %}
{% endtabs %}

### 🧱 Temel Klasörlerin Oluşturulması

{% tabs %}
{% tab title="👩‍💻 Kod ile Dizin Oluşturma" %}
İlerideki yapı için bu dizinin yolu `%TENSORFLOW%` olarak ifade edilecektir.

{% hint style="success" %}
Düzgün ve verimli çalışmak için buradaki yapıyı kullanmanız önerilir.
{% endhint %}

```text
mkdir %TENSORFLOW%\workspace\example_detection
mkdir %TENSORFLOW%\workspace\example_detection\data
mkdir %TENSORFLOW%\workspace\example_detection\images\train
mkdir %TENSORFLOW%\workspace\example_detection\images\eval
mkdir %TENSORFLOW%\workspace\example_detection\models
```
{% endtab %}

{% tab title="📂 Temel Yapı" %}
```text
+ addons
+ docs
+ models
+ scripts
+ workspace
    + example_detection
        + data
        + models
            + <model_ismi>
                + eval
                + train
                - *.config
                ...
            + <model_ismi>
                + eval
                + train
                - *.config
                ...
            ...
        ...
    + example2_detection
        + data
        + models
            + <model_ismi>
                + eval
                + train
                - *.config
                ...
            + <model_ismi>
                + eval
                + train
                - *.config
                ...
            ...
        ...
```

| Dizin | Açıklama |
| :--- | :--- |
| addons | LabelImg vs. |
| docs | Dökümanlar |
| models | Tensorflow Models dosyası |
| scripts | Kullanacağınız ortak kod parçaları |
| workspace | Çalışma Alanı |
{% endtab %}

{% tab title="👨‍💼 Çalışma Alanı" %}
```text
+ workspace
    + example_detection
        + data
        + models
        ...
    + example2_detection
        + data
        + models
        ...
    ...
```

| Dizin | Açıklama |
| :--- | :--- |
| data | Eğitime katılacak verileri \(_eval.record, train.record, label\_map_\) içeririr. |
| model | Eğitilecek modellerin dosyalarını içerir. |
{% endtab %}

{% tab title="📀 Data" %}
```text
+ example_detection
    + data
        - label_map.pbtxt
        - eval.record
        - train.record
    + models
    ...
...
```

| Dosya | Açıklama |
| :--- | :--- |
| `label_map.pbtxt` | Etiket haritası dosyası |
| `eval.record` | Test için kullanılacak tensorflow kayıtları \(TF record\) |
| `train.record` | Eğitim için kullanılacak tensorflow kayıtları \(TF record\) |
{% endtab %}

{% tab title="🤖 Model Dizini" %}
```text
+ example_detection
    + data
    + models
        + <model_ismi>
            + eval
            + train
            - *.config
            ...
        + <model_ismi>
            + eval
            + train
            - *.config
            ...
        ...
    ...
...
```

Her bir model için ayrı dizinler oluşturulur.

| İsim | Tipi | Açıklama |
| :--- | :--- | :--- |
| eval | Dizin | Test sonuçları burada tutulur. |
| train | Dizin | Eğitim çıktıları burada tutulur |
| `.config` | Dosya | Yapılandırma dosyası |
{% endtab %}
{% endtabs %}

{% hint style="info" %}

{% endhint %}

## 👨‍🏫 Özelleştirilmiş Tensorflow Obje Algılayıcısı Eğitme

Özelleştirilmiş model eğitmek için alttakilerin yapılmış olması gerekmektedir:

* [🚧 Tensorflow Kurulumu](tek-sayfa-anlatim.md#tensorflow-kurulumu)
* [🚧 Tensorflow Algılama Modellerinin Kurulumu](tek-sayfa-anlatim.md#tensorflow-algilama-modellerinin-kurulumu)
* [💷 LabelImg Kurulumu](tek-sayfa-anlatim.md#labelimg-kurulumu)

{% tabs %}
{% tab title="🎴 Resim Etiketleme" %}
Etiketleme işlemini **labelImg** üzerinden yapmaktayız.

### 👨‍💻 Derlenmiş LabelImg

İndirdiğiniz dizindeki `labelimg.exe` dosyasını çalıştırmanız yeterlidir.

### 🐍 Python ile LabelImg

İşlemleri **Anconda Prompt** ile işlemler yapmalıyız.

```bash
conda activate labelImg
cd %TENSORFLOW%\addons\labelImg
python labelImg.py ..\..\workspace\example_detection\images # çıktıları hedefleme
```

### 👨‍🔧 Etiket Yollarını veya Adlarını Düzenleme

XML ve resim dosyalarını başka bir yolda oluşturduyasan alttaki script yardımıyla düzeltebilirsin

* Script dosyasını [buraya](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/resources/xml_path_regulator.py) tıklayarak indirmeli ve gerekli dizine alttaki komutla koymalıyız
* Komutları **Anaconda Prompt** üzerinden **tensorflow** ortamını aktif ederek uygulamayı unutmayın.

```bash
# Train verilerini yeniden adlandırma ve düzeltme
python xml_path_regulator.py -i %TENSORFLOW%\workspace\example_detection\images\train -p train

# Test verilerini yeniden adlandırma ve düzeltme
python xml_path_regulator.py -i %TENSORFLOW%\workspace\example_detection\images\eval -p eval
```

{% hint style="info" %}
LabelImg kullanımı için [bu videoya](https://www.youtube.com/watch?v=K_mFnvzyLvc&feature=youtu.be&t=9m13s) bakabilirsin.
{% endhint %}
{% endtab %}

{% tab title="🌍 Etiket Haritası Oluşturma" %}
* Alttaki komutla açılan dizinde `.pbtxt` uzantılı etiket haritası dosyasısı oluşturun
* Örnek dosya yapısı komutların altındadır.

```bash
cd %TENSORFLOW%\workspace\example_detection\annotations
start .
```

```javascript
item {
  id: 1
  name: 'cat'
}
item {
  id: 2
  name: 'dog'
}
```

* `cat` ve `dog` etiket isimleridir
{% endtab %}

{% tab title="📃 Tensorflow Kayıtları Oluşturma" %}
* **Resim** verileri toplanır veya çekilir.
* Toplanan resimler `labelimg` yardımıyla etiketlenir ve `.xml` uzantılı dosyaları oluşturulur.
* `images` dizinine **resimler** ve onlara ait **xml** dosyaları %80'i train %20'i eval olacak şekilde klasörlere ayrılarak yerleştirilir.
* `scripts/preprocessing` dizindeki `xml_path_regulator.py` scripti aracılığıyla xml ve resimlerde yol sorunları düzeltilir, veriler yeniden adlandırılır.
* `scripts/preprocessing` dizindeki `xml_to_csv.py` scripti aracılığıyla veriler `.csv` uzantılı tablosal bir dosyaya dönüştürülür.
* Oluşturulan **csv** dosyasında resimlerin etiketlerine göre sayıları [tablo]() olarak gösterilir. \(Excel yardımıyla\)
* Verilerde denge durumunun \(her veriden yaklaşık olarak aynı sayıda varsa\) kontrolü yapılır.
* Her çeşit veri için bir `id` belirtilecek şekilde `label_map.pbtxt` adlı etiket haritası oluşturulur
* Oluşturulan **csv**, **etiket haritası** ve **resim** verileri `scripts/preprocessing` dizindeki `generate_tfrecord.py` scripti aracılığıyla veriler `.record` uzantılı kayıtlara dönüştürülür.
* Seçilen modele özgü yapılandırma dosyası indirilir.
* Yapılandırma dosyası olan `*.config` dosyasındaki `PATH_TO_CONFIGURED` olarak işaretlenen alanlar, `num_classes`, `num_examples` ve `batch_size` değerleri güncellenir.
  * `num_examples` eval dizindeki resim sayısıdır \(toplam class sayısı değil\)

**Resimlerdeki Hataları Bulma**

Resimlerde hata olduğu zaman eğitim aşamasında tensorflow modeli çalışma hatası vermektedir. Resimleri kontrol etmek için [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/check_images.py) scripti alttaki komutlarla kullanabilirsiniz.

```text
python scripts\preprocessing\check_images.py -i workspace\example_detection\images\train

python scripts\preprocessing\check_images.py -i workspace\example_detection\images\eval
```

**Verileri Yeniden Adlandırma ve XML Hatalarını Düzeltme**

LabelImg ile etiketlediğiniz resimleri farklı bir dizine taşımanız durumunda XML dosyalarındaki yollar uyuşmayacaktır. XML dosya yollarını düzeltmek, etiketsiz resimleri görüntülemek için [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/xml_path_regulator.py) script dosyamı alttaki komutlar ile kullanabilirsiniz.

```text
python scripts\preprocessing\xml_path_regulator.py -i %TENSORFLOW%\workspace\example_detection\images\train  -p train

python scripts\preprocessing\xml_path_regulator.py -i %TENSORFLOW%\workspace\example_detection\images\eval  -p eval
```

**Etiketlenmemiş Resimleri Bulma**

Etiketlenmemiş resimleri [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/find_unlabeled_imgs.py) script dosyası ile alttaki komutlar ile kullanabilirsiniz.

> Eğer XML scriptini kullandıysanız bu kontrolü yapmanıza **gerek yoktur**, XML scripti bunu zaten yapmaktadır.

```text
python scripts\preprocessing\find_unlabeled_imgs.py -i %TENSORFLOW%\workspace\example_detection\images\train

python scripts\preprocessing\find_unlabeled_imgs.py -i %TENSORFLOW%\workspace\example_detection\images\eval
```

**XML'i CSV'ye Çevirme**

XML dosyalarını CSV dosyasında toparlamak için [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/xml_to_csv.py) scripti alttaki komutlar ile kullanabilirsin.

> Komutları **Anaconda Prompt** üzerinden **tensorflow** ortamını aktif ederek uygulamayı unutmayın.

```bash
# Create train data:
python scripts\preprocessing\xml_to_csv.py -i %TENSORFLOW%\workspace\example_detection\images\train -o %TENSORFLOW%\workspace\example_detection\images\train_labels.csv

# Create eval data:
python scripts\preprocessing\xml_to_csv.py -i %TENSORFLOW%\workspace\example_detection\images\eval -o %TENSORFLOW%\workspace\example_detection\images\test_labels.csv
```

**CSV'lerden Resim Bilgilerini Analiz Etme**

Her bir etiketten kaç tane olduğunu anlamak için csv dosyalarını açıp alltaki yöntemi uygulayın.

* `class` hücresiinin bir altındaki hücreyi seçin
* `ctrl` + `shift` + `aşağı ok` ile tüm sınıf verilerini seçin
* Sağ alttaki butona tıklayın
* `Tables` sekmesine gelin
* Açılan sekmede `Pivot Table` butonuna tıklayın
* Tablo'dan etiketlenen verileri kontrol edin
* Fazladan etiketlenmiş verilerin ismini bulup, filename, width vs. verilerin yazıldığı alanda `CTRL` + `F` komutu ile aratıp, uygun dosya ismini ve `xml` dosyasını silin

![](../.gitbook/assets/image%20%2830%29.png)

![](../.gitbook/assets/image%20%2832%29.png)

![](../.gitbook/assets/image%20%2822%29.png)

![](../.gitbook/assets/image%20%2814%29.png)

**CSV'yi Record'a Çevirme**

CSV dosyalarını TF kayıtlarına çevirmek için [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/generate_tfrecord.py) scripti alttaki komutlar ile kullanabilirsin.

> Komutları **Anaconda Prompt** üzerinden **tensorflow** ortamını aktif ederek uygulamayı unutmayın.

```text
python generate_tfrecord.py --label_map=%TENSORFLOW%\workspace\example_detection\data\label_map.pbtxt --csv_input=%TENSORFLOW%\workspace\example_detection\images\train_labels.csv --img_path=%TENSORFLOW%\workspace\example_detection\images\train --output_path=%TENSORFLOW%\workspace\example_detection\data\train.record

python generate_tfrecord.py --label_map=%TENSORFLOW%\workspace\example_detection\data\label_map.pbtxt --csv_input=%TENSORFLOW%\workspace\example_detection\images\test_labels.csv --img_path=%TENSORFLOW%\workspace\example_detection\images\eval --output_path=%TENSORFLOW%\workspace\example_detection\data\eval.record
```
{% endtab %}

{% tab title="🍢 Pipeline Yapılandırma" %}
* Tensorflow'un resmi açıklaması için [buraya](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/configuring_jobs.md) tıklayabilirisin

#### Medellin İndirilmesi ve Gerekli Yere Taşınması

* Tensorflow önceden eğitilmiş modelleri indirmek için [buraya](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md#coco-trained-models-coco-models) tıklayabilirsin
* `.tar.gz` uzantılı olacağı için [winrar](https://www.win-rar.com/download.html?&L=0) ya da [7zip](https://www.7-zip.org/download.html) gibi ek uygulamalarla `buraya çıkart` demen gerekmekte
  * `Klasör'e çıkart` değil `buraya çıkart` diyeceksiniz.

{% hint style="warning" %}
Klasör içinde aynı isimde başka klasör olmasın
{% endhint %}

```bash
# Modelin çıkartıldığı dizinde
cd <model_ismi>
move * %TENSORFLOW%\workspace\example_detection\pre_trained_model
move saved_model %TENSORFLOW%\workspace\example_detection\pre_trained_model
cd %TENSORFLOW%\workspace\example_detection\pre_trained_model
```

* `<model_ismi>` Seçip, indirdiğiniz `.tar.gz` uzantılı dosyanın adı
  * `TAB` tuşu ile dizindeki dosya adlarını tamamlayabilirsiniz
  * `*.tar.gz` uzantısı yazılmayacak
  * _Örn: ssd\_inception\_v2\_coco\_2018\_01\_28_
  * _Örn: ssd\_mobilenet\_v1\_ppn\_shared\_box\_predictor\_300x300\_coco14\_sync\_2018\_07\_03_

#### Modellin Yapılandırma Dosyaları

Seçtiğiniz modelin `*.config` dosyasını `example_detection/training` klasörü altına kopyalamanız gerekmekte.

```bash
mkdir %TENSORFLOW%\workspace\example_detection\training

copy %TENSORFLOW%\models\research\object_detection\samples\configs\<model_ismi>.config %TENSORFLOW%\workspace\example_detection\training
```

* `<model_ismi>` Seçip, indirdiğiniz `.tar.gz` uzantılı dosyanın adı
  * `TAB` tuşu ile dizindeki dosya adlarını tamamlayabilirsiniz
  * `*.tar.gz` uzantısı yazılmayacak
  * Tarih son ekini içermemeli
    * `*_2018_07_03.tar.gz` ise `*.tar.gz` olarak yazılmalı
  * _Örn: ssd\_inception\_v2_
  * _Örn: ssd\_mobilenet\_v1\_ppn\_shared\_box\_predictor\_300x300\_coco14\_sync_

#### Modelin Yapılandırma Dosyasını Düzenleme

Yapılandırma örnek dosyası için [buraya](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/workspace/traffic_light_detector/training/ssd_mobilenet_v2_coco.config) bakabilirsin.

| Düzenlenecek Satır | Açıklama | Örnek |
| :--- | :--- | :--- |
| `num_classes` | Etiket türü sayısı | `2` |
| `batch_size` | Toplu işleme boyutu | `24` |
| `num_steps` | Adım sayısı | `2000` |
| `fine_tune_checkpoint` | Eğitilmiş modelin yolu | `"./pre_trained_model/model.ckpt"` |
| `label_map_path` | Etiket haritası yolu | `"./annotations/train.record"` |
| `input_path` | Train dosyası yolu | `"./annotations/train.record"` |
| `input_path` | Test dosyası yolu | `"./annotations/eval.record"` |
{% endtab %}

{% tab title="🤖 Modeli Eğitme" %}
Modeli eğitmek için `train.py` script dosyasını kullanacağız.

> Modeli önerilen dosya olan `model_main.py` ile eğitmek için [buraya]() bakmalısın.

#### Eğitim Scriptlerini Çalışma Alanına Kopyalama

Çalışma ortamının düzgün ilerlemesi adına alttaki komut ile gerekli yere scripti kopyalayalım

```bash
copy %TENSORFLOW%\models\research\object_detection\legacy\train.py %TENSORFLOW%\workspace\example_detection
copy %TENSORFLOW%\models\research\object_detection\model_main.py
```

#### Eğitimde Raporlanacak Seviyeyi Ayarlama \(isteğe Bağlı\)

Eğitimde uyarı ve bilgileri gizlemek için `TF_CPP_MIN_LOG_LEVEL` adlı ortam değişkeni oluşturup seviyesini tanımlıyoruz

```bash
set TF_CPP_MIN_LOG_LEVEL=2
```

#### Modeli train.py Dosyası ile Eğitime

`# TODO Daha düzgün ve detaylı linkli bir yazı ekle`

> Eskimiş olan bir eğitim kodudur, `model_main.py` kod dosyası tensorflow tarafından önerilir.

```bash
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training\<yapılandırma_dosyası>
```

* `<yapılandırma_dosyası>` Modelimizin yapılandırma dosyasının tam adı
  * **training** klasörüne attığımız yapılandırma dosyaları
  * _Örn: ssd\_inception\_v2\_coco.config_

**Eğitime Başladığında Gelen Örnek Çıktı**

```bash
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:Restoring parameters from ssd_inception_v2_coco_2017_11_17/model.ckpt
INFO:tensorflow:Running local_init_op.
INFO:tensorflow:Done running local_init_op.
INFO:tensorflow:Starting Session.
INFO:tensorflow:Saving checkpoint to path training\model.ckpt
INFO:tensorflow:Starting Queues.
INFO:tensorflow:global_step/sec: 0
INFO:tensorflow:global step 1: loss = 13.8886 (12.339 sec/step)
INFO:tensorflow:global step 2: loss = 16.2202 (0.937 sec/step)
INFO:tensorflow:global step 3: loss = 13.7876 (0.904 sec/step)
INFO:tensorflow:global step 4: loss = 12.9230 (0.894 sec/step)
INFO:tensorflow:global step 5: loss = 12.7497 (0.922 sec/step)
INFO:tensorflow:global step 6: loss = 11.7563 (0.936 sec/step)
INFO:tensorflow:global step 7: loss = 11.7245 (0.910 sec/step)
INFO:tensorflow:global step 8: loss = 10.7993 (0.916 sec/step)
INFO:tensorflow:global step 9: loss = 9.1277 (0.890 sec/step)
INFO:tensorflow:global step 10: loss = 9.3972 (0.919 sec/step)
INFO:tensorflow:global step 11: loss = 9.9487 (0.897 sec/step)
INFO:tensorflow:global step 12: loss = 8.7954 (0.884 sec/step)
INFO:tensorflow:global step 13: loss = 7.4329 (0.906 sec/step)
INFO:tensorflow:global step 14: loss = 7.8270 (0.897 sec/step)
INFO:tensorflow:global step 15: loss = 6.4877 (0.894 sec/step)
```

#### Modeli model\_main.py Dosyası ile Eğitme

Bu dosya ile eğitim önerilen eğitim şeklidir.

* `train.py` ile eğitime nazaran, kaldığı yerden devam eder
  * 1000 adım yapıldıysa, ikinci eğitimi 1200 yaptığınızda 200 adım eğitir
  * `train.py` eğitiminde modelin sonucunun ayırılıp, sonuç üzerinden eğitim yapılması gerekir

> Eğitim dosyaları arasında **performans veya kalite farkı yoktur**, kaynak için [buraya](https://github.com/tensorflow/models/issues/6100) bakabilirsin.

**Eğitim için Gereksinimlerin Kurulması**

Eğitim için `pycocotools` kurulumu gereklidir

**Windows için PyCocoTools Kurulumu**

Windows desteğiyle kurulum yapmak için alttaki komutu koşturun

```bash
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```

> Açıklama için [buraya](https://github.com/philferriere/cocoapi) bakabilirsin.

**Linux için Cocotools**

```bash
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make
cp -r pycocotools /content/models/research/
cd ../..
rm -rf cocoapi
```

**Eğitimi Hazırlama ve Başlatma**

Resmi kaynağa ulaşmak için [buraya](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_locally.md) bakabilirsin.

* `model_main.py` eğitim için önerilen dosyadır
* Varsayılan olarak ekrana raporlama yapmaz, yapmasını isterseniz [buraya](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10/issues/184#issuecomment-437811347) bakabilirsiniz

```bash
# From the tensorflow/models/research/ directory
PIPELINE_CONFIG_PATH={path to pipeline config file}
MODEL_DIR={path to model directory}
NUM_TRAIN_STEPS=50000
SAMPLE_1_OF_N_EVAL_EXAMPLES=1
python object_detection/model_main.py \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --model_dir=${MODEL_DIR} \
    --num_train_steps=${NUM_TRAIN_STEPS} \
    --sample_1_of_n_eval_examples=$SAMPLE_1_OF_N_EVAL_EXAMPLES \
    --alsologtostderr
```

#### Eğitimi Etkileyen Faktörler

Training times can be affected by a number of factors such as:

* The computational power of you hardware \(either CPU or GPU\): Obviously, the more powerful your PC is, the faster the training process.
* Whether you are using the TensorFlow CPU or GPU variant: In general, even when compared to the best CPUs, almost any GPU graphics card will yield much faster training and detection speeds. As a matter of fact, when I first started I was running TensorFlow on my Intel i7-5930k \(6/12 cores @ 4GHz, 32GB RAM\) and was getting step times of around 12 sec/step, after which I installed TensorFlow GPU and training the very same model -using the same dataset and config files- on a EVGA GTX-770 \(1536 CUDA-cores @ 1GHz, 2GB VRAM\) I was down to 0.9 sec/step!!! A 12-fold increase in speed, using a “low/mid-end” graphics card, when compared to a “mid/high-end” CPU.
* How big the dataset is: The higher the number of images in your dataset, the longer it will take for the model to reach satisfactory levels of detection performance.
* The complexity of the objects you are trying to detect: Obviously, if your objective is to track a black ball over a white background, the model will converge to satisfactory levels of detection pretty quickly. If on the other hand, for example, you wish to detect ships in ports, using Pan-Tilt-Zoom cameras, then training will be a much more challenging and time-consuming process, due to the high variability of the shape and size of ships, combined with a highly dynamic background.
* And many, many, many, more. . . .

#### Eğitim İşlemini TensorBoard Kullanarak Takip Etme

**Anaconda Prompt** üzerinden alttaki komutlar uygulanır:

```bash
activate tensorflow_cpu # ya da gpu
tensorboard --logdir=training\
```

Alttaki gibi bir çıktı gelmesi gerekmekte:

```bash
TensorBoard 1.6.0 at http://YOUR-PC:6006 (Press CTRL+C to quit)
```

> Çıktıyı görüntülemek için verilen url'i tarayıcına kopyalaman yeterlidir.

#### Sonuç Grafiğini Dışarı Aktarma

**Anaconda Prompt** üzerinden alttaki komutlar uygulanır:

```bash
activate tensorflow_cpu # ya da gpu

copy %TENSORFLOW%\models\research\object_detection/export_inference_graph.py %TENSORFLOW%\workspace\example_detection

cd %TENSORFLOW%\workspace\example_detection

python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/<yapılandırma_dosyası> --trained_checkpoint_prefix training/model.ckpt-<checkpoint> --output_directory trained-inference-graphs/output_inference_graph_v1.pb
```

* `<yapılandırma_dosyası>` Modelimizin yapılandırma dosyasının tam adı
  * **training** klasörüne attığımız yapılandırma dosyaları
  * _Örn: ssd\_inception\_v2\_coco.config_
* `<checkpoint>` **example\_detection/training** dizinindeki gösterilmek istenen adımın numarası
  * _Örn: 13302_
{% endtab %}
{% endtabs %}

## 🌠 Colab Üzerinden Tensorflow Modelini Eğitme

Colab ücretsiz GPU sunduğu için çok hızlı bir eğitim imkanı sunar.

### 📂 Colab Eğitimi için Gereken Dosyalar

* label\_map.pbtxt
* eval.record
* train.record
* \*.config
* model\_main.py \(eskisi: train.py\)
* export\_inference\_graph.py

### 👩‍💻 Colab Üzerinden Eğitim Kodları

{% embed url="https://colab.research.google.com/drive/1JvMqUga8ALUF-YwPp4gPVZ8SjxsOoFad" %}


# 🚧 Tensorflow Algılama Modellerinin Kurulumu

## 🔰 Temel Bilgiler

* Algılama modelleri tabloma erişmek için [buraya](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/detection_models/tensorflow_algılama_modelleri.pdf) tıklayabilirsin
  * Resmi sitesi için [buraya](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) bakabilirsin
* Video üzerinden açıklama için [buraya](https://youtu.be/COlbP62-B-U) bakabilirsin

{% hint style="info" %}
Resmi açıklamalar `models/research/object_detection/g3doc` dizinindedir.
{% endhint %}

## 📦 Paketlerin Kurulumu

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

## 🤖 Modellerin Kurulumu

Alttaki talimatlar ve komutlar yardımıyla tensorflow modellerini kurun:

* Modelleri indirmek için [buraya](https://github.com/tensorflow/models/archive/master.zip) tıklayabilirsin
* İstersen [buraya](https://github.com/tensorflow/models) tıklayarak GitHub linkine erişebilirsin
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

**Models Klasörü Yapısı**

```text
+ models
    + offical
    + research
    + sample
    ...
```

## ✨ Protobuff'ların İşlenmesi

* 📃 Protobuf dosyaları \(`.proto` uzantılı olan dosyalar\) 
* 👨‍💻 Python kodlarını oluşturmak için kullanılan dosyalardır.
* 📢 İşlemler `TensorFlow/models/research/` dizininde yapılmalıdır

{% tabs %}
{% tab title="🎇 Windows" %}
```bash
for /f %i in ('dir /b object_detection\protos\*.proto') ^
do protoc object_detection\protos\%i --python_out=.
```
{% endtab %}

{% tab title="🐧 Linux" %}
```bash
protoc object_detection/protos/*.proto --python_out=.
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
Protobuff'ların işlenmesiyle `.py` uzantılı dosyalar oluşacaktır
{% endhint %}

## 🧐 Obje Algılama Paketlerinin Kurulumu

```python
python setup.py build
python setup.py install
```

## 🌃 Ortam Değişkenlerini Tanımlama

Ortam değişkenleri 2 farklı yöntemle tanımlanabilir.

### ✨ Geçici Tanımlama

```bash
set PYTHONPATH=%PYTHONPATH%;%TENSORFLOW%\models\research;^
%TENSORFLOW%\models\research\slim;^
%TENSORFLOW%\models\research\object_detection
```

{% hint style="warning" %}
📢 Terminal her açıldığında yapılması gerekmektedir
{% endhint %}

### 💫 Otomatik Tanımlama

* Her `conda activate <ortam_ismi>` komutu yazıldığında ortamlar dahil edilir
* Her `conda deactivate` yazıldığında ortamlar kaldırılır
* `<conda_ortamı_yolu>` Conda ortamının kurulduğu yol
  * _Örn: `%USERPROFILE%\Anaconda3\envs\tensorflow-cpu`_

{% hint style="info" %}
‍🧙‍♂ Resmi kaynak için [buraya](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#saving-environment-variables) bakabilirsin.
{% endhint %}

{% tabs %}
{% tab title="🎇 Windows" %}
```bash
cd <conda_ortamı_yolu>
mkdir .\etc\conda\activate.d
echo set PYTHONPATH=%TENSORFLOW%\models\research;^
%TENSORFLOW%\models\research\slim;^
%TENSORFLOW%\models\research\object_detection > .\etc\conda\activate.d\env_vars.bat
```
{% endtab %}

{% tab title="🐧 Linux" %}
```bash
cd <conda_ortamı_yolu>
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
echo export PYTHONPATH=${PYTHONPATH}:${TENSORFLOW}/models/research:\
${TENSORFLOW}/models/research/slim:\
${TENSORFLOW}/models/research/object_detection > etc/conda/activate.d/env_vars.sh
echo unset PYTHONPATH > etc/conda/deactivate.d/env_vars.sh
```
{% endtab %}
{% endtabs %}

## ✅ Kurulumları Test Etme

Jupyter notebook ile API'ları test etmemiz gerekmekte.

```bash
cd object_detection
jupyter notebook
```

{% hint style="info" %}
‍🧙‍♂ Jupyter notebook hakkında bilgi sahibi değilsen [buraya](https://www.youtube.com/watch?v=COlbP62-B-U&feature=youtu.be&t=7m23s) tıklayarak ne yapman gerektiğini öğrenebilirsin.
{% endhint %}


# 👨‍🏫 Modeli Eğitime

## 🔰 Ön Bilgiler

Modeli eğitmek için `train.py` script dosyasını kullanacağız.

{% hint style="info" %}
Modeli önerilen dosya olan `model_main.py` ile eğitmek için buraya bakmalısın.
{% endhint %}

## 🩹 Eğitim Scriptlerini Çalışma Alanına Kopyalama

Çalışma ortamının düzgün ilerlemesi adına alttaki komut ile gerekli yere scripti kopyalayalım

```text
copy %TENSORFLOW%\models\research\object_detection\legacy\train.py %TENSORFLOW%\workspace\example_detectioncopy %TENSORFLOW%\models\research\object_detection\model_main.py
```

## 📜 Eğitimde Raporlanacak Seviyeyi Ayarlama \(isteğe Bağlı\)

Eğitimde uyarı ve bilgileri gizlemek için `TF_CPP_MIN_LOG_LEVEL` adlı ortam değişkeni oluşturup seviyesini tanımlıyoruz

```text
set TF_CPP_MIN_LOG_LEVEL=2
```

## **📦 Eğitim için Gereksinimlerin Kurulması**

Eğitim için `pycocotools` kurulumu gereklidir

{% tabs %}
{% tab title="🎇 Windows" %}
Windows desteğiyle kurulum yapmak için alttaki komutu koşturun

```aspnet
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```

> Açıklama için [buraya](https://github.com/philferriere/cocoapi) bakabilirsin.
{% endtab %}

{% tab title="🐧 Linux" %}
```bash
git clone https://github.com/cocodataset/cocoapi.gitcd cocoapi/PythonAPImakecp -r pycocotools /content/models/research/cd ../..rm -rf cocoapi
```
{% endtab %}
{% endtabs %}

## **🏴 Eğitimi Hazırlama ve Başlatma**

Resmi kaynağa ulaşmak için [buraya](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_locally.md) bakabilirsin.

* `model_main.py` eğitim için önerilen dosyadır
* Varsayılan olarak ekrana raporlama yapmaz, yapmasını isterseniz [buraya](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10/issues/184#issuecomment-437811347) bakabilirsiniz

{% tabs %}
{% tab title="👨‍💻 model\_main.py" %}
Bu dosya ile eğitim önerilen eğitim şeklidir.

* `train.py` ile eğitime nazaran, kaldığı yerden devam eder
  * 1000 adım yapıldıysa, ikinci eğitimi 1200 yaptığınızda 200 adım eğitir
  * `train.py` eğitiminde modelin sonucunun ayrılıp, sonuç üzerinden eğitim yapılması gerekir

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

{% hint style="success" %}
Eğitim dosyaları arasında **performans veya kalite farkı yoktur**, kaynak için [buraya](https://github.com/tensorflow/models/issues/6100) bakabilirsin.
{% endhint %}
{% endtab %}

{% tab title="🤺 train.py" %}
```bash
python train.py \
    --logtostderr \
    --train_dir=training/ \
    --pipeline_config_path=training\<yapılandırma_dosyası>
```

* `<yapılandırma_dosyası>` Modelimizin yapılandırma dosyasının tam adı
  * **training** klasörüne attığımız yapılandırma dosyaları
  * _Örn: ssd\_inception\_v2\_coco.config_

{% hint style="warning" %}
Eskimiş olan bir eğitim kodudur, `model_main.py` kod dosyası tensorflow tarafından önerilir.
{% endhint %}
{% endtab %}

{% tab title="⭐ Örnek Çıktı" %}
```bash
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:depth of additional conv before box predictor: 0
INFO:tensorflow:Restoring parameters from ssd_inception_v2_coco/model.ckpt
INFO:tensorflow:Running local_init_op.INFO:tensorflow:Done running local_init_op.
INFO:tensorflow:Starting Session.
INFO:tensorflow:Saving checkpoint to path training\model.ckpt
INFO:tensorflow:Starting Queues.
INFO:tensorflow:global_step/sec: 0INFO:tensorflow:global step 1: loss = 13.8886
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
{% endtab %}
{% endtabs %}

## 🧲 Eğitimi Etkileyen Faktörler

Training times can be affected by a number of factors such as:

* The computational power of you hardware \(either CPU or GPU\): Obviously, the more powerful your PC is, the faster the training process.
* Whether you are using the TensorFlow CPU or GPU variant: In general, even when compared to the best CPUs, almost any GPU graphics card will yield much faster training and detection speeds. As a matter of fact, when I first started I was running TensorFlow on my Intel i7-5930k \(6/12 cores @ 4GHz, 32GB RAM\) and was getting step times of around 12 sec/step, after which I installed TensorFlow GPU and training the very same model -using the same dataset and config files- on a EVGA GTX-770 \(1536 CUDA-cores @ 1GHz, 2GB VRAM\) I was down to 0.9 sec/step!!! A 12-fold increase in speed, using a “low/mid-end” graphics card, when compared to a “mid/high-end” CPU.
* How big the dataset is: The higher the number of images in your dataset, the longer it will take for the model to reach satisfactory levels of detection performance.
* The complexity of the objects you are trying to detect: Obviously, if your objective is to track a black ball over a white background, the model will converge to satisfactory levels of detection pretty quickly. If on the other hand, for example, you wish to detect ships in ports, using Pan-Tilt-Zoom cameras, then training will be a much more challenging and time-consuming process, due to the high variability of the shape and size of ships, combined with a highly dynamic background.
* And many, many, many, more. . . .

## 👀 Eğitim İşlemini TensorBoard Kullanarak Takip Etme

**Anaconda Prompt** üzerinden alttaki komutlar uygulanır:

```text
activate tensorflow_cpu # ya da gputensorboard --logdir=training\
```

Alttaki gibi bir çıktı gelmesi gerekmekte:

```text
TensorBoard 1.6.0 at http://YOUR-PC:6006 (Press CTRL+C to quit)
```

> Çıktıyı görüntülemek için verilen url'i tarayıcına kopyalaman yeterlidir.

## 📃 Sonuç Grafiğini Dışarı Aktarma

**Anaconda Prompt** üzerinden alttaki komutlar uygulanır:

```text
activate tensorflow_cpu # ya da gpu​copy %TENSORFLOW%\models\research\object_detection/export_inference_graph.py %TENSORFLOW%\workspace\example_detection​cd %TENSORFLOW%\workspace\example_detection​python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/<yapılandırma_dosyası> --trained_checkpoint_prefix training/model.ckpt-<checkpoint> --output_directory trained-inference-graphs/output_inference_graph_v1.pb
```

* `<yapılandırma_dosyası>` Modelimizin yapılandırma dosyasının tam adı
  * **training** klasörüne attığımız yapılandırma dosyaları
  * _Örn: ssd\_inception\_v2\_coco.config_
* `<checkpoint>` **example\_detection/training** dizinindeki gösterilmek istenen adımın numarası
  * _Örn: 13302_


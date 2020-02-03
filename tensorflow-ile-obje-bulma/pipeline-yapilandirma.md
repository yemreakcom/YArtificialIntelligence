# 🍢 Pipeline Yapılandırma

## 🔰 Önemli bilgiler

* Tensorflow'un resmi açıklaması için [buraya](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/configuring_jobs.md) tıklayabilirisin

## 🚙 Medellin İndirilmesi ve Gerekli Yere Taşınması

* Tensorflow önceden eğitilmiş modelleri indirmek için [buraya](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md#coco-trained-models-coco-models) tıklayabilirsin
* `.tar.gz` uzantılı olacağı için [winrar](https://www.win-rar.com/download.html?&L=0) ya da [7zip](https://www.7-zip.org/download.html) gibi ek uygulamalarla `buraya çıkart` demen gerekmekte
  * `Klasör'e çıkart` değil `buraya çıkart` diyeceksiniz.

Klasör içinde aynı isimde başka klasör olmasın

```text
# Modelin çıkartıldığı dizindecd <model_ismi>move * %TENSORFLOW%\workspace\example_detection\pre_trained_modelmove saved_model %TENSORFLOW%\workspace\example_detection\pre_trained_modelcd %TENSORFLOW%\workspace\example_detection\pre_trained_model
```

* `<model_ismi>` Seçip, indirdiğiniz `.tar.gz` uzantılı dosyanın adı
  * `TAB` tuşu ile dizindeki dosya adlarını tamamlayabilirsiniz
  * `*.tar.gz` uzantısı yazılmayacak
  * _Örn: ssd\_inception\_v2\_coco\_2018\_01\_28_
  * _Örn: ssd\_mobilenet\_v1\_ppn\_shared\_box\_predictor\_300x300\_coco14\_sync\_2018\_07\_03_

## 📑 Modelin Yapılandırma Dosyaları

Seçtiğiniz modelin `*.config` dosyasını `example_detection/training` klasörü altına kopyalamanız gerekmekte.

```text
mkdir %TENSORFLOW%\workspace\example_detection\training​copy %TENSORFLOW%\models\research\object_detection\samples\configs\<model_ismi>.config %TENSORFLOW%\workspace\example_detection\training
```

* `<model_ismi>` Seçip, indirdiğiniz `.tar.gz` uzantılı dosyanın adı
  * `TAB` tuşu ile dizindeki dosya adlarını tamamlayabilirsiniz
  * `*.tar.gz` uzantısı yazılmayacak
  * Tarih son ekini içermemeli
    * `*_2018_07_03.tar.gz` ise `*.tar.gz` olarak yazılmalı
  * _Örn: ssd\_inception\_v2_
  * _Örn: ssd\_mobilenet\_v1\_ppn\_shared\_box\_predictor\_300x300\_coco14\_sync_

## 👨‍🔧 Modelin Yapılandırma Dosyasını Düzenleme

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


---
description: Tensorflow için hata notları
---

# 🐞 Hata Notları

## 'conda' is not recognized as an internal or external command

`Anaconda Prompt` üzerinden terminal işlemlerinize devam etmeniz durumunda sorun gidecektir.

## '...' is not recognized as an internal or external command

[Gerekli Paketlerin Kurulumları]() tamamlanmadığı için bu hata ile karşılaşıyor olabilirsiniz.

## 'ImportError: No module named' Hataları

PythonPath ayarlanmadığı için bu hata ile karşılaşmaktasınız.

```bash
set PYTHONPATH=%TENSORFLOW%\models\research;%TENSORFLOW%\models\research\slim;%TENSORFLOW%\models\research\object_detection
```

> Dökümandaki ilgili alana yönelmek için [buraya]() tıklayabilrisin.

## 'dict\_keys' object does not support indexing

Açıklama linki için [buraya](https://github.com/tensorflow/models/pull/6044/files) bakabilirsin.

```bash
start %TENSORFLOW%\models\research\object_detection\models\feature_map_generators.py
```

* Satır 518'deki yere alttaki kodu yapıştırın

```python
image_features = image_features[list(image_features.keys())[0]]
```

## Object was never used \(type \)

> Yakında..

## 'unicodeescape' codec can't decode bytes in position

Modelinizin `.config` dosyanıza yazdığın tam yol verilerinde `\` yerine `/` veya `\\` kullanmalısınız.

## Allocation of X exceeds 10% of system memory

* Rastgeldiğim bu [kaynağa](https://github.com/tensorflow/tensorflow/issues/18736#issuecomment-385976699) göre **ssd\_mobilenet\_v2\_coco modeline** özgü bir hatadır.
* Hatanın çözüm kaynağı için [buraya](https://github.com/tensorflow/tensorflow/issues/18736#issuecomment-388709455) tıklayabilirsin

## google.protobuf.text\_format.ParseError, Expected string but found

Config dosyalarının text editör üzerinden düzenlemesi durumunda, türkçe karakterler için text editörü yapıyı değiştirmekte ve tensorflow bunu algılayamamaktadır. Sorunu çözmek için alttakiler yardımıyla `.config` dosyasını düzenleyin:

* VsCode
* Notepad++
* Sublime
* Atom

> Harici kaynak için [buraya](https://github.com/tensorflow/models/issues/1897#issuecomment-313879598) bakabilirsin.

## Value Error: No Variable to Save

Model eğitimi yapıldığı sırada gelen bir hatadır, çözümü için `.config`dosyanızı bu şekilde düzenleyin:

```text
train_config: {
  ...
  fine_tune_checkpoint: "./pre_trained_model/model.ckpt"
  fine_tune_checkpoint_type:  "detection"
  ...
}
```

> `ssd_mobilenet_v1_quantized_300x300_coco14_sync` modelinde test edilmiştir.


---
description: >-
  Anadonca (Miniconda) ve Tensorflow uygulamalarının kurulumu, kurulum sonucunu
  test etme ve birlikte çalıştırma
---

# 🚧 Tensorflow Kurulumu

## 💘 Önemli Hususlar

* 📈 Tensorflow anaconda üzerinden daha sağlıklı, taşınabilir ve verimli çalışabilmekte
* 👮‍♂️ Anaconda'nın sanal ortamları, paketlerin çakışmasını engelleyecektir
* 👀 Anaconda'nın Tensorflow'daki avantajı için [buraya](https://www.anaconda.com/tensorflow-in-anaconda/) göz atabilirsin.

## 💚 Anaconda Kurulumu

{% embed url="https://python.yemreak.com/anaconda/anacondaya-giris" caption="" %}

## 💛 Tensorflow CPU veya GPU Kurulumu

* 💁‍♂️ Bu kurulum CPU kurulumu olarak da geçmekte
* 💨 GPU kurulumu CPU'ya nazaran oldukça hızlı eğitim seçeneği sağlar
* 📢 GPU kurulumu için gereksinimleri sağlıyorsanız GPU kurulumu \(tensorflow-gpu\) yapmanız tavsiye edilir

### 🚧 Sanal Ortam Oluşturma ve Üzerine Kurma

```bash
conda create -n tensorflow tensorflow # CPU kurulumu
conda create -n tensorflow tensorflow-gpu # GPU kurulumu
```

## ✅ Kurulumu Test Etme

Alttaki komut ile 'Hello, TensorFlow!' çıktısını almanız gerekmektedir.

```python
python -c
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
>>> print(sess.run(hello))
```


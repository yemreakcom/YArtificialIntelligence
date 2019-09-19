# 12. Kapanış

## Gereklilikler

* Test edilmesi için gereken uygulamayı [buradan](https://github.com/yedehrab/self-driving-car-sim) indirmelisin (*Authonomus Mode'da çalışır*)
* Tüm gereklilikleri kurmak için [buradaki](./requirement.bat) `requirement.bat` dosyasını çalıştırman lazım.

## Ortam oluşturulması

```bash
conda create --name <ortam_ismi>
conda activate <ortam_ismi>
```

**Örnek ortam oluşturma:**

```bash
 conda create --name myenv
 conda activate myenv
 ```

 > VScode için; sol alt kısımdan kullanılacak ortamın python derleyicisini seçmeyi unutmayın!

## Ortam Yüklemeleri

```bash
conda install -c anaconda flask
conda install -c conda-forge python-socketio
conda install -c conda-forge eventlet
conda install -c conda-forge tensorflow
conda install -c conda-forge keras
conda install -c anaconda pillow
conda install -c anaconda numpy
conda install -c conda-forge opencv
```

> Keras üzerinden Tensorflow alt yapısını kullanmamız gerkemekte. (*Sadece farklı bir altyapı kullanılıyorsa bunu yazın*)

```bash
set KERAS_BACKEND=tensorflow
```

## Kopyala & Yapıştır

İster not defterine ekleyip uzantısını `bat` yaparak, ister direkt `CMD`ye kopyalarak çalıştırabilirsin.

```bash
conda create --name myenv
y
conda activate myen
conda install -c anaconda flask
y
conda install -c conda-forge python-socketio
y
conda install -c conda-forge eventlet
y
conda install -c conda-forge tensorflow
y
conda install -c conda-forge keras
y
conda install -c anaconda pillow
y
conda install -c anaconda numpy
y
conda install -c conda-forge opencv
y
set KERAS_BACKEND=tensorflow
```

## Loss Grafiği

![loss](../kaynaklar/final-loss.png)

<!--Index-->

## 📂 Harici Dosyalar

- [Behavioral_Clonning.ipynb](./Behavioral_Clonning.ipynb)
- [drive.py](./drive.py)
- [genereted-udacity-simulated-model.h5](./genereted-udacity-simulated-model.h5)
- [requirement.bat](./requirement.bat)

<!--Index-->

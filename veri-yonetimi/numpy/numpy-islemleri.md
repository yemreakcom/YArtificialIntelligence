# 👷‍♂️ Numpy İşlemleri

## 🧱 Temel İşlemler <a id="numpy-islemleri"></a>

Tüm işlemler `nparray` objesinin alt metotlarıdır.

* Tüm operatör işlemlerini \(`+`, `/` ...\) destekler

| Alt metodlar | Açıklama |
| :--- | :--- |
| `<ndarray>.sum()` | Elemanları toplama |
| `<ndarray>.sum(axis=<int>` | Eksendeki elemanları toplama \(_0 = dikey 1 = yatay_\) |
| `<ndarray>.mean()` | Ortalama |
| `np.dot(<ndarray>, <ndarray>)` | Inner product \(_iç çarpım = x1.y1 + x2.y2 ..._ \) |
| `np.outher(<ndarray>, <ndarray>)` | Outher product \(_matrix çarpımı_\) |

## Boyut İşlemleri <a id="boyut-islemleri"></a>

```python
mat = np.random.rand(20, 10)mat.reshape(40, 5).shape # (40, 5)mat.reshape(30, 5) # Hata verir 200 öğe (30, 5)'e ayrılamazmat.ravel().shape # Düzleştirme (200,)mat.transpose().shape # (10, 20)
```

## Dizileri Birleştirme <a id="dizileri-birlestirme"></a>

```python
print(a) # [1 2 3 4 5]print(b) # [2 3 4 5 6]​np.hstack((a, b))# array([1, 2, 3, 4, 5, 2, 3, 4, 5, 6])​np.vstack((a, b))# array([[1, 2, 3, 4, 5],#       [2, 3, 4, 5, 6]])​np.dstack((a, b))# array([[[1, 2],#        [2, 3],#        [3, 4],#        [4, 5],#        [5, 6]]])
```

## Numpy Hızlı Notlar <a id="numpy-hizli-notlar"></a>

```python
a_slice_prev = a_prev[0:2,0:2,:]​(m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape(f, f, n_C_prev, n_C) = W.shape​for a in depth:    W = W[..., a]
```

### Resim İşleme <a id="resim-isleme"></a>

```python
fname = "images/thumbs_up.jpg"image = np.array(ndimage.imread(fname, flatten=False))my_image = scipy.misc.imresize(image, size=(64,64))plt.imshow(my_image)
```

## 💫 Numpy Değişken Dönüşümü <a id="numpy-degisken-doenuesuemue"></a>

| Metod | Açıklama |
| :--- | :--- |
| `dtype` | Değişken tipi |
| `astype(<dtype>)` | Tip değiştirme |

```python
np.logspace(1, 10, 10).dtype # float64np.logspace(1, 10, 10).astype(int).dtype # int64
```

##  <a id="numpy-islemleri"></a>


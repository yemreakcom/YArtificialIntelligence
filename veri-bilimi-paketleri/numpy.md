# 🔢 NumPy

## ❔ NumPy Nedir <a id="numpy-nedir"></a>

* Matematiksel fonksiyonlara odaklanır \(_sin log floor_\)
* `random` paketinin geliştirilmiş halidir
* `ndarray` ile matrix yapısı sunar

## 💖 NumPy Avantajları <a id="numpy-avantajlari"></a>

* **Çok hızlı** işlem yapar
  * `list` üzerindeki işlemlerde her bir objenin tipine bakılır
  * `ndarray`'da tipler belli olduğundan bakılmadan işleme sokulur

## 🚅 NumPy `ndarray` <a id="numpy-ndarray"></a>

Sırasıyla 1D ve 2D `ndarray` yapısı:

* Dikdörtgen olanları matrix'e çevirir
  * `(3, 3)`, `(5, 3)`, boyutları dikdörtgen ifade eder
* Olmayanları `(x, )` boyutlu objelere çevirir
  * Birden fazla farklı öğe olduğundan obje olarak işlenir

$$
[x_1, x_2, x_3, x_4] \begin{bmatrix} x_{11} & x_{12} & ... \end{bmatrix}
$$

```python
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
an_array = np.array(list_of_lists)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [[1 2 3] [4 5 6] [7 8 9]]

non_rectangular = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
non_rectangular_array = np.array(non_rectangular)
# [[1, 2], [3, 4, 5], [6, 7, 8, 9]] [list([1, 2]) list([3, 4, 5]) list([6, 7, 8, 9])] 

print(an_array.shape, an_array.dtype) # (3, 3) int64 
print(non_rectangular_array.shape, non_rectangular_array.dtype) # (3,) object
```

## ✨ Numpy'da `ndarray` Oluşturma <a id="numpyda-ndarray-olusturma"></a>

| Metod | Açıklama | Örnek |
| :--- | :--- | :--- |
| `np.arange(1, 10, 2)` | `1` den `10` a kadar `4`er `4`er artar | `array([1, 5, 9])` |
| `np.linspace(2, 10, 3)` | `1` ile `10` arasını `3`parçaya böler | `array([ 2., 6., 10.])` |
| `np.logspace(2, 10, 2)` | Logaritmik | `array([1.e+02, 1.e+10])` |
| `np.zeros(3)` | `3` tane sıfır | `array([0., 0., 0.])` |
| `np.diag([1,2,3,4])` | `(4, 4)` Diagonel matrix | ​ |
| `np.eye(5)` | `(5, 5)` Birim matrix | ​ |

Diagonel ve birim matrix \`\`\`py \# Diagonel array\(\[\[1, 0, 0, 0\], \[0, 2, 0, 0\], \[0, 0, 3, 0\], \[0, 0, 0, 4\]\]\) \# Birim array\(\[\[1., 0., 0., 0., 0.\], \[0., 1., 0., 0., 0.\], \[0., 0., 1., 0., 0.\], \[0., 0., 0., 1., 0.\], \[0., 0., 0., 0., 1.\]\]\) \`\`\`

## 💫 Numpy Değişken Dönüşümü <a id="numpy-degisken-doenuesuemue"></a>

| Metod | Açıklama |
| :--- | :--- |
| `dtype` | Değişken tipi |
| `astype(<dtype>)` | Tip değiştirme |

```python
np.logspace(1, 10, 10).dtype # float64np.logspace(1, 10, 10).astype(int).dtype # int64
```

## 👷‍♂️ Numpy İşlemleri <a id="numpy-islemleri"></a>

Tüm işlemler `nparray` objesinin alt metodlarıdır

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


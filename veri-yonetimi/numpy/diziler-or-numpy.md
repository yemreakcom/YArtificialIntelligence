# 🚅 Diziler \| Numpy

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

## 🧮 Diagonel ve birim matrix

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Diagonel

array([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]])

# Birim

array([[1., 0., 0., 0., 0.], [0., 1., 0., 0., 0.], [0., 0., 1., 0.,
      0.], [0., 0., 0., 1., 0.], [0., 0., 0., 0., 1.]])
```


# 🥴 Karışık Notlar

## Matrix İşlemleri

> `A, B, C` gibi semboller matrix belirtir.

```python
1e-7 == 0.0000001 # True (10 ^ -7)
1e+4 == 1000 # True (10^4)

A = (A < 5) # 5'ten küçük ise true
np.mean(A) # Ortalama A'nın değeri (true ya da false)

A = A[A > 5] # 5 ten büyük olanları alma

# Maskeleme (5'ten küçük olanlar sıfırlanır)
A = np.multiply(A, A < 5)
```

## Jupyter Notları

* ALT'a basılı tutarak sütun seçimi yapabilirsin
* ALT GR'e basılı tutarak birden fazla imleç ekleyebilirsin
* SHIFT'e basılı tutarak yön tuşları ile metin seçimi yapabilrisin

## Temel Özellikleri

* Matematiksel \(vektör tabanlı\) işlemler için kaçınılmazdır
* Python için SIML \(single instruction multiple ...\) yapısını kullanır
* Single thread değil multi thread çalışır. \(multiprogramming\)
* Optimize edilmiştir ve `for` döngülerinden 300 kata kadar daha hızlıdır

## Temel Fonksiyonlar

```python
import numpy as np

np.sum(<V>, <V>) # Vektörel toplama
np.dot(<V>, <V>) # Vektörel çarpma
np.exp(<V>, <V>) # Vektörel e^
np.log(<V>, <V>) # Vektörel log
np.max(<V>, <V>) # Vektörel en yüksek değeri bulma
np.min(<V>, <V>) # Vektörel min değeri bulma
np.mean(<V>) # Vektörel ortalama alma
np.where(<koşul>, <true>, <false>) # Vektörel If-else
```

## IF-Else Yapısı

### One IF-ELIF

**Approach \#1** One approach:

```python
keep_mask = X==50
out = np.where(X>50,0,1)
out[keep_mask] = 50
```

**Approach \#2** Alternatively, for in-situ edit:

```python
replace_mask = X!=50
X[replace_mask] = np.where(X>50,0,1)[replace_mask]
# Or (X<=50).astype(int) in place of np.where(X>50,0,1)
```

**Code-golf?** If you actually want to play code-golf/one-liner:

```python
(X<=50)+(X==50)*49
```

### Multiple IF-ELIFs

**Approach \#1:**

For a bit more generic case involving more if-elif parts, we could make use of [`np.searchsorted`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.searchsorted.html) -

```python
out_X = np.where(X<=40,0, np.searchsorted([40,50,60,70,80,90], X)+3)
```

> [Kaynak](https://stackoverflow.com/a/45768290/9770490)

## Harici Kaynaklar

* [Numpy için If-Else yapısı](https://stackoverflow.com/a/45768290/9770490)


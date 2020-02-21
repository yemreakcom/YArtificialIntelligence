---
description: NumPy veri formatı ve onları işleme
---

# 🔢 NumPy \| Veri Bilimi

## 💎 Dosya Formatı \(`numpy`\)

* Makine öğrenimin oldukça kullanılan bir pakettir
* Kendisine özel basit kullanımlı dosya işlemleri vardır
* Dosya uzantısı `npy` şeklindedir

## 💠 NumPy Metodları

| Metod | Açıklama |
| :--- | :--- |
| `savetxt(<file.txt>, <obj>)` | Metni dosyaya **text** formatında kaydetme |
| `save(<file.npy>, <obj>)` | Metni dosyaya **binary** formatında kaydetme |
| `obj = loadtxt(<file.txt>)` | Dosyadan **text** formatındaki metni okuma |
| `obj = load(<file.npy>)` | Dosyadan **binary** formatındaki metni okuma |

## 🧃 Numpy Objesi

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
sample_array = np.random.random((4, 4)) 

# [[0.02573499 0.82494109 0.89756743 0.84206605]
# [0.70146385 0.1468585 0.45772617 0.23692087]
# [0.005141 0.22425271 0.29602516 0.64871444]
# [0.15156162 0.46722448 0.37752783 0.10490116]]		
```

Numpy objesi örneği \`\`\`python sample\_array = np.random.random\(\(4, 4\)\) \# \[\[0.02573499 0.82494109 0.89756743 0.84206605\] \# \[0.70146385 0.1468585 0.45772617 0.23692087\] \# \[0.005141 0.22425271 0.29602516 0.64871444\] \# \[0.15156162 0.46722448 0.37752783 0.10490116\]\] \`\`\`

## 💾 Numpy Kaydetme

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Metin olarak kaydetme (verimsiz)
np.savetxt('./data/sample_array.txt', sample_array)
# ./data/sample_array.txt 2.573499304710569202e-02 8.249410915227861629e-01 8.975674256604490031e-01 8.420660467417920847e-01 7.014638530667735017e-01 1.468584962112742254e-01 4.577261675584743950e-01 2.369208677107362826e-01 5.140998044749989226e-03 2.242527110614195296e-01 2.960251573689319793e-01 6.487144382421085043e-01 1.515616208846672919e-01 4.672244790863220310e-01 3.775278308063384491e-01 1.049011560631800677e-01

# Binary olarak kaydetme (Verimli)
np.save('./data/sample_array.npy', sample_array) ``` ```bash
# ./data/sample_array.npy NUMPYv{'descr': '
```

## 👀 Numpy Okuma

```python
# Metin olarak kaydetme (verimsiz)
print(np.loadtxt('./data/sample_array.txt'))

# Binary olarak kaydetme (Verimli)
print(np.load('./data/sample_array.npy'))

 # Her iki kullanım için de aynıdır
```


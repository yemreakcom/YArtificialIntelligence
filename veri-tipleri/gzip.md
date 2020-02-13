# 📚  Sıkıştırılmış Veriler

## 💎 Sıkıştırılmış Veri Formatı \(`gzip`\)

* Çok sık kullanılan sıkıştırma tipidir
* [deflate algorithm](http://www.infinitepartitions.com/art001.html) yöntemini kullanır
  * `10, 10, 10, 2, 3, 3, 3, 3, 3, 50, 50, 1, 1, 50, 10, 10, 10, 10` \(18 sayı\) yerine
  * `(3, 10), (1, 2), (5, 3), (2, 50), (2, 1), (1, 50), (4, 10)` \(14 sayı\) yazılır
  * 3 tane 10, 1 tane 2, 5 tane 3 ...
* Düşük verili dosyalarda verimli çalışmaz 😢
  * Başlık bilgisi fazladan yer kaplar
  * Sıkıştırma algoritması için çok fazla tekrarlı bitler gerekir
* Sade metin yerine kodlanmış metin barındırır
* Dosya işlemlerinde `w` değil `wb` kullanılır

> `w` plaint text, `wb` binary text şeklinde yazar

## 💠 Gzip Metodları

| Metod | Açıklama |
| :--- | :--- |
| `gzip.open(<dosya>, <erişim modu>)` | Dosyaya erişim |

## ⭐ Gzip Örnekleri

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
with gzip.open('./data/short_text.txt.gz', 'wb') as f:
    f.write(short_text.encode('utf-8'))

```


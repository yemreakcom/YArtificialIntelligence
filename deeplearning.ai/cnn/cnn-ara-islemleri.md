# 🍟 CNN Ara İşlemleri

## 🐛 Convolution İşlemlerindeki Sorunlar

* Kenarlardaki pikseller çok az kullanılır
  * Her pixel filtrenin merkezine gelemiyor
* Resmin boyutu küçülür

## Padding

* Kenarlara fazladan satır eklenir
* Satırların pixel değerleri `0` olur
* `padding = p` ise `p=1` için 0 değerler kenar eklenir
  * 4 kenar olduğundan 4 satır

## Convolution Türleri

| Özellik | Açıklama | Girdi | Çıktı boyutu |
| :--- | :--- | :--- | :--- |
| Valid | _Padding_ olmadan işlem yapılır \) | $n$ | $n - f + 1$ |
| Same | _Padding_ işlemini kulalnara boyutu koruma | $n + 2p$ | $n$ |
| Stripe | _Stripe_ işlemi ile adım sayısını belirleme | $n + 2p$ | $\(n + 2p + f\) / s + 1$ |

> $p = \(f - 1\) / 2$ için çıktı değeri korunur.

| Harf | Temsil ettiği boyut |
| :--- | :--- |
| $$n $$ | Resim |
| $$f$$  | Filtre |
| $$p$$  | Padding |
| $$s$$  | Stripe |

## Stride

* Her adımda kaç birim ilerleneceğini belirtir

![](../../.gitbook/assets/image%20%2812%29.png)

## 3D \(Renkli Resimler\) için Convolution

* Renkli resimlerin derinlik \(_"depth", "channel"_\) değeri 3'tür
  * `n x n x d`,`64 x 64 x 3`
* Filtre de **3D** olmak zorundadır
  * RGB için ayrı filterler
  * Toplamda 3 filtre olduğundan `f x f x 3` boyutlu olur
* Çıktı değeri hala **2D** olarak kalır

![](../../.gitbook/assets/image%20%2821%29.png)

### Çoklu Filtre Kullanımı

* Her özellik için ayrı bir filtre kullanılır
* Sonrasın tüm filtreler birleştirilir
* `f x f x filtre çeşidi`, `4x4x2`

### Tek katmanlı CNN Mimarisi

| Değer | Karşılığı |
| :--- | :--- |
| $a ^ {\[0\]}  = X$ | Resim |
| $W$ | Filtreye değerleri |
| $b$ | Filtreye eklenen sabit sayı |
| $Z$ | İşlenmiş filtre \($W.X + b$\) |
| $g\(Z\)$ | Aktivasyon \(_ReLU_ ...\) |
| $a ^ {\[l\]}$ | Son filtrelenmiş çıktı |

![](../../.gitbook/assets/image%20%2833%29.png)


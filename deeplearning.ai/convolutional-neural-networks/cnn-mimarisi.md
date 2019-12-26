# 💒 CNN Mimarisi

## CNN Notasyonu

![](../../.gitbook/assets/image%20%2829%29.png)

## ConvNet

Convolutional Neural Network yerine bu kısaltılmış ad kullanılmakta

### ConvNet Hyperparametreleri

| Parametre | Terim | Açıklama |
| :--- | :--- | :--- |
| $f$ | Filter | Filtre boyutu |
| $s$ | Stride | Adım sayısı |
| $p$ | Padding | Doldurma miktarı |
| $n\_{filter}$ | \# of filter | Filtre sayısı |

## ConvNet Örneği

![](../../.gitbook/assets/image%20%289%29.png)

## Pooling Layer

Çok derin ağlarda `avg pooling` diğerlerinde `max pooling` kullanılır

| Pooling | Açıklama |
| :--- | :--- |
| Max Pooling | En büyük pixel değerini alır |
| Avarage Pooling | Pixellerin ortalamasını alır |

### Max Pooling

* En belirgiin özellikleri ortaya çıkarır
* Filtredeki en büyük pixeli alır
* Öğrenme olmaz, sadece işlem hızını etkiler
  * Parametre ve _gradient descent_ yok
  * Sadece hyperparametreler var

> ⚠ Neden iyi çalıştığına dair net bir sebep bilinmiyor.

![](../../.gitbook/assets/image%20%2815%29.png)

## Neural Network Örneği

* Parametrelerin \(`w`, `b`\) olmadığı alanlar katman olarak sayılmaz
  * Pooling alanları bir öncesindeki CONV ile ortak katman olarak ele alınır

![](../../.gitbook/assets/image%20%2838%29.png)

### NN'de Katman Tablosu

* _Activation size_ ilerledikçe azalır
  * Convolutional işlemlerinin başladığı `CONV1` katmanında başlayarak azalır
* Çok hızlı azalırsa model verimli çalışmaz

![](../../.gitbook/assets/image%20%2839%29.png)

## Matematiksel Notasyon

* Superscript $\[l\]$ denotes an object of the $l^{th}$ layer.
  * Example: $a^{\[4\]}$ is the $4^{th}$ layer activation. $W^{\[5\]}$ and $b^{\[5\]}$ are the $5^{th}$ layer parameters.
* Superscript $\(i\)$ denotes an object from the $i^{th}$ example.
  * Example: $x^{\(i\)}$ is the $i^{th}$ training example input.
* Lowerscript $i$ denotes the $i^{th}$ entry of a vector.
  * Example: $a^{\[l\]}\_i$ denotes the $i^{th}$ entry of the activations in layer $l$, assuming this is a fully connected \(FC\) layer.
* $n\_H$, $n\_W$ and $n\_C$ denote respectively the height, width and number of channels of a given layer. If you want to reference a specific layer $l$, you can also write $n\_H^{\[l\]}$, $n\_W^{\[l\]}$, $n\_C^{\[l\]}$.
* $n_{H_{prev}}$, $n_{W_{prev}}$ and $n_{C_{prev}}$ denote respectively the height, width and number of channels of the previous layer. If referencing a specific layer $l$, this could also be denoted $n\_H^{\[l-1\]}$, $n\_W^{\[l-1\]}$, $n\_C^{\[l-1\]}$.


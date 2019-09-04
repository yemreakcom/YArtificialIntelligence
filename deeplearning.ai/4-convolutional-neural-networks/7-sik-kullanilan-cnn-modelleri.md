# 7 - Sık Kullanılan CNN Modelleri

## ResNet \(Resudial Network\)

* Aktivasyon sonucu diğer katmana aktarır ve ekler. \(`+`\)
* $a^{\[l+2\]} = g\(Z^{\[l+2\]} + a^{\[l\]}\)$
* Bu yapı sayesinde çok katmanlı veriler oluşturulabiliyor
* Başlarda verilerin etkisinin çok azalması engellenir \(_"vanishing / exploding gradient"_\)

![](../../.gitbook/assets/resnet_ex.png)

&lt;/details&gt;

### Neden ResNet

* Derinlere indikçe sinir ağı aşınır
* Öğrenme ve gelişme sürecinde kayıplara uğrar
* Düz yapıda \(_plain net_\):
  * $a\_l$ değerlerinin parametreleri \(`w`, `b`\) 0'a yaklaşır
  * $a^{\[l+1\]} = g\(W^{\[l\]} \times a^{\[l\]} + b\_l\)$ formülü $W=0$ için $0$ olur, yani **ölür**
  * Gradyanlar çalışmaz hale gelir \(_no gradient descent_\)
* ResNet yapısında:
  * $a^{\[l+2\]} = g\(Z^{\[l+2\]} + a\_l\)$ ve $Z^{\[l+2\]} = g\(W^{\[l+2\]} \times a^{\[l+1\]} + b^{\[l+2\]}\)$
  * $W=0$ için $a\_l$ değeri aktarılır \(eski aktivasyon sonucu kullanılır\)
  * Sinir ağını etkilemesine izin verilmez

### Eğitim Grafiği \(Loss\)

![](../../.gitbook/assets/resnet_vs_plain.png)

### ResNet vs PlainNet

![](../../.gitbook/assets/resnet_vs_paint_nn.png)

### ResNet için Önemli Husular

$\(Conv \times 3 \rArr Pool\) \rArr ... \rArr \(Conv \times 3 \rArr Pool\) \rArr Softmax$

* CNN için **"some"** padding yapısı tercih edilir
  * Boyutun değişmesini engellemek için seçilir
  * $dim\(a^{\[l\]}\) = dim\(a^{\[l+2\]}\)$ olmak zorundadır ki matrix ataması gerçekleşebilsin
    * $dim\(..\)$ Boyut'u anlamına gelmektedir
* Some padding yerine **"vali"** kullanılırsa
  * Boyutlar eşit olmayacağından ekstra bir hyperparam \($W\_s$\) ile çarpılarak, boyutlar eşitlenir
  * $a^{\[l+2\]} = W\_s \times a^{\[ l\]}$
    * $dim\(W_s\) = \(a^{\[l+2\]}, a_{a}\)$

## 1 x 1 Convolutional Nedir ve Neden Yapılır

> Network in network olarak da bilinir.

* Temel amacı boyutu sıkıştırmak ve küçültmekdir. 
  * $n\_c$ değerini küçültmek için kullanılır
  * $n\_c \rArr n\_f$ , $n\_f$ = Filtre sayısı
* Sıkıştırılmış verinin olduğu katmana **bottleneck layer** denir
  * Şişenin dar kısmına verilen isim, bu katman CNN'in ufak kısmını ele alır

    ![](../../.gitbook/assets/pic_bottleneck.png) 
* Bazı ağlarda hesaplamadan tasarruf edilir
* 1 x 1 filtreye sokulup ardından ReLU'ya sokulma işlemidir
  * Aynı derinlik hizasında olanlar toplanır ve öyle aktarılır
* Eğer filtre ile kanal aynı ise katamana _non-linerity_ \(doğrusalsızlık\) özelliği eklenir

![](../../.gitbook/assets/ex_1x1_conv.png) ![](../../.gitbook/assets/1x1_conv_drop_comp.png)

## Inception Network

* 1x1 Convolution'dan oluşan bir sürü Inception Module'den oluşur

![](../../.gitbook/assets/inception_module.png) ![](../../.gitbook/assets/inception_network.png)


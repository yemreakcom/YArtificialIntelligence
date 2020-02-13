# 📈 Matplotlib \| Veri Yönetimi

## 🔰 Ne İşe Yarar <a id="nedir"></a>

* Grafiksel çizim işlemlerine odaklanır.
* Grafik çizimleri ve gösterimler için kullanılan pakettir
* Sıklıkla `import matplotlib.pyplot as plt` şeklinde dahil edilir

## ✨ Grafik Oluşturma <a id="grafik-olusturma"></a>

| Metod | Açıklama |
| :--- | :--- |
| `plot(<list_val>)` | Listeyi grafiğe çizme |
| `title(<str_name>)` | Grafiğin başlığı |
| `xlabel(<str_name>)` | Grafiğin x kısmına yazılacak yazı |
| `ylabel(<str_name>)` | Grafiğin y kısmına yazılacak yazı |
| `legend(<list_names>)` | Grafikdeki çizimlerin isimleri |

## 💞 Birden Fazla Grafik İşlemleri <a id="birden-fazla-grafik-islemleri"></a>

* Çoklu grafikler için `figure` tanımı kullanılır
* Genel kullanım formatı `fig = plt.figure(figsize=(<width>, <height>))`

| Metod | Açıklama |
| :--- | :--- |
| `fig.suptitle(<str_title>)` | Tüm grafiklerin başlığı |
| `ax = plt.subplot(<row>, <col>, <index>)` | Alt grafik oluşturma |
| `ax.hist(<str_name>)` | Histogram \(dikdörtgen gösterim\) grafiği çizdirme |
| `ax.scatter(<list_val1>, <list_val2>, label='<str_name>')` | Noktasal grafik çizdirme |
| `ax.set_xlabel(<str_name>)` | Alt grafiğin x kısmına yazılacak yazı |
| `ax.set_ylabel(<str_name>)` | Alt grafiğin y kısmına yazılacak yazı |

## ❣️ Noktasal Grafiğe Çizgi Çizdirme

```text
from scipy.stats import linregress​fit_line = linregress(shoes, jerseys)ax3.plot(shoes, fit_line[1] + fit_line[0] * shoes, 'r', label='Line of best fit')
```

## 🔗 Faydalı Kaynaklar

* ​[Matplotlib Çizgi Çizimleri](https://matplotlib.org/3.1.1/tutorials/intermediate/legend_guide.html)​

[  
](https://ds.yemreak.com/kisisel-notlar/1.2.2-pandas)


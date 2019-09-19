# Çalışma Alanı

Düzgün ve verimli çalışmak için buradaki yapıyı kullanmanız önerilir.

## Temel Yapı

```txt
+ addons
+ docs
+ models
+ scripts
+ workspace
    + example_detection
        + data
        + models
            + <model_ismi>
                + eval
                + train
                - *.config
                ...
            + <model_ismi>
                + eval
                + train
                - *.config
                ...
            ...
        ...
    + example2_detection
        + data
        + models
            + <model_ismi>
                + eval
                + train
                - *.config
                ...
            + <model_ismi>
                + eval
                + train
                - *.config
                ...
            ...
        ...
    ...
```

| Dizin     | Açıklama                           |
| --------- | ---------------------------------- |
| addons    | LabelImg vs.                       |
| docs      | Dökümanlar                         |
| models    | Tensorflow Models dosyası          |
| scripts   | Kullanacağınız ortak kod parçaları |
| workspace | Çalışma Alanı                      |

### Çalışma Alanı Yapısı

```txt
+ workspace
    + example_detection
        + data
        + models
        ...
    + example2_detection
        + data
        + models
        ...
    ...
```

| Dizin | Açıklama                                                                      |
| ----- | ----------------------------------------------------------------------------- |
| data  | Eğitime katılacak verileri (*eval.record, train.record, label_map*) içeririr. |
| model | Eğitilecek modellerin dosyalarını içerir.                                     |

#### Data Dizini Yapısı

```txt
+ example_detection
    + data
        - label_map.pbtxt
        - eval.record
        - train.record
    + models
    ...
...
```

| Dosya             | Açıklama                                                  |
| ----------------- | --------------------------------------------------------- |
| `label_map.pbtxt` | Etiket haritası dosyası                                   |
| `eval.record`     | Test için kullanılacak tensorflow kayıtları (TF record)   |
| `train.record`    | Eğitim için kullanılacak tensorflow kayıtları (TF record) |

#### Models Dizini Yapısı

```txt
+ example_detection
    + data
    + models
        + <model_ismi>
            + eval
            + train
            - *.config
            ...
        + <model_ismi>
            + eval
            + train
            - *.config
            ...
        ...
    ...
...
```

Her bir model için ayrı dizinler oluşturulur.

| İsim      | Tipi  | Açıklama                        |
| --------- | ----- | ------------------------------- |
| eval      | Dizin | Test sonuçları burada tutulur.  |
| train     | Dizin | Eğitim çıktıları burada tutulur |
| `.config` | Dosya | Yapılandırma dosyası            |

## Kayıtların Oluşturulması

- **Resim** verileri toplanır veya çekilir.
- Toplanan resimler `labelimg` yardımıyla etiketlenir ve `.xml` uzantılı dosyaları oluşturulur.
- `images` dizinine **resimler** ve onlara ait **xml** dosyaları %80'i train %20'i eval olacak şekilde klasörlere ayrılarak yerleştirilir.
- `scripts/preprocessing` dizindeki `xml_path_regulator.py` scripti aracılığıyla xml ve resimlerde yol sorunları düzeltilir, veriler yeniden adlandırılır.
- `scripts/preprocessing` dizindeki `xml_to_csv.py` scripti aracılığıyla veriler `.csv` uzantılı tablosal bir dosyaya dönüştürülür.
- Oluşturulan **csv** dosyasında resimlerin etiketlerine göre sayıları [tablo](#Excel%20ile%20Tablo%20G%C3%B6sterimi) olarak gösterilir. (Excel yardımıyla)
- Verilerde denge durumunun (her veriden yaklaşık olarak aynı sayıda varsa) kontrolü yapılır.
- Her çeşit veri için bir `id` belirtilecek şekilde `label_map.pbtxt` adlı etiket haritası oluşturulur
- Oluşturulan **csv**, **etiket haritası** ve **resim** verileri `scripts/preprocessing` dizindeki `generate_tfrecord.py` scripti aracılığıyla veriler `.record` uzantılı kayıtlara dönüştürülür.
- Seçilen modele özgü yapılandırma dosyası indirilir.
- Yapılandırma dosyası olan `*.config` dosyasındaki `PATH_TO_CONFIGURED` olarak işaretlenen alanlar, `num_classes`, `num_examples` ve `batch_size` değerleri güncellenir.

## Eğitimin Başlatılması

- [ ] TODO

## Harici Bilgiler

### Excel ile Tablo Gösterimi

![csv](../../res/csv_table.jpg)

# Hızlı Notlar

## Temel Yapı

```sh
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

## Kayıtların Oluşturulması

- **Resim** verileri toplanır veya çekilir.
- Toplanan resimler `labelimg` yardımıyla etiketlenir ve `.xml` uzantılı dosyaları oluşturulur.
- `images` dizinine **resimler** ve onlara ait **xml** dosyaları %80'i test %20'i test olacak şekilde klasörlere ayrılarak yerleştirilir.
- `scripts/preprocessing` dizindeki `xml_path_regulator.py` scripti aracılığıyla xml ve resimlerde yol sorunları düzeltilir, veriler yeniden adlandırılır.
- `scripts/preprocessing` dizindeki `xml_to_csv.py` scripti aracılığıyla veriler `.csv` uzantılı tablosal bir dosyaya dönüştürülür.
- Oluşturulan **csv** dosyasında resimlerin etiketlerine göre sayıları [tablo](#Excel%20ile%20Tablo%20G%C3%B6sterimi) olarak gösterilir. (Excel yardımıyla)
- Verilerde denge durumunun (her veriden yaklaşık olarak aynı sayıda varsa) kontrolü yapılır.
- Her çeşit veri için bir `id` belirtilecek şekilde `label_map.pbtxt` adlı etiket haritası oluşturulur
- Oluşturulan **csv**, **etiket haritası** ve **resim** verileri `scripts/preprocessing` dizindeki `generate_tfrecord.py` scripti aracılığıyla veriler `.record` uzantılı kayıtlara dönüştürülür.
- Seçilen modele özgü yapılandırma dosyası indirilir.
- Yapılandırma dosyası olan `*.config` dosyasındaki `PATH_TO_CONFIGURED` olarak işaretlenen alanlar, `num_classes`, `num_examples` ve `batch_size` değerleri güncellenir.
- `num_examples` test dizindeki resim sayısıdır (toplam class sayısı değil)

### Excel ile Tablo Gösterimi

![csv](res\csv_table.jpg)
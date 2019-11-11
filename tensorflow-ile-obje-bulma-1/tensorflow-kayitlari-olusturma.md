# 📃 Tensorflow Kayıtları Oluşturma

## 👣 Temel Adımlar

* **Resim** verileri toplanır veya çekilir.
* Toplanan resimler `labelimg` yardımıyla etiketlenir ve `.xml` uzantılı dosyaları oluşturulur.
* `images` dizinine **resimler** ve onlara ait **xml** dosyaları %80'i train %20'i eval olacak şekilde klasörlere ayrılarak yerleştirilir.
* `scripts/preprocessing` dizindeki `xml_path_regulator.py` scripti aracılığıyla xml ve resimlerde yol sorunları düzeltilir, veriler yeniden adlandırılır.
* `scripts/preprocessing` dizindeki `xml_to_csv.py` scripti aracılığıyla veriler `.csv` uzantılı tablosal bir dosyaya dönüştürülür.
* Oluşturulan **csv** dosyasında resimlerin etiketlerine göre sayıları tablo olarak gösterilir. \(Excel yardımıyla\)
* Verilerde denge durumunun \(her veriden yaklaşık olarak aynı sayıda varsa\) kontrolü yapılır.
* Her çeşit veri için bir `id` belirtilecek şekilde `label_map.pbtxt` adlı etiket haritası oluşturulur
* Oluşturulan **csv**, **etiket haritası** ve **resim** verileri `scripts/preprocessing` dizindeki `generate_tfrecord.py` scripti aracılığıyla veriler `.record` uzantılı kayıtlara dönüştürülür.
* Seçilen modele özgü yapılandırma dosyası indirilir.
* Yapılandırma dosyası olan `*.config` dosyasındaki `PATH_TO_CONFIGURED` olarak işaretlenen alanlar, `num_classes`, `num_examples` ve `batch_size` değerleri güncellenir.
  * `num_examples` eval dizindeki resim sayısıdır \(toplam class sayısı değil\)

## **🕵️‍♂️ Resimlerdeki Hataları Bulma**

Resimlerde hata olduğu zaman eğitim aşamasında tensorflow modeli çalışma hatası vermektedir. Resimleri kontrol etmek için [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/check_images.py) scripti alttaki komutlarla kullanabilirsiniz.

```text
python scripts\preprocessing\check_images.py -i workspace\example_detection\images\train​python scripts\preprocessing\check_images.py -i workspace\example_detection\images\eval
```

## **👨‍🔧 Verileri Yeniden Adlandırma ve XML Hatalarını Düzeltme**

LabelImg ile etiketlediğiniz resimleri farklı bir dizine taşımanız durumunda XML dosyalarındaki yollar uyuşmayacaktır. XML dosya yollarını düzeltmek, etiketsiz resimleri görüntülemek için [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/xml_path_regulator.py) script dosyamı alttaki komutlar ile kullanabilirsiniz.

```text
python scripts\preprocessing\xml_path_regulator.py -i %TENSORFLOW%\workspace\example_detection\images\train  -p train​python scripts\preprocessing\xml_path_regulator.py -i %TENSORFLOW%\workspace\example_detection\images\eval  -p eval
```

## **🧐 Etiketlenmemiş Resimleri Bulma**

Etiketlenmemiş resimleri [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/find_unlabeled_imgs.py) script dosyası ile alttaki komutlar ile kullanabilirsiniz.

> Eğer XML scriptini kullandıysanız bu kontrolü yapmanıza **gerek yoktur**, XML scripti bunu zaten yapmaktadır.

```text
python scripts\preprocessing\find_unlabeled_imgs.py -i %TENSORFLOW%\workspace\example_detection\images\train​python scripts\preprocessing\find_unlabeled_imgs.py -i %TENSORFLOW%\workspace\example_detection\images\eval
```

## **💫 XML'i CSV'ye Çevirme**

XML dosyalarını CSV dosyasında toparlamak için [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/xml_to_csv.py) scripti alttaki komutlar ile kullanabilirsin.

> Komutları **Anaconda Prompt** üzerinden **tensorflow** ortamını aktif ederek uygulamayı unutmayın.

```text
# Create train data:python scripts\preprocessing\xml_to_csv.py -i %TENSORFLOW%\workspace\example_detection\images\train -o %TENSORFLOW%\workspace\example_detection\images\train_labels.csv​# Create eval data:python scripts\preprocessing\xml_to_csv.py -i %TENSORFLOW%\workspace\example_detection\images\eval -o %TENSORFLOW%\workspace\example_detection\images\test_labels.csv
```

## **👁‍🗨 CSV'lerden Resim Bilgilerini Analiz Etme**

Her bir etiketten kaç tane olduğunu anlamak için csv dosyalarını açıp alltaki yöntemi uygulayın.

* `class` hücresiinin bir altındaki hücreyi seçin
* `ctrl` + `shift` + `aşağı ok` ile tüm sınıf verilerini seçin
* Sağ alttaki butona tıklayın
* `Tables` sekmesine gelin
* Açılan sekmede `Pivot Table` butonuna tıklayın
* Tablo'dan etiketlenen verileri kontrol edin
* Fazladan etiketlenmiş verilerin ismini bulup, filename, width vs. verilerin yazıldığı alanda `CTRL` + `F` komutu ile aratıp, uygun dosya ismini ve `xml` dosyasını silin

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LtFvhrURZC-q-L1-hz0%2F-LtPfR1qFi8AK6pBijty%2F-LtPugZ3XPt8YOD7XpX-%2Fimage.png?alt=media&token=c96ab80b-a407-494c-a885-ca8fd60624e9)![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LtFvhrURZC-q-L1-hz0%2F-LtPfR1qFi8AK6pBijty%2F-LtPujWd3zDuenT1dXhR%2Fimage.png?alt=media&token=4b0b5517-cf1c-4eaa-8a61-ed8b5be146a2)![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LtFvhrURZC-q-L1-hz0%2F-LtPfR1qFi8AK6pBijty%2F-LtPum0Jb5_R9D3cEVLb%2Fimage.png?alt=media&token=9f18415f-c79c-4efc-a9d6-76ff82a230e8)![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LtFvhrURZC-q-L1-hz0%2F-LtPfR1qFi8AK6pBijty%2F-LtPutmhJIfabmcOzpoC%2Fimage.png?alt=media&token=1566c5e0-1920-481e-a529-13d4719c90ee)

## **💱 CSV'yi Record'a Çevirme**

CSV dosyalarını TF kayıtlarına çevirmek için [buradaki](https://github.com/yedhrab/YArtificalIntelligent/tree/f5ce601da28961f26a48e137783188839c9f5600/3%20-%20Tensorflow/scripts/preprocessing/generate_tfrecord.py) scripti alttaki komutlar ile kullanabilirsin.

> Komutları **Anaconda Prompt** üzerinden **tensorflow** ortamını aktif ederek uygulamayı unutmayın.

```text
python generate_tfrecord.py --label_map=%TENSORFLOW%\workspace\example_detection\data\label_map.pbtxt --csv_input=%TENSORFLOW%\workspace\example_detection\images\train_labels.csv --img_path=%TENSORFLOW%\workspace\example_detection\images\train --output_path=%TENSORFLOW%\workspace\example_detection\data\train.record​python generate_tfrecord.py --label_map=%TENSORFLOW%\workspace\example_detection\data\label_map.pbtxt --csv_input=%TENSORFLOW%\workspace\example_detection\images\test_labels.csv --img_path=%TENSORFLOW%\workspace\example_detection\images\eval --output_path=%TENSORFLOW%\workspace\example_detection\data\eval.record
```


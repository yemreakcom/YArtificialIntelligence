# 📂 Dizin Yapısını Oluşturma

## 🌃 Tensorflow Dizininizi Geçici Ortam Değişkenlerine Ekleme

{% tabs %}
{% tab title="⚡ Hızlı İşlem" %}
Alttaki komut yardımıyla açık olan cmd ekranına ortam değişkeni tanımlayabilirsiniz.

```text
set TENSORFLOW=<dizin_yolu>
```

* `<dizin_yolu>` Tensorflow'u kurmak istediğiniz dizin
  * _Örn: "C:\Tensorflow"_
{% endtab %}

{% tab title="🚀 Kalıcı İşlem" %}
* Bilgisayarıma sağ tıklayın `Ayarlar` kısmına girin
* Sol alanda `Gelişmiş Sistem Ayarları`'na tıklayın
* Açılan ekranda `Ortam Değişkenleri` butonuna tıklayın
* Üst kısımdaki kullanıcı değişkenleri alanında `Yeni` butonuna tıklayın
* Değişken ismine: `Tensorflow` Değerine: 'dizin yolunuzu' yazın
{% endtab %}
{% endtabs %}

## 🧱 Temel Klasörlerin Oluşturulması

{% tabs %}
{% tab title="👩‍💻 Kod ile Dizin Oluşturma" %}
İlerideki yapı için bu dizinin yolu `%TENSORFLOW%` olarak ifade edilecektir.

```text
mkdir %TENSORFLOW%\workspace\example_detection
mkdir %TENSORFLOW%\workspace\example_detection\data
mkdir %TENSORFLOW%\workspace\example_detection\images\train
mkdir %TENSORFLOW%\workspace\example_detection\images\eval
mkdir %TENSORFLOW%\workspace\example_detection\models
```

{% hint style="success" %}
Düzgün ve verimli çalışmak için buradaki yapıyı kullanmanız önerilir.
{% endhint %}
{% endtab %}

{% tab title="📂 Temel Yapı" %}
```text
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
```

| Dizin | Açıklama |
| :--- | :--- |
| addons | LabelImg vs. |
| docs | Dökümanlar |
| models | Tensorflow Models dosyası |
| scripts | Kullanacağınız ortak kod parçaları |
| workspace | Çalışma Alanı |
{% endtab %}

{% tab title="👨‍💼 Çalışma Alanı" %}
```text
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

| Dizin | Açıklama |
| :--- | :--- |
| data | Eğitime katılacak verileri \(_eval.record, train.record, label\_map_\) içeririr. |
| model | Eğitilecek modellerin dosyalarını içerir. |
{% endtab %}

{% tab title="📀 Data" %}
```text
+ example_detection
    + data
        - label_map.pbtxt
        - eval.record
        - train.record
    + models
    ...
...
```

| Dosya | Açıklama |
| :--- | :--- |
| `label_map.pbtxt` | Etiket haritası dosyası |
| `eval.record` | Test için kullanılacak tensorflow kayıtları \(TF record\) |
| `train.record` | Eğitim için kullanılacak tensorflow kayıtları \(TF record\) |
{% endtab %}

{% tab title="🤖 Model Dizini" %}
```text
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

| İsim | Tipi | Açıklama |
| :--- | :--- | :--- |
| eval | Dizin | Test sonuçları burada tutulur. |
| train | Dizin | Eğitim çıktıları burada tutulur |
| `.config` | Dosya | Yapılandırma dosyası |
{% endtab %}
{% endtabs %}


---
description: 'Veri bilimi (data science) giriş, temel kullanım ve tanıma'
---

# 🔰 Giriş \| Veri Bilimi

## 🧱 Temel Bilgiler

* CSV, JSON işlemleri için `pandas` _package_'ı kullanılır
* `DataFrame`, `pandas` paketinin bir objesidir

## 🌟 Popüler Paketler

| Kütüphane | Açıklama |
| :--- | :--- |
| NumPy | Matematiksel işlemler |
| Matplotlib | Grafik çizim işlemleri |
| Pandas | Çoklu verileri işleme |

## 🆚 CSV vs JSON

| CSV | JSON |
| :--- | :--- |
| Csv en sade tablo verisi formatıdır | `dict` ve `list`'in harmanlanmış hali denebilir |
| `<val>, <val>, ...` formatında saklanır | `{<key>: <value> ...}` formatında saklanır |
| `pandas` paketi ile ele alınır | `pandas` paketi ile ele alınır |

## 🔸 Dosya Tipleri

| Gzip | NumPy | Pickle |
| :--- | :--- | :--- |
| Sıkıştırılmış dosyalardır \(daha az MB\) | Matematik ve matrix işlemlerini ele alır | Objeleri dosyaya kaydetmeyi sağlar |
| Dosya uzantısı `.gz` | Dosya uzantısı `npy` | Dosya uzantısı `pkl` |
| Binary formattadır \(`wb`\) | Text formatında da kayıt edilebilir \(`w`, `wb`\) | Binary formatındadır \(`wb`\) |

## 💠 DataFrame Metodları

| Metod | Açıklama |
| :--- | :--- |
| `df.head()` | Verilerin başlangıç kısmından birazını gösterme |
| `df.read_csv(<dosya yolu>)` | CSV dosyasını okuma |
| `df.to_csv(<dosya yolu>)` | CSV dosyası oluşturma |
| `df.read_json(<dosya yolu>)` | JSON dosyasını okuma |
| `df.to_json(<dosya yolu | url>)` | JSON dosyası oluşturma |


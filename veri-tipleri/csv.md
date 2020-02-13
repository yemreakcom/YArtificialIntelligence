---
description: 'Tablo (csv) oluşturma, okuma ve temel kullanım'
---

# 📅 Tablo Verileri

## 🧱 Temel Bilgiler

* `csv` en sade tablo verisi formatıdır
* `,` karakteri ile veriler ayrılır
* `pandas` moduülü ile ele alınır

## 👀 Tablo Okuma

```python
list_table = []
with open('./data/csv_sample.txt', 'r') as f:
    for line in f.readlines():
        list_table.append(line.strip().split(','))
list_table
```

```python
 [
  ['index', 'name', 'age'],
  ['0', 'Dylan', '28'],
  ['1', 'Terrence', '54'],
  ['2', 'Mya', '31']
 ]
```

## 🏗️ Tablo Oluşturma

* CSV dosyalarında veriler `,` karaterine göre sütunlara yerleşir
* Tanımlanmayan alanlara `NaN` yazılır

```python
pd.DataFrame({'a': [0, 3, 10], 'b': [True, True, False]}).to_csv('./data/pd_write.csv')
pd.read_csv('./data/pd_write.csv', index_col=0)
```


---
description: 'Web üzerindeki JavaScript verileri (json) yapısı, okuma ve temel işlemler'
---

# 📜 JSON \| Veri Bilimi

## ❔ JSON Nedir

* Internet üzeriindenki çoğu veri JSON tipindedir
  * Web üzeride Javascript çok fazla kullanılmaktadır
  * Google, Twitter vs.
* JavaScript Object Notation olarak açılır
* JavaScript'te bilgileri aktarmak için kullanılır

## 🏗️ JSON Yapısı

* `dict` ve `list`'in harmanlanmış hali denebilir

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

book1 = {
    'title': 'The Prophet',
    'author': 'Khalil Gibran',
    'genre': 'poetry',
    'tags': [
        'religion',
        'spirituality',
        'philosophy',
        'Lebanon',
        'Arabic',
        'Middle East',
        ],
    'book_id': '811.19',
    'copies': [{'edition_year': 1996, 'checkouts': 486,
               'borrowed': False}, {'edition_year': 1996,
               'checkouts': 443, 'borrowed': False}],
    }
book2 = {
    'title': 'The Little Prince',
    'author': 'Antoine de Saint-Exupery',
    'genre': 'children',
    'tags': ['fantasy', 'France', 'philosophy', 'illustrated', 'fable'
             ],
    'id': '843.912',
    'copies': [{
        'edition_year': 1983,
        'checkouts': 634,
        'borrowed': True,
        'due_date': '2017/02/02',
        }, {'edition_year': 2015, 'checkouts': 41, 'borrowed': False}],
    }
library = [book1, book2]
library
			
```

## ⭐ JSON Örneği

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
[{
    'title': 'The Prophet',
    'author': 'Khalil Gibran',
    'genre': 'poetry',
    'tags': [
        'religion',
        'spirituality',
        'philosophy',
        'Lebanon',
        'Arabic',
        'Middle East',
        ],
    'book_id': '811.19',
    'copies': [{'edition_year': 1996, 'checkouts': 486,
               'borrowed': False}, {'edition_year': 1996,
               'checkouts': 443, 'borrowed': False}],
    }, {
    'title': 'The Little Prince',
    'author': 'Antoine de Saint-Exupery',
    'genre': 'children',
    'tags': ['fantasy', 'France', 'philosophy', 'illustrated', 'fable'
             ],
    'id': '843.912',
    'copies': [{
        'edition_year': 1983,
        'checkouts': 634,
        'borrowed': True,
        'due_date': '2017/02/02',
        }, {'edition_year': 2015, 'checkouts': 41, 'borrowed': False}],
    }]
			
```

## 👀 JSON Okuma

* JSON dosyaları `f.read()` şeklinde değil, `json.load(f)` şekinde okunur

> `f`, dosya objesi

### 🏈 `f.read` 

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
with open('./data/library.json', 'r') as f:
    library_string = f.read()

```

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''[\n {\n "title": "The Prophet",\n "author": "Khalil Gibran",\n "genre": "poetry",\n "tags": [\n "religion",\n "spirituality",\n "philosophy",\n "Lebanon",\n "Arabic",\n "Middle East"\n ],\n "book_id": "811.19",\n "copies": [\n {\n "edition_year": 1996,\n "checkouts": 486,\n "borrowed": false\n },\n {\n "edition_year": 1996,\n "checkouts": 443,\n "borrowed": false\n }\n ]\n },\n {\n "title": "The Little Prince",\n "author": "Antoine de Saint-Exupery",\n "genre": "children",\n "tags": [\n "fantasy",\n "France",\n "philosophy",\n "illustrated",\n "fable"\n ],\n "id": "843.912",\n "copies": [\n {\n "edition_year": 1983,\n "checkouts": 634,\n "borrowed": true,\n "due_date": "2017/02/02"\n },\n {\n "edition_year": 2015,\n "checkouts": 41,\n "borrowed": false\n }\n ]\n }\n]'''

```

### 🏀 `json.load(f)` 

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
with open('./data/library.json', 'r') as f:
    reloaded_library = json.load(f)
reloaded_library

```

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
[{
    'title': 'The Prophet',
    'author': 'Khalil Gibran',
    'genre': 'poetry',
    'tags': [
        'religion',
        'spirituality',
        'philosophy',
        'Lebanon',
        'Arabic',
        'Middle East',
        ],
    'book_id': '811.19',
    'copies': [{'edition_year': 1996, 'checkouts': 486,
               'borrowed': False}, {'edition_year': 1996,
               'checkouts': 443, 'borrowed': False}],
    }, {
    'title': 'The Little Prince',
    'author': 'Antoine de Saint-Exupery',
    'genre': 'children',
    'tags': ['fantasy', 'France', 'philosophy', 'illustrated', 'fable'
             ],
    'id': '843.912',
    'copies': [{
        'edition_year': 1983,
        'checkouts': 634,
        'borrowed': True,
        'due_date': '2017/02/02',
        }, {'edition_year': 2015, 'checkouts': 41, 'borrowed': False}],
    }]


```

## 🌍 URL ile JSON okuma

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
pd.read_json('https://api.github.com/repos/pydata/pandas/issues?per_page=5')
```


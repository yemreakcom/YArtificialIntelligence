# 🚅 Serileştirmiş Veriler

## 🔰 Serileştirme \(`pickle`\)

* Uygulamanın oluşturduğu verileri dosyaya kaydedip, tekrardan kullanmayı sağlar
  * Karmaşık uygulamalarda sıklıkla yapılır
* Kaydetme işlemi text formatında değil , **binary** formatında olur
  * `w` yerine `wb` kullanılır
* Sıklıkla `pickle` paketi kullanılır
* Dosya uzantısı `pkl`

## 💠 Pickle Metodları

| Metod | Açıklama |
| :--- | :--- |
| `dump(<pickle>, <file>)` | `pickle` objesini dosyaya yazma |
| `pickle = load(<file>)` | `pickle` objesini dosyadan okuma |

## ⭐ Pickle Örnekleri

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle 

pickle_example = ['hello', {'a': 23, 'b': True}, (1, 2, 3), [['dogs',
                  'cats'], None]]

# Metin olarak kaydedilemez
with open('./data/pickle_example.txt', 'w') as f:
    f.write(pickle_example) 
# TypeError: write() argument must be str, not list

# Pickle olarak kaydedebiliriz
with open('./data/pickle_example.pkl', 'wb') as f:
    pickle.dump(pickle_example, f)

with open('./data/pickle_example.pkl', 'rb') as f:
    reloaded_example = pickle.load(f)

reloaded_example
# ['hello', {'a': 23, 'b': True}, (1, 2, 3), [['dogs', 'cats'], None]]

reloaded_example == pickle_example # True
			
```


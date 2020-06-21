# 🔰 Giriş \| Pandas

## ❔ Ne için Kullanılır

Veri çekme işlemleri için kullanılır.

## 💫 Dict'i CSV'ye Çevirme

```python
df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})

df.to_csv(index=False)
# 'name,mask,weapon\nRaphael,red,sai\nDonatello,purple,bo staff\n'
```

## 🏓 Excel Oluşturma & Okuma

```python
import pandas as pd

pd.DataFrame({'a': [0, 3, 10], 'b': [True, True, False]}).to_excel('./pd_write.xlsx')
data = pd.read_csv('./pd_write.xlsx', index_col=0)

```

## 🧱 Temel İşlemler

| DataFrame İşlemi | Açıklama |  |
| :--- | :--- | :--- |
| `df.loc[<i>] = <list>` | i. **indekse** değer atama |  |
| `df.iloc[<i>] = <list>` | i. **satıra** değer atama \(çok tercih etme\) |  |
| `df.drop(DATA_FRAME.index, inplace=True)` | Tüm verileri silme |  |
| \`df.to\_csv\(&lt;file | filename&gt;, header=f.tell\(\)==0\)\` | CSV'ye ekleme \(`tell` dosyanın başı ise 0 verir\) |
| `len(pandas.read_csv(<path_to_csv>))` | Veri sayısını bulma |  |


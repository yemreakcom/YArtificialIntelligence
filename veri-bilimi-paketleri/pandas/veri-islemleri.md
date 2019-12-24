# 🗃️ Veri İşlemleri

## 👀 Verileri Okuma

Ana yapı `df.<metod>` şeklindedir.

> `<işlem>[<i>]` ile `i`. değer alınır

| Metod | Açıklama |
| :--- | :--- |
| `.loc[[<iname>, ...], <col_name> ]` | Birden fazla verinin özelliğini alma |
| `.loc[<iname>:<iname>, <col_name>]` | İki index ismi arasındaki verileri alma |
| `.iloc[<i>]` | İlk `i` veriyi alma |
| `.iloc[<i1>:<i2>, <col_i>]` | `i1` ile `i2` arasındaki `col_i`. sütunu alma |

## 💫 Verileri Değiştirme

| İşlem | Açıklama |
| :--- | :--- |
| `df['<col_name'] = <val_list>` | Sütun ekleme \(`val_list` uzunluğu satır sayısına eşit olmalı\) |
| `np.random.choice(<list>, size=len(df)` | Örnek `<val_list>` |
| `df[<iname>] = <list>` | `iname` isminde sütun oluşturma |
| `df.loc[<i>] = <list>` | `i`. satırda eleman oluşturma |
| `df.loc[<iname>] = {<col_name>: <val>, ...}` | Satır ekleme |
| `df.drop(<iname>)` | Satır \(veri\) silme |
| `df.drop(<i>, inplace=True)` | `i`. satırı silme |
| `df.drop(<col_name>, axis=1)` | Sütun silme |
| `df.drop(<col_name>, axis=1, inplace=True)` | Değişikliği tablo üstünde uygulama |
| `df.index.<iname> = <name>` | `iname` ismindeki sütunun adını `name` yapma |


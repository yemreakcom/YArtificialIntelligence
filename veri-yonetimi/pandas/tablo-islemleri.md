# 📊 Tablo İşlemleri

### Tablo Oluşturma

```python
import pandas as pd

 # List ile tablo oluşturma
df = pd.DataFrame(<list>, columns=<list>)
df = pd.DataFrame(list(zip(<col1>, <col2>, <col3>, <col4>)))
df = pd.DataFrame(list(zip(<val_list>, <val_list>)), columns=<col_list>, index = <iname_list>) #

# Dict ile tablo oluşturma
df = pd.DataFrame(<dict>, index=<iname_list>)
df = pd.DataFrame({<col>: <val_list>, ...}, index=<iname_list>)

# Sütun değiştirme
df.columns = <list>

# Index değiştirme (ve df'e uygulama)
df.set_index(<col>, inplace=True)
# Index sıfırlama (ve df'e uygulama)
df.reset_index(inplace=True)
# Birden fazla index belirleme
df.set_index(['username', 'email'])
```

Kullacı tablosu örneği \`\`\`py from string import ascii\_letters, digits import numpy as np import datetime usernames = \['alice36', 'bob\_smith', 'eve'\] passwords = \[''.join\(np.random.choice\(list\(ascii\_letters + digits\), 8\)\) for x in range\(3\)\] creation\_dates = \[datetime.datetime.now\(\).date\(\) - datetime.timedelta\(int\(x\)\) for x in np.random.randint\(0, 1500, 3\)\] df = pd.DataFrame\({'username': usernames, 'password': passwords, 'date-created': pd.to\_datetime\(creation\_dates\)}\) df \`\`\` !\[\]\(../res/df\_ex\_tablo\_users.png\)

Numpy'dan tablo oluşturma \`\`\`py random\_data = np.random.random\(\(4,3\)\) df\_random = pd.DataFrame\(random\_data, columns=\['a', 'b', 'c'\]\) df \`\`\` !\[\]\(../res/df\_ex\_tablo\_numpy.png\)

### Tablo Birleştirme

| İşlem | Açıklama |
| :--- | :--- |
| `pd.merge(left=<df1>,right=<df2>, left_on=<iname1>, right_on=<iname2>)` | Kesişimi \(Inner join\) |
| `pd.merge(left=<df1>,right=<df2>, how='left', left_on=<iname1>, right_on=<iname2>)` | A ve kesim \(Left join\) |
|  |  |

> Kaynaklar: [Pandas Merging Data](https://datacarpentry.org/python-ecology-lesson/05-merging-data/index.html)

### Tabloyu Bölme

Ana yapı `df<işlem>`

| İşlem | Açıklama |
| :--- | :--- |
| `.dtypes` | Tablodaki özellikleri \(attr\) listeler |
| `[<col>]` | Sütun alma \(`pandas.core.series.Series`\) |
| `mean()` | Sütunların ortalama değerlerini alma |
| `loc[<iname>]` | İndex ismi ile veri okuma |
| `.loc[[<iname>, ...], <col_list> ]` | Tabloyu parçalama |
| `.head()` | Tablonun başını görüntüleme |
| `.tail()` | Tablonun sonunu görüntüleme |

### Tablodan Veri Alma

| İşlem | Açıklama |
| :--- | :--- |
| `[<col>]` | Sütun alma \(`pandas.core.series.Series`\) |
| `df[<col>][<i>]` | `col` sütunundaki `i`. öğeye erişme |
| `df.loc[<i>, <col>]` | `i`. öğenin `col` verisine erişme |
| `df.describe()` | İstatistiksel verileri alma \(count mean std min 25 50 75 max\) |

### Tabloda Arama

| İşlem | Açıklama |
| :--- | :--- |
| `df.loc[df[<column_name>] == <some_value>]` | Sütunun değeri eşit olanları listeleme |
| `df.loc[df['column_name'].isin(some_values)]` |  |
| `df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]` |  |

> ⚠ `df['column_name'] >= A & df['column_name'] <= B` yapısı parantez olmadığından `df['column_name'] >= (A & df['column_name']) <= B` şeklinde algılanır.
>
> Kaynak: [Stackoverflow](https://stackoverflow.com/a/17071908/9770490)

### Tablo ile İlgili Code Snippets

```python
# Max / Sum yapıp verileri listeler
idx = pb_all_data.groupby(['post_code'])['items'].transform(max) == pb_all_data['items']
df_items_by_region = pb_all_data[idx]['items'] /  pb_all_data.groupby('post_code').sum()['items']

items_by_region = []
for i in range(100):
    x, y = df_items_by_region.index[i]
    z = df_items_by_region[i]
    items_by_region.append((x, y, z))
```

> Kaynak: [Stackoverflow](https://stackoverflow.com/a/15705958/9770490)


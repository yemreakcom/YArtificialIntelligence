# 🏃‍♂️ Hızlı Notlar \| Pandas

## 🔗 Faydalı Bağlantılar

* [Neden SQL değil de bu?](https://datascience.stackexchange.com/a/34366)
* [Dökümantasyon](https://pandas.pydata.org/pandas-docs/stable/user_guide/)
* [SQL to Pandas](https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e)

## Hızlı Notlar

* `df.dtypes` Tablodaki özellikleri listeler

Json okuma \`\`\`py import gzip import simplejson as json with gzip.open\('./data/yelp.json.gz', 'r'\) as f: yelp\_data = \[json.loads\(line\) for line in f\] yelp\_df = pd.DataFrame\(yelp\_data\) yelp\_df.head\(\) \`\`\`

## DataFrame Series

* Datafrme `dict of Series` şeklinde tanımlanır
* Seriler aynı `np.array` gibidir
  * `index` ile boyutlarını görebiliriz
  * `RangeIndex(start=0, stop=37938, step=1)`
* `yelp_df[100]['city']` şeklinde erişim olmaz
  * `yelp_df['city'][100]` şeklinde 100. öğeye erişilir
  * Veya `yelp_df.loc[100, 'city']` şeklinde 100.verinin şehir verisi alınır

## Hızlı Kod Notları

```python
df = pd.DataFrame({'shoe_size': shoes, 'jersey_size': jerseys}, index = players)
df = pd.DataFrame(list(zip(shoes, jerseys)), columns = ['shoe_size', 'jersey_size'], index = players)
print(df['shoe_size'])
print(np.log(df))
df.mean()
print(df.loc['Ronaldo'])
print(df.loc[['Ronaldo', 'George Best'], 'shoe_size'])
# can also select position-based slices of data
print(df.loc['Ronaldo':'George Best', 'shoe_size'])
# for position-based indexing, we will typically use iloc
print(df.iloc[:5])
print(df.iloc[2:4, 0])
# to see just the top of the DataFrame, use head
df.head()
# of for the bottom use tail
df.tail()
# adding a new column
df['position'] = np.random.choice(['goaltender', 'defense', 'midfield', 'attack'], size=len(df))
df.head()
# adding a new row
df.loc['Dylan'] = {'jersey_size': 91, 'shoe_size': 9, 'position': 'midfield'}
df.loc['Dylan']
df.drop('Dylan')
df.drop('position', axis=1)
df = df.drop('Dylan')
print(df)
df.drop('position', axis=1, inplace=True)
print(df)
```

## Veri Çekme

* Gzip'ten alabiliyor

```python
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("dw-data/practices.csv.gz", names=col_names)
pratices.head() # Başı gösterme
pratices.tail() # Sonu gösterme

scripts['items'].sum() # Tüm items değerlerini toplama
pratices.describe() # veri sayısı, ortalama, standart sapma, min, 1.çeyrek, medyan, 2.çeyerk, max

# count  973193.000000  973193.000000  973193.000000  973193.000000
# mean        9.133136      73.058915      67.986613     741.329835
# std        29.204198     188.070257     174.401703    3665.426958
# min         1.000000       0.000000       0.040000       0.000000
# 25%         1.000000       7.800000       7.330000      28.000000
# 50%         2.000000      22.640000      21.220000     100.000000
# 75%         6.000000      65.000000      60.670000     350.000000
# max      2384.000000   16320.000000   15108.320000  577720.000000

scripts.groupby("bnf_name").sum() # Tüm değerleri toplama ve bnf_name'e göre gruplama
sum_bnf_items = sums_bnf['items']
most_common_item = [(sum_bnf_items.idxmax(), sum_bnf_items.max())]
# idmax: ID max: Değeri döndürür
df.loc[sum_bnf_items.idxmax()] # Max eleman satırını basma

df.filter(['a', 'b']) # sadece a b sütünunu gösterme
```

## Birleştirme

```python
# Indexlere göre otomatik birleştirme
pd.concat([scripts, practices], axis=1, join='inner')

concated_data['sums'] = concated_data.groupby(["post_code"])['items'].transform('sum') # Aynı post koda göre toplama
```

## Drop İşlemleri

* [Pandas Drop](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)

## Harici Linkler

* [Group by one columns and find sum and max value for another in pandas](https://stackoverflow.com/a/44725963/9770490)


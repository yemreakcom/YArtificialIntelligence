---
description: Makine öğrenimi uygulamak için önceden hazırlanmış python paketine giriş.
---

# 🚶‍ SciKit-Learn'e Giriş

## ❔ SciKit-Learn Nasıl Çalışır?

Tabloda verilen `Estimator` class yapısını kullanılır

| Obje | Terminolojisi | Açıklama |
| :--- | :--- | :--- |
| `X` | Featured matrix | Özellik matriksi |
| `Y` | Label vector | Etiket vektörü |
| `fit` |  | eğitim metodu |
| `predict` |  | tahmin metodu |

## 👶 Scikit-Learn Basit Kullanım

```python
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True, normalize=False)
lr.fit(X.reshape(-1, 1), y)
lr.coef_, lr.intercept_

predictions = lr.predict(X.reshape(-1, 1))
plt.plot(X, y, '.', label='data')
plt.plot(X, predictions, label='model')
plt.legend();
```

![](../.gitbook/assets/image%20%2813%29.png)

## 👨‍💻 Scikit-Learn PipeLine Kullanımı

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

pipe = Pipeline([
    ('polynomial_transform', PolynomialFeatures(3)),
    ('linear_fit', LinearRegression())
])

pipe.fit(X.reshape(-1, 1), y)

predictions = pipe.predict(X.reshape(-1, 1))
plt.plot(X, y, '.', label='data')
plt.plot(X, predictions, label='model')
plt.legend();
```

![](../.gitbook/assets/image%20%281%29.png)

## 🦋 Genelleştirme Yapılması Durumunda SciKit-Learn Performansı

```python
X = np.linspace(0, 4, 100)
y = X**exp + np.random.randn(X.shape[0])/10
predictions = pipe.predict(X.reshape(-1, 1))
plt.plot(X, y, '.', label='data')
plt.plot(X, predictions, label='model')
plt.legend()
```

![](../.gitbook/assets/image%20%2823%29.png)

## 🔗 Harici Bağlantılar

* [📜 Intro to Machine Learning](https://github.com/yedhrab/YArtificalIntelligent/tree/88f012cd66170bd63be379c8400a3fb28e5bc634/0.2%20-%20Machine%20Learninig%20Notebooks/1%20-%20Eğitici%20Notebooklar/0%20-%20Intro%20to%20Machine%20Learning.ipynb)
* [📺 WQU ML lecture 01](https://www.youtube.com/watch?v=9J6FNvil6Gw&feature=youtu.be)
* [📊 WQU Data Science](https://wqu.org/programs/data-science)


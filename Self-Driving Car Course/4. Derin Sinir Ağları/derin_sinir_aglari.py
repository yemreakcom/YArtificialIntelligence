# Derin Sinir Ağları
# Yunus Emre AK

import numpy as np
import matplotlib.pyplot as plt

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Özel veri kümeleri oluşturmak için
from sklearn import datasets

# Nokta sayısı
n = 500

# İncelenecek veri kümesini oluşturma (mavi = 0, turuncu = 1)
x, y = datasets.make_circles(n_samples=n, random_state=123, noise=0.1, factor=0.2)

# Modeli ayrı bir tabloda çizeceğiz
plt.figure(1)

# Noktaları çizdirme
# önce maviler (0), sonra turuncular (1) çizilir
plt.scatter(x[y==0, 0], x[y==0, 1])
plt.scatter(x[y==1, 0], x[y==1, 1])

# Sinir ağı modelini oluşturma
model = Sequential()

# Sinir ağının tipini ve nöronlarını oluşturma
# Dense: Layer (katman) X(input_shape=2)-4-1 (çıktı)
model.add(Dense(4, input_shape=(2,), activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

# Optimize etme ve değişim tipini ayarlama
model.compile(Adam(lr=0.01), 'binary_crossentropy', metrics=['accuracy'])

# Modele verileri ekleme
# verbose: Ekrana çıktıları yazar
# batch_size: Her devre için gereken adım (GPU ile alakalı)
# epochs: Devre sayısı
h = model.fit(x=x, y=y, verbose=1, batch_size=20, epochs=100, shuffle='true')

# Grafik verilerini ayrı bir tabloda göstereceğiz
plt.figure(2)

# Öğrenme grafiğini çizdirme
plt.plot(h.history['acc'])
plt.xlabel('epoch')
plt.legend(['accuracy'])
plt.title('accuracy')

# Öğrenme grafiğini çizdirme
plt.plot(h.history['loss'])
plt.xlabel('epoch')
plt.legend(['loss'])
plt.title('loss')

def plat_decision_boundary(x, y, model):
    # x,y dağılımlarını bulma (0.5 br daha uzun olacak çizgi)
    x_span = np.linspace(min(x[:, 0]) - 0.25, max(x[:, 0]) + 0.25)
    y_span = np.linspace(min(x[:, 1]) - 0.25, max(x[:, 1]) + 0.25)
    
    # Her x'e karşılık bir y değerinin geldiği matriksi oluşturma
    xx, yy = np.meshgrid(x_span, y_span)
    xx_, yy_ = xx.ravel(), yy.ravel()
    tablo = np.c_[xx_, yy_]
    
    ongoru_metodu = model.predict(tablo)
    z = ongoru_metodu.reshape(xx.shape)
    plt.contourf(xx, yy, z)
    

# Modellerin olduğu yere çizilecek
plt.figure(1)

# Modeli ekrana çizdirme
plat_decision_boundary(x, y, model)
plt.scatter(x[:n, 0], x[:n, 1])
plt.scatter(x[n:, 0], x[n:, 1])


# Modeli ekrana çizdirme
plat_decision_boundary(x, y, model)
plt.scatter(x[:n, 0], x[:n, 1])
plt.scatter(x[n:, 0], x[n:, 1])


# Yeni bir nokta oluşturma ve test etme
x1 = 0.1
x2 = 0.2
nokta = np.array([[x1, x2]])

# Model'in öngürüsü
ongoru = model.predict(nokta)

# Noktayı ekrana belirgin olarak çizme
plt.plot([x1], [x2], marker='o', markersize=10, color="red")

# Öngörüyü yazdırma
print("Öngörüm ", ongoru.item(0))

# Plot'u çizdirme
plt.show()
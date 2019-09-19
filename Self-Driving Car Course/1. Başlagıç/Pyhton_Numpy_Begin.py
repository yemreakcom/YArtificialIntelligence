#!/usr/bin/env python
# coding: utf-8

# # Numpy olmadan kod

# In[16]:


list_two = list(range(1, 4))
list_three = list(range(1,4))
list_sum = []

print(list_two, " -> ", list_three)

for i in range(3):
    list_two[i] **= 2
    list_three[i] **= 3
    list_sum.append(list_two[i] + list_three[i])
    
print(list_two, " -> ", list_three)
print(list_sum)


# # Numpy Sonrası

# In[22]:


import numpy as np

# list_two = list(range(1, 4)) ** 2 olmaz
array_two = np.arange(1, 4) ** 2
array_three = np.arange(1, 4) ** 3

print(array_two + array_three)


# Numpy 2D, 3D diziler

# In[35]:


# Verileri oluşturma
x = np.arange(3)
y = np.arange(3, 6)
z = np.arange(6, 9)

# 2D dizi
multi_array = np.array([x, y, z])

# Diziyi yazdırma
print(multi_array, "\n")

# i-j verisi
print(multi_array.shape)


# Verilen 2 sayı arasındaki istenen sayıda sayıyı gösterir

# In[45]:


# 1 ve 10 dahil, 50 tane sayı gösterir
w = np.linspace(1, 31, 3)
print(w, "\n")

# 1 ve 30 dahildir
x = np.linspace(1, 30, 5)
print(x)

# 30 dahil değildir (False)
x = np.linspace(1, 30, 5, False)
print(x)


# Kısmi listeleme ve yazdırma olayı (slice)

# In[101]:


# 2. veriden sonraki verileri listeler
x = np.arange(3, 10)
print(x)
print(x[2:])
print(x[:2 :1])


# 1D diziyi 2D veya 3D şekline getirme (reshaping)

# In[82]:


# 9 verili x dizi oluşturma
x = np.arange(1,10)
print("1D:\n", x)

# 3x3 lük dizi haline çevirme
y = x.reshape(3,3)
print("2D:\n", y)

# 9 elaman, 3x5'lik diziye dönüştürülemez. 15 eleman olması lazım
# z = x.reshape(3, 5)

# 3 satır olmasını istiyoruz, sütun sayısını otomatik ayarlar ( 9 / 3 tam sayı olmazsa hata verir)
z = x.reshape(3, -1)
print("2D:\n", z)

print("\n -----")

# 8 verili x dizisi
short_x = np.arange(1,9)
print("1D:\n", short_x)

t = short_x.reshape(2, 2, -1)
print("3D:\n", t)





# Çok boyutlu dizilerde kısmi listeleme ve yazdırma (slice)

# In[100]:


x = np.arange(1, 19).reshape(3, 2, 3)
print("Parçalı çıktılar:")
print(x[2, 0:1, 2])

#1 den sonrası, 2 den öncesi, ve 0. eleman
print(x[1:, :2, 0])

# 2 farklı gösterim, ikisinin de çıktısı aynıdır
print("\nEş çıktılar:")
print(x[2, :, :])
print(x[2, ...])


print("Farklı gösterimler:")
print(x[2, :3, :3 :2])


# Çok boyutlularda işlemler

# In[110]:


x = np.arange(1,10).reshape(3, 3)
print(x)

print("---\nKoşullu gösterimler:")
print("\n", x[x > 5])
print("\n", x > 5)


# Genel metotlar

# In[116]:


x = np.arange(3, 10).reshape(7, 1)
print(x)

print("En yüksek değer:", x.max())
print("En düşük değer:", x.min())


# Boyutlandırılmış dizileri işleme

# In[127]:


x = np.arange(1, 10).reshape(3, -1)
print(x)

print("---")

# Dizinin orjinalini 1D döndürür
y = x.ravel()
y[1] = 5
print("Ravel:", y, "\nOrjinal:\n", x, "\n") 

# Dizinin kopyasını döndürür
z = x.flatten()
z[1] = 1
print("Flatten:", z, "\nOrjinal:\n", x)


# Matriks işlemleri

# In[149]:


x = np.arange(1, 10)
print(x, "\n")

# 3x3 matrisk yapma
x.shape = [3, 3]
print(x, "\n")

# Transpozunu alma
x = x.T
print(x, "\n")

# Yeniden boyutlandırma, eğer veri yoksa olanları tekrarlar
y = np.resize(x, (6, 6))
print(x, "\n")
print(y, "\n")

# 6 elemanlı 0 dizisi (float)
z = np.zeros((6))
print(z, "\n")

# Her elamanı 1 olan (int), 3x3 matriks
z = np.ones((3, 3), dtype=int)
print(z, "\n")

# 3x3 lük birim matriks
z = np.eye(3, dtype=int)
print(z, "\n")

# 3x3 lük 0-1 arası rastgele verilerden oluşan matriks
t = np.random.rand(3, 3)
print(t, "\n")


# Matriksler (veya çok boyutlu diziler) üzerinde çarpım işlemi

# In[156]:


x = np.matrix([1, 2, 3, 4, 5, 6]).reshape(3, 2)
print(x, "\n")

y = np.matrix([4, -1, 2, 4, 5, -2]).reshape(2, 3)
print(y, "\n")

# Matrikslerde çarpım
z = x * y
print(z)

z = x @ y
print(z)

z = np.matmul(x, y)
print(z)


# # Jupyter genel kullanımını bu şekilde olabilir (?)

# Matriksleri iç içe yığma

# In[168]:


# Yatay yığma işlemi için satırların, dikey yığma işlemi için sütunların aynı olması lazım

x = np.arange(1, 5).reshape(2, 2)
print(x)
print(x.shape)


# In[169]:


# Yatay yığma işlemi için satırların, dikey yığma işlemi için sütunların aynı olması lazım
y = np.arange(5, 13).reshape(2, 4)
print(y)
print(y.shape)


# Yatay ekleme işlemi

# In[170]:


# Yatay ekleme işlemi için satırların aynı olması lazım
# np.concatenate((x, y), axis = 0) ile eşdeğer
z = np.hstack((x, y))
print(z)
print(z.shape)


# Dikey ekleme işlemi

# In[181]:


# Dikey ekleme işlemi için satırların aynı olması lazım
x = x.reshape(-1, 4)
print(x)

# np.concatenate((x, y), axis = 1) ile eşdeğer
z = np.vstack((x, y))
print(z)
print(z.shape)


# Derinliğe ekleme işlemi

# In[188]:


# X ve Y matrikslerin satır ve sütunları aynı olmak zorundadır (x.shape == y.shape)
x = y * 2;

# Derinliğe ekleme işlemi için z adlı 3. bir parametre oluşturulur 
t = np.dstack((x, y))
print(t)


# Sütun olarak ekleme işlemi (yatay eklemeden farklıdır)

# In[190]:


x = np.arange(4)
print(x)


# In[191]:


y = np.arange(4)
print(y)


# In[196]:


# Yatay ekleme
z1 = np.hstack((x, y))
print(z1)

print("---")

# Sütun olarak ekleme
z2 = np.column_stack((x, y))
print(z2)


# In[ ]:





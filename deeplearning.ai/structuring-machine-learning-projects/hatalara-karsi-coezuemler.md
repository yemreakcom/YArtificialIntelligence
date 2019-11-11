# 👨‍🔧 Hatalara Karşı Çözümler

## 🌸 High Bias

* Sinir ağlarını geliştir
* Yeniden katmanları eğit
* Sinir ağlarının mimarisini değiştir
  * _Hyperparameters_
  * RNN, CNN ...
  * Aktivasyon fonksiyonu
  * Derinliği ve boyutu

## 🎈 Avoidable Bias

* Daha büyük model eğitimi
* Uzun veya iyi optimasyon algoritması
  * Momentum
  * RMSProp
  * Adam
* Sinir ağlarının mimarisini değiştir
  * _Hyperparameters_
  * RNN, CNN ...
  * Aktivasyon fonksiyonu
  * Derinliği ve boyutu

## 🌒 High Variance

* Daha çok veri topla
  * _Data augmentation_
* _Regularization_ uygula \(çok etkili\)
  * _L2 regularization_
* Sinir ağlarının mimarisini değiştir
  * _Hyperparameters_
  * RNN, CNN ...
  * Aktivasyon fonksiyonu
  * Derinliği ve boyutu

## ⛅ Data Missmatch

* _Error analysis_'i _dev set_ üzerine uygula
  * _Test set_ üzerine uygulanmama sebebi, _test set_'in ezberlenmesinden \(_overfitting_\) kaçınmak
  * _Train_ ile _dev / test_ kümelerinin arasındaki farkı anlamaya çalış
* _Dev set_, _train set_'ten farklıysa birbirine benzetmeye çalış
  * _Dev_ gürültülü ise _"noisy reduction"_ uygulayabilirsin
* _Train_'e _dev_'e benzer veriler topla
* _"Artifical data syntjessis"_ ile yapay veri oluştur
  * Sade sese gürültü ekleyebilirisin
  * Yankılama ekleyebilirsiz

## 📉 Degree of Overfitting

* _Dropout layer_ ekle


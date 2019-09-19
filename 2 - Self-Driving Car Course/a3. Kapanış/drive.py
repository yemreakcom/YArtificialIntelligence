# Test edilmesi için gereken uygulama (Authonomus Mode'da çalışır)
# https://github.com/yedehrab/self-driving-car-sim

# Ortam oluşturulması
# conda create --name <ortam_ismi>
# conda activate <ortam_ismi>

# Örnek ortam oluşturma:
# conda create --name myenv
# conda activate myenv

# Not: VScode için solt alt kısımdan kullanılacak ortamın python derleyicisini seçmeyi unutmayın!

# Gerekli yüklemeler
# conda install -c anaconda flask
# conda install -c conda-forge python-socketio
# conda install -c conda-forge eventlet
# conda install -c conda-forge tensorflow
# conda install -c conda-forge keras
# set KERAS_BACKEND=tensorflow
# conda install -c anaconda pillow
# conda install -c anaconda numpy
# conda install -c conda-forge opencv

import socketio # İstemci (Client) ve Sunucu (Server) arasında iletişimi sağlar
from flask import Flask # Web uygulaması örneği oluşturmada kullanılır. (Web socket)
import eventlet # Web iletişimi arasındaki olayları (events) kontrol etmek için
from keras.models import load_model # Eğitilimiş Model İşlemleri
import base64 # Şifre işlemleri
from io import BytesIO # Byte işlemleri 
from PIL import Image # Resim işlemleri (pillow)
import numpy as np # Matriks işlemleri
import cv2 # Görüntü İşleme (OpenCV)

# Sabit değişkenler
HIZ_LIMITI = 20

# Sunucunun tanımlanması
sio = socketio.Server()

# Web uygulamasını oluşturma
app = Flask(__name__) # '__main__' ismini atar

# Arabanın belli bir hızı aşmasını engelleme
def gazi_sinirla(hiz):
    # Hız limite ulaştığında 1 değeri gelecek ve sonucunda gaz verisi 1-1'den 0 olacak
    return 1.0 - hiz / HIZ_LIMITI
    
# Resmi analiz etmek için ön işleme sokar (Colab kodları)
def resmi_onisle(nparr_resim):
    # Resmi kırpma
    nparr_resim = nparr_resim[60:135, :, :]
    # Resmi YUV formatına alma
    nparr_resim = cv2.cvtColor(nparr_resim, cv2.COLOR_RGB2YUV)
    # Resmi bulanıklaştırma
    nparr_resim = cv2.GaussianBlur(nparr_resim, (3, 3), 0)
    # Resmi yeniden boyutlandırma
    nparr_resim = cv2.resize(nparr_resim, (200, 66))
    # Resmi normalizasyona sokma
    nparr_resim = nparr_resim / 255 # /= çalışmaz! (çünkü numpy_arr)
    return nparr_resim

# Cevap geldiği anda tetikenir (belki try-except ile yapılabilir)
@sio.on('telemetry')
def telemetry(sid, data): # Data: Aracın veirleri
    # Hız değerini alma (Çok hızlı gitmemesi lazım)
    hiz = float(data['speed'])
    gaz = gazi_sinirla(hiz)

    # Gelen şifrelenmiş veriyi çözümleyerek resmi oluşturma
    resim = Image.open(BytesIO(base64.b64decode(data['image'])))
    # Resmi numpy array şekline dönüştürme
    resim = np.asarray(resim)
    # Resmi ön işleme sokma
    resim = resmi_onisle(resim)
    # Resmi 3D'den 4D'ye alma
    resim = np.array([resim])

    # Direksiyon açısını tahmin etme
    direksiyon_acisi = float(model.predict(resim))

    # Değerleri ekrana yazma
    print("Direksiyon Açısı: {} Gaz: {} Hız:{}".format(direksiyon_acisi, gaz, hiz))

    # Verileri araca gönderme
    kontrol_gonder(direksiyon_acisi, gaz)

# Bağlantı yapıldığı anda tetiklenir
@sio.on('connect') # message, disconnect
def baglan(sid, eventlet):
    print("Bağlantı başarılı!")

    # Başlangıç değeri
    kontrol_gonder(0, 0)

def kontrol_gonder(direksiyon_acisi, gaz):
    sio.emit('steer', data = {
        'steering_angle': direksiyon_acisi.__str__(),
        'throttle': gaz.__str__()
    })

if __name__ == '__main__':
    # Model'ü yükleme
    model = load_model('genereted-udacity-simulated-model.h5')
    # Middleware: trafiği soketio'ya sevk eden
    app = socketio.Middleware(sio, app)

    # IP: '' Tüm olası IP'leri kontrol et
    # Port: 4567 Bağlantı noktasını oluşturma
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
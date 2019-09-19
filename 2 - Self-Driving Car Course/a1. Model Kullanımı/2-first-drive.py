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

# İstemci (Client) ve Sunucu (Server) arasında iletişimi sağlar
import socketio

# Event (olayları) kontrol etmek için
import eventlet

# Web uygulaması örneği oluşturmada kullanılır. (Web socket)
from flask import Flask

# Sunucunun tanımlanması
sio = socketio.Server()

# Web uygulamasını oluşturma
app = Flask(__name__) # '__main__' ismini atar

@sio.on('connect') # message, disconnect
def baglan(sid, eventlet):
    print("Bağlantı başarılı!")

def kontrol_gonder(direksiyon, gaz):
    sio.emit('steer', data = {
        'steering_angle': direksiyon,
        'throttle': gaz
    })

if __name__ == '__main__':
    # Middleware: trafiği soketio'ya sevk eden
    app = socketio.Middleware(sio, app)

    # IP: '' Tüm olası IP'leri kontrol et
    # Port: 4567 Bağlantı noktasını oluşturma
    eventlet.wsgi.server(eventlet.listen(('', 4567)))
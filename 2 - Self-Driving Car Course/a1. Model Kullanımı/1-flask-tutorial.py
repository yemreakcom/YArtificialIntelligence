# Gerekli yüklemeler
# conda install -c anaconda flask

# Web uygulaması örneği oluşturmada kullanılır. (Web socket)
from flask import Flask

# Web uygulamasını oluşturma
app = Flask(__name__) # '__main__' ismini atar

# localhast:port/home uzantısında çalışır
@app.route('/home')
def selamlama():
    return 'Selam'

# Eğer scripti çalıştırıyorsak
if __name__ == '__main__':
    app.run(port=3000)
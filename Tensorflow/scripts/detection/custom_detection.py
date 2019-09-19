import time

import cv2
from PIL import ImageGrab as ig

from detection_utils import *

# Hata ayıklama ve bilgilendirme notlarını aktif eder
DEBUG = True

# Çıktı kaydını aktif etme
KEEP = False

# Yakalanan ekranın gösterilme boyutu (Varsayılan için 0 yapın)
WIDTH = 0
HEIGHT = 0

# FPS Bilgilerini hesaplama
if DEBUG:
    frame_count = 0
    last_time = time.time()

# Ekranda alan seçtirme
dimension = draw_dimension()
print(f'Seçilen alan: {dimension}') if DEBUG else None

# Çıktı kayıt edici tanımlama
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    5.0,
    (dimension[2] - dimension[0], dimension[3] - dimension[1])
) if KEEP else None

while True:
    # Ekran görüntüsü
    screen = ig.grab(dimension)

    # Obje algılama işlemi için resmi numpy dizisine çevirmeliyiz
    screen_np = np.array(screen)

    # BGR tipindeki görüntüyü RGB yapıyoruz
    screen_np_RGB = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)

    # Resimden obje bilgilerini alma
    detect_infos = detect_from_image(screen_np_RGB)

    # TODO Labelmap'ten otomatik çekilecek
    # Levhalara göre tepkiler
    for label, koordinate in detect_infos:
        # Kırmızı Işık
        if label == 1:
            pass
        # Yeşil ışık
        elif label == 2:
            pass
        # Durak
        elif label == 3:
           pass
        # Trafiğe kapalı
        elif label == 4:
            pass
        # Giriş Yasak
        elif label == 5:
           pass
        # Sol Yasak
        elif label == 6:
            pass
        # Sağ Yasak
        elif label == 7:
           pass
        # Park
        elif label == 8:
            pass
        # Park Yasak
        elif label == 9:
           pass
        # Hız 20
        elif label == 10:
            pass
        # Hız 30
        elif label == 11:
            pass
        # Saga dönüş
        elif label == 12:
            pass
        # Sola dönüş
        elif label == 13:
            pass

    # Gösterilecek ekranın boyutunu ayarlama
    screen_width = WIDTH if WIDTH != 0 else dimension[2] - dimension[0]
    screen_height = HEIGHT if WIDTH != 0 else dimension[3] - dimension[1]

    # Kaydedilen ekranı uygun boyutta görüntüleme
    cv2.imshow(
        'object detection',
        cv2.resize(
            screen_np_RGB,
            (
                screen_width,
                screen_height
            )
        )
    )

    # Çıktıyı kaydetme
    out.write(screen_np_RGB) if KEEP else None

    # 'q' tuşuna basıldığında çıkma işlemi
    if cv2.waitKey(25) & 0xFF == ord('q'):
        out.release() if KEEP else None
        cv2.destroyAllWindows()
        break

    # FPS bilgilerini basma
    if DEBUG:
        frame_count += 1
        if time.time() - last_time >= 1:
            print('FPS: {}'.format(frame_count))
            frame_count = 0
            last_time = time.time()

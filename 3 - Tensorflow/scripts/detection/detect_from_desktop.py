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

if DEBUG:
    frame_count = 0
    last_time = time.time()

dimension = draw_dimension()
print(f'Seçilen alan: {dimension}') if DEBUG else None

out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    5.0,
    (dimension[2] - dimension[0], dimension[3] - dimension[1])
) if KEEP else None

while True:
    # Ekran görüntüsü
    screen = ig.grab(dimension)
    screen_np = np.array(screen)

    # BGR tipindeki görüntüyü RGB yapıyoruz
    screen_np_RGB = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)

    # Ekranda algılama yapma ve işaretleme
    detect_on_image(screen_np_RGB)

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

    # Çıktı görüntülerini video olarak kayıt etme
    out.write(screen_np_RGB) if KEEP else None

    # 'q' tuşuna basıldığında çıkma işlemi
    if cv2.waitKey(25) & 0xFF == ord('q'):
        out.release() if KEEP else None
        cv2.destroyAllWindows()
        break

    if DEBUG:
        # noinspection PyUnboundLocalVariable
        frame_count += 1
        # noinspection PyUnboundLocalVariable
        if time.time() - last_time >= 1:
            print('FPS: {}'.format(frame_count))
            frame_count = 0
            last_time = time.time()

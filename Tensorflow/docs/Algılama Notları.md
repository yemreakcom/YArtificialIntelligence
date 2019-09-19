# Algılama Notları

Obje algılama işlemlerindeki notları barındırır.

## Koordinatlar

Numpy ve tensorflow işleyişinde koordinatlar (h,w,d) şeklindedir.

- h: Yükseklik
- w: Genişlik
- d: Derinlik

### Modelin Sonucunu Ekrana Basma

```py
# Boyut bilgileri (h, w, d) şeklindedir
height, width, _ = image.shape

# ...


# Perform the actual detection by running the model with the image_np as input
(boxes, scores, classes, num) = sess.run(
    [detection_boxes, detection_scores, detection_classes, num_detections],
    feed_dict={image_tensor: image_expanded})

# Bulunan objenin bilgilerini yazdırma
if debug:
    for score, box, label in zip(scores[0], boxes[0], classes[0]):
        if score > MIN_SCORE_THRESH:
            print("----------------------")
            # Koordinat verileri (y0, x0, y1, x1) şeklindedir
            print("Koordinatlar: ", box[0] * height, box[1]
                    * width, box[2] * height, box[3] * width)
            print("Uzunluk: ", box[1] - box[0])
            print("Olasılık: %", score)
            print("Etiket: ", label)
            print("Toplam Algılama: ", num)
            print("----------------------\n")

```

## Hata Notları

### N/A Adlı Etiketlerin Gözükmesi

Bu hata `detection_utils` dosyasında `NUM_CLASSES` değişkeni etiket çeşidi kadar olmadığında gelir.
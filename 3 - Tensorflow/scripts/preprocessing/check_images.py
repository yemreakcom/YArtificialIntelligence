"""Usage
python check_images.py -i <IMAGE_PATH>

Examples:
    python check_images.py -i ./images/test
"""

import tensorflow as tf
import argparse
import os

# TODO Konsoldan al
DEBUG = True

def main():
    # Argüman parçalıyıcı tanımlama
    parser = argparse.ArgumentParser(
        description="Tensorflow Modeli için Resim Kontrolcüsü")

    # Argüman ekleme
    parser.add_argument("-i",
                        "--inputDir",
                        help="Resim dosyalarının olduğunu dizinin konumu",
                        type=str)
    # Argümanları alma
    args = parser.parse_args()

    # Dizin girilmezse bulunduğu konumu ele alma
    if args.inputDir is None:
        args.inputDir = os.getcwd()

    # Dizin kontrolü
    assert os.path.isdir(args.inputDir), "Verilen dizin geçersiz."

    # Dizindeki resimleri alma ve test etme
    corrupted_imgs = find_corrupted_imgs(args.inputDir)

    if corrupted_imgs is not None:
        for img in corrupted_imgs:
            print(f"Hasarlı resim yolu: {img}")
    else:
        print("Hasarlı resim yok")


def find_corrupted_imgs(path):
    corrupted_imgs = []
    imgs_names = os.listdir(path)
    with tf.Graph().as_default():
        for img_name in imgs_names:
            if ".jpg" in img_name:
                # Resim yolunu oluşturma
                img_path = path + "\\" + img_name
                succes = True

                # Resmi kontrol etme
                try:
                    image_contents = tf.read_file(img_path)
                    image = tf.image.decode_jpeg(image_contents, channels=3)
                    init_op = tf.initialize_all_tables()
                    with tf.Session() as sess:
                        sess.run(init_op)
                        sess.run(image)
                except:
                    succes = False
                    corrupted_imgs.append(img_path)
                
                # TODO Hatalı olanları daha belirgin yaz ya da rapor dosyasına ekle
                print(f"{img_name} is {'succes' if succes else 'corrupt'}") if DEBUG else None

    return corrupted_imgs if len(corrupted_imgs) > 0 else None

if __name__ == "__main__":
    main()

"""
Usage:
python find_unlabeled_imgs.py -i [PATH_TO_IMAGE_XML_FOLDER]

# Train verilerini kontrol etme
python find_unlabeled_imgs.py -i %homedrive%%homepath%\Tensorflow\workspace\training_demo\images\train

# Test verilerini kontrol etme
python find_unlabeled_imgs.py -i %homedrive%%homepath%\Tensorflow\workspace\training_demo\images\test
"""

import argparse
import os
import glob
import re


def main():
    # CLI Argümanı işleyicisi oluşturma
    parser = argparse.ArgumentParser(
        description="Sample TensorFlow XML path regulator"
    )

    # Girdi yolu argümanı
    parser.add_argument(
        "-i",
        "--inputDir",
        help='XML dosyalarının bulunduğu resim dosyalarının yolu\n(C:\\Users...)',
        type=str
    )

    # Adlandırma argümanı
    parser.add_argument(
        "-p",
        "--prefix",
        help='XML ve resim dosyalarını sıralı adlandırmak için ön ek\n(img -> img0 .. img50)',
        type=str
    )

    args = parser.parse_args()

    # Girdi yolu yoksa bulunan dizini işleme
    if args.inputDir is None:
        args.inputDir = os.getcwd()

    # Dizin kontrolü
    assert (os.path.isdir(args.inputDir))

    check_if_labelled(args.inputDir, "*jpg")


def check_if_labelled(pathname, pattern):
    # Dosya yollarını ve sayacı tanımalama
    file_paths = glob.iglob(os.path.join(pathname, pattern))
    for file_path in file_paths:
        # Dosya uzantısını alma
        _, ext = os.path.splitext(os.path.basename(file_path))

        # Etiket dosyası kontrolü
        if not os.path.isfile(file_path.replace(ext, '.xml')):
            print(f"Etiketlenmemiş resim algılandı: '{file_path}'")

    print("İşlem sonu ~YemreAk")


# Sadece bu dosya derlendiğinde çalışması için
# Başka bir dosyaya aktarıldığında __name__ = 'foo' (başka dosyanın ismi) olur
if __name__ == '__main__':
    main()

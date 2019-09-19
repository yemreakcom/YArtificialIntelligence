"""
Usage:
python xml_path_regulator.py -i [PATH_TO_IMAGE_XML_FOLDER] -p [PREFIX_OF_EVERY_FILE]

# Train verilerini yeniden adlandırma ve düzeltme
python xml_path_regulator.py -i %homedrive%%homepath%\Tensorflow\workspace\training_demo\images\train  -p image

# Test verilerini yeniden adlandırma ve düzeltme
python xml_path_regulator.py -i %homedrive%%homepath%\Tensorflow\workspace\training_demo\images\test  -p image
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

    if args.prefix is not None:
        rename_files(args.inputDir, '*jpg', args.prefix)

    regulate_xmls(args.inputDir)


def rename_files(pathname, pattern, prefix):
    # Dosya yollarını ve sayacı tanımalama
    file_paths = glob.iglob(os.path.join(pathname, pattern))

    # Sayı verisi
    count = 0

    # Her bir dosyayı ve xml'ini yeniden adlandırma
    for file_path in file_paths:
        # Dosya uzantısını alma
        _, ext = os.path.splitext(os.path.basename(file_path))

        # Etiket dosyası varsa yeniden adlandırma
        if os.path.isfile(file_path.replace(ext, '.xml')):
            os.rename(file_path, os.path.join(
                pathname, prefix + ('%.5d' % count) + ext))
            os.rename(file_path.replace(ext, '.xml'), os.path.join(
                pathname, prefix + ('%.5d' % count) + '.xml'))
            count += 1
        else:
            print(f"Etiketlenmemiş resim algılandı ve adlandırılmadı: '{file_path}'")


def regulate_xmls(input_dir):
    # XML verilerini güncelleme
    xml_paths = get_file_paths(input_dir, "xml")
    for xml_path in xml_paths:
        xml = change_xml(xml_path)
        fp = open(xml_path, "w")
        fp.write(xml)


def get_file_paths(input_dir, ext=""):
    if ext != "":
        wild_card = os.path.join(input_dir, '*.{}'.format(ext))
    else:
        wild_card = os.path.join(input_dir, '*')

    return glob.glob(wild_card)


def change_xml(xml_path):
    xml = ''
    img_path = xml_path.replace('.xml', '.jpg')
    folder, filename = parse_xml_path(img_path)

    with open(xml_path) as fp:
        for i, line in enumerate(fp):
            if i == 1:
                line = change_xml_tag_value(line, folder)
            elif i == 2:
                line = change_xml_tag_value(line, filename)
            elif i == 3:
                line = change_xml_tag_value(line, img_path)

            # Yeni XML dosyası için metni ekleme
            if line is not None:
                xml += line

    return xml


def change_xml_tag_value(xml_line, value):
    split_line = re.split('[<>]', xml_line)
    if len(split_line) == 5:
        split_line[2] = value
        return '{}<{}>{}<{}>{}'.format(
            split_line[0], split_line[1], split_line[2],
            split_line[3], split_line[4]
        )


def parse_xml_path(xml_path):
    split_path = xml_path.split("\\")

    filename = split_path.pop()
    folder = split_path.pop()

    return folder, filename


# Sadece bu dosya derlendiğinde çalışması için
# Başka bir dosyaya aktarıldığında __name__ = 'foo' (başka dosyanın ismi) olur
if __name__ == '__main__':
    main()

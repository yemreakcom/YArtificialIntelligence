python ../../../scripts/preprocessing/xml_to_csv.py -i ../images/train -o ../images/train_labels.csv
python ../../../scripts/preprocessing/xml_to_csv.py -i ../images/eval -o ../images/eval_labels.csv
python ../../../scripts/preprocessing/generate_tfrecord.py --label_map=./label_map.pbtxt --img_path=..\images\train --csv_input=../images/train_labels.csv --output_path=./train.record
python ../../../scripts/preprocessing/generate_tfrecord.py --label_map=./label_map.pbtxt --img_path=..\images\eval --csv_input=../images/eval_labels.csv --output_path=./eval.record

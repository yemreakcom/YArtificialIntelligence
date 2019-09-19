import os

import cv2
import numpy as np
import tensorflow as tf

# PythonPath tanımlıysa sadece 'utils' yazılabilir
from models.research.object_detection.utils import label_map_util
from models.research.object_detection.utils import visualization_utils as vis_util

# Define the video stream
cap = cv2.VideoCapture(0)  # Change only if you have more than one webcams

# # What model to download. Models can bee found here:
# # https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
# MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'
# MODEL_FILE = MODEL_NAME + '.tar.gz'
# DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'
#
# # Path to frozen detection graph. This is the actual model that is used for the object detection.
# PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
#
# # List of the strings that is used to add correct label for each box.
# PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')
#
# # Number of classes to detect
# NUM_CLASSES = 2
#
# # Download Model
# opener = urllib.request.URLopener()
# opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
# tar_file = tarfile.open(MODEL_FILE)
# for file in tar_file.getmembers():
#     file_name = os.path.basename(file.name)
#     if 'frozen_inference_graph.pb' in file_name:
#         tar_file.extract(file, os.getcwd())


# Name of the directory containing the object detection module we're using (without .pb)
MODEL_NAME = 'inference_graph'

# Grab path to current working directory
CWD_PATH = r'C:\Users\YEmre\Tensorflow\workspace\traffic_light_detector'  # os.getcwd()

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH, 'annotations', 'label_map.pbtxt')

# Number of classes the object detector can identify
NUM_CLASSES = 2

# Alt algılama sınırı (olasılk %)
MIN_SCORE_THRESH = 0.70

# Load a (frozen) Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

# Loading label map
# Label maps map indices to category names, so that when our convolution network
# predicts `5`, we know that this corresponds to `airplane`. Here we use internal
# utility functions, but anything that returns a dictionary mapping integers to
# appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# # Helper code
# def load_image_into_numpy_array(image):
#     (im_width, im_height) = image.size
#     return np.array(image.getdata()).reshape(
#         (im_height, im_width, 3)).astype(np.uint8)


# Detection
with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        while True:
            # Read frame from camera
            ret, image_np = cap.read()

            # Expand dimensions since the model expects images to have shape: [1,
            # None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            # Input tensor is the image
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Output tensors are the detection boxes, scores, and classes
            # Each box represents a part of the image where a particular object was detected
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represents level of confidence for each of the objects.
            # The score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            # Extract detection classes
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            # Number of objects detected
            num_detections = detection_graph.get_tensor_by_name(
                'num_detections:0')

            # Perform the actual detection by running the model with the image as input
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})

            # Bulunan objenin bilgilerini yazdırma
            for score, box, label in zip(scores[0], boxes[0], classes[0]):
                if score > MIN_SCORE_THRESH:
                    print("Normalize Koordinaatlar: ", box)
                    print("Olasılık: %", score)
                    print("Etiket: ", label)
                    print("Toplam Algılama: ", num)

            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=MIN_SCORE_THRESH)

            # All the results have been drawn on the frame, so it's time to display it.
            cv2.imshow('object detection', cv2.resize(image_np, (800, 600)))

            # Press 'q' to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

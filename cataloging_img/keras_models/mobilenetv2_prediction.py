import os

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

from tools.file_manager import FileManager


class MobileNetV2Prediction:
    def __init__(self, directory):
        self.directory = directory
        self.model = MobileNetV2(weights='imagenet')
        self.predictions = []

    def predict(self, img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = preprocess_input(img_array)
        img_array = np.expand_dims(img_array, axis=0)

        predictions = self.model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=1)[0]

        return decoded_predictions

    def predict_multiple(self):
        img_paths = FileManager().get_image_files(self.directory)

        predictions = []
        for img_path in img_paths:
            predictions.append(self.predict(img_path))

        self.predictions = predictions
        return predictions

    def collect_predictions(self):
        if not self.predictions:
            self.predict_multiple()

        collected_predictions = []
        for prediction in self.predictions:
            labels = [label for _, label, _ in prediction]
            collected_predictions.extend(labels)
        return collected_predictions

    def statistics(self):
        predictions = self.collect_predictions()
        statistics = {}
        for prediction in predictions:
            if prediction in statistics:
                statistics[prediction] += 1
            else:
                statistics[prediction] = 1

        # sort statistics by value
        statistics = dict(sorted(statistics.items(), key=lambda item: item[1], reverse=True))
        return statistics

    def sort_files_by_tags(self):
        statistics = self.statistics()

        length = len(self.predictions)
        threshold = length // 100
        threshold = 10 if length < 100 else threshold
        threshold = 1 if length < 10 else threshold

        tags_to_keep = [tag for tag in statistics if statistics[tag] >= threshold]

        folder_files_map = {}
        others_dir = os.path.join(self.directory, "OTHERS")

        for tag, value in statistics.items():
            if tag in tags_to_keep:
                tag_dir = os.path.join(self.directory, f"{tag}_{value}")
                folder_files_map[tag_dir] = []
            else:
                tag_other_dir = os.path.join(others_dir, f"{tag}_{value}")
                if not os.path.exists(tag_other_dir):
                    os.makedirs(tag_other_dir)
                if tag_other_dir not in folder_files_map:
                    folder_files_map[tag_other_dir] = []

        image_files = FileManager().get_image_files(self.directory)
        for img_path, prediction in zip(image_files, self.predictions):
            tag = prediction[0][1]
            dest_dir = os.path.join(self.directory, f"{tag}_{statistics.get(tag, 'UNKNOWN')}")

            if os.path.exists(img_path):
                if tag in tags_to_keep:
                    folder_files_map[dest_dir].append(img_path)
                else:
                    tag_other_dir = os.path.join(others_dir, f"{tag}_{statistics.get(tag, 'UNKNOWN')}")
                    if tag_other_dir in folder_files_map:
                        folder_files_map[tag_other_dir].append(img_path)
                    else:
                        os.makedirs(tag_other_dir)
                        folder_files_map[tag_other_dir] = [img_path]
            else:
                print(f"File not found: {img_path}")

        return folder_files_map





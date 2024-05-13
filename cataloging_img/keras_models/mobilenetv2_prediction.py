import os

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

from tools.file_manager import FileManager


class MobileNetV2Prediction:
    def __init__(self, directory):
        self.model = MobileNetV2(weights='imagenet')
        self.file_manager = FileManager(directory)
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
        img_paths = self.file_manager.get_image_files()

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

        tags_to_keep = [tag for tag in statistics if statistics[tag] >= threshold]

        folder_files_map = {}

        directory = self.file_manager.directory
        for tag, value in statistics.items():
            if tag in tags_to_keep:
                tag_dir = os.path.join(directory, f"{tag}_{value}")
                folder_files_map[tag_dir] = []

        others_dir = os.path.join(directory, "OTHERS")
        folder_files_map[others_dir] = []

        image_files = self.file_manager.get_image_files()
        for img_path, prediction in zip(image_files, self.predictions):
            tag = prediction[0][1]
            dest_dir = os.path.join(directory, f"{tag}_{statistics.get(tag, 'UNKNOWN')}")

            if os.path.exists(img_path):
                if tag in tags_to_keep:
                    folder_files_map[dest_dir].append(img_path)
                else:
                    folder_files_map[others_dir].append(img_path)
            else:
                print(f"File not found: {img_path}")

        self.file_manager.move_files_to_folders(folder_files_map)


if __name__ == '__main__':
    dir_path = "C:\Workspace\diplom\parser\imgs\Leopard 2 tank photos"
    resnet = MobileNetV2Prediction(dir_path)
    resnet.sort_files_by_tags()



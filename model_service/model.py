import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image
from io import BytesIO

class resNet50ImagenetLabelPridictor:

    def __init__(self):
        self.__model = tf.keras.applications.ResNet50(weights="imagenet")

    def prepare_image(self, img_data: bytes) -> np.ndarray:
        """ Prepares the given image for prediction. """

        img = tf.keras.preprocessing.image.load_img(BytesIO(img_data), target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.resnet50.preprocess_input(img_array)

        return img_array

    def predict_label(self, input_array: np.ndarray) -> str:
        """ Predicts the label for the provided array. """

        predictions = self.__model.predict(input_array)
        decoded_predictions = decode_predictions(predictions, top=1)[0]

        return decoded_predictions[0][1]

    def summary(self):
        self.__model.summary()

if __name__ == "__main__":
    class_instance = resNet50ImagenetLabelPridictor()
    class_instance.summary()
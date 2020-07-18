from models.my_keras import MyImageFile as my_image
from models.my_keras import MyModelFromFile as my_model
from models.my_keras import MyNumbers as numbers

import keras
import numpy as np
from PIL import Image

def load_file_predict(file = 'image_none.jpeg'):
    image = my_image('images/' + file)
    image.grayscale()
    x = image.toTestX()

    model = my_model()
    predict_y = model.predict(x)
    predict_y = numbers(predict_y)

    print('-----------')
    print('対象データ', file)
    print('予測データ', predict_y.trimValue())
    print('予測ラベル', predict_y.resultNumber())
    print('-----------')
    print()

def main_load_file():
    print()
    print(":: --- image ---")
    print()

    image = my_image('images/image_none.jpeg')
    image.viewInfo()
    image.viewExtrema()
    image.viewPixel()

    print()
    print(":: --- grayscale ---")
    print()

    image.grayscale()
    image.viewInfo()
    image.viewExtrema()
    image.viewPixel()

    print()
    print(":: --- reshape ---")
    print()

    x = image.toTestX()
    print(x)

    print()
    print(":: --- model ---")
    print()
    model = my_model()

    print()
    print(":: --- predict ---")
    print()
    predict_y = model.predict(x)

    print()
    print(":: --- y ---")
    print()
    predict_y = numbers(predict_y)

    # print('予測データ', predict_y.value())
    print('予測データ', predict_y.trimValue())
    print('予測ラベル', predict_y.resultNumber())

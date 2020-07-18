import keras
import numpy as np
from PIL import Image, ImageOps


class MyImageFile:
    """my class"""

    def __init__(self, file):
        from PIL import Image
        im = Image.open(file)
        im = ImageOps.invert(im)
        self.im = im
        self.file = file

    def viewInfo(self):
        im = self.im
        print('(フォーマット、サイズ、モード) :: ', (im.format, im.size, im.mode))

    def viewExtrema(self):
        print('(RBC各色の最小値と最大値) :: ', (self.im.getextrema()))

    def viewPixel(self, xy = (10, 10)):
        print('(指定した座標の色を取得) :: ', (self.im.getpixel(xy)))

    def grayscale(self):
        self.im = self.im.convert('L')

    def toTestX(self):
        im = self.im
        im = im.convert('L')
        im = im.resize((28, 28), Image.LANCZOS)

        x = np.array(im)
        x = x.reshape(1, 784)
        x = x.astype('float32')
        x /= 255
        return x

class MyNumbers:
    """my class"""

    def __init__(self, y):
        self.y = y

    def _trim(self, x):
        if x < 0.1:
            return 0
        else:
            return x

    def value(self):
        return self.y

    def trimValue(self):
        return list(map(self._trim, self.y))

    def resultNumber(self):
        max = 0
        i = 0
        r = 0
        for num in self.y:
            if max < num:
                max = num
                r = i
            i = i + 1

        return (r, max)

class MyModelCommon:
    """my class"""

    num_classes = 10
    batch_size = 128
    epochs = 20
    __verbose_fit = 1
    __verbose_evaluate = 0

    def save(self, name = 'my_model.h5'):
        self.model.save(name)

    def summary(self):
        self.model.summary()

    def predict(self, x):
        x = x.reshape(1, 784)
        predict = self.model.predict(x, batch_size=None, verbose=0, steps=None)
        return predict[0]

class MyModelFromFile(MyModelCommon):
    """my class"""

    def __init__(self, name = 'my_model.h5'):
        from keras.models import load_model
        self.model = load_model(name)

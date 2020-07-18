import keras
import numpy as np
from PIL import Image


class MyImageFile:
    """my class"""

    def __init__(self, file):
        from PIL import Image
        self.file = file
        self.im = Image.open(file)

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

class MyMnist:
    """mnist wrapper"""

    num_classes = 10

    def load_data(self):
        from keras.datasets import mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test

    def reshape(self):
        # -------------
        # x_train
        # -------------
        x_train = self.x_train
        x_train = x_train.reshape(60000, 784)
        x_train = x_train.astype('float32')
        x_train /= 255
        self.x_train = x_train

        # -------------
        # x_test
        # -------------
        x_test = self.x_test
        x_test = x_test.reshape(10000, 784)
        x_test = x_test.astype('float32')
        x_test /= 255
        self.x_test = x_test

    def to_categorical(self):
        self.y_train = keras.utils.to_categorical(self.y_train, self.num_classes)
        self.y_test = keras.utils.to_categorical(self.y_test, self.num_classes)

    def sample(self):
        import random
        min = 0
        max = len(self.x_test)-1
        i = random.randint(min, max)
        x = self.x_test[i]
        y = self.y_test[i]
        return (x, y, i)

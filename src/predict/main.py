# work
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# from models.my_keras import MyMnist as mnist
# from models.my_keras import MyModelFromFile as model
# from models.my_keras import MyNumbers as numbers
# from models.my_keras import MyImageFile as image

from models import operation

operation.load_file_predict()

#
# print()
# print(":: --- load_data ---")
# print()
# mnist = mnist()
# mnist.load_data()
# mnist.reshape()
# mnist.to_categorical()
#
# (x, y, i) = mnist.sample()
#
# print()
# print(":: --- model ---")
# print()
# model = model()
# model.summary()
#
# print()
# print(":: --- predict ---")
# print()
# predict_y = model.predict(x)
#
# print()
# print(":: --- y ---")
# print()
# predict_y = numbers(predict_y)
#
# print('正解データ', i, y)
# # print('予測データ', predict_y.value())
# print('予測データ', predict_y.trimValue())
# print('予測ラベル', predict_y.resultNumber())

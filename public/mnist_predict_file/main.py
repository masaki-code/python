import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
from PIL import Image, ImageOps
from keras.models import load_model

# メソッド定義（指定したファイルを予測）
def predict_classes(im_file):
    # 画像ファイル読み込み
    im = Image.open(im_file)

    # 画像ファイル変換
    im = im.resize((28, 28)) # サイズ調整
    im = im.convert('L')     # 白黒変換
    im = ImageOps.invert(im) # 値反転

    # 画像データから検証データ作成
    x = np.array(im)        # NumPy配列に
    x = x.reshape(1, 784)   # 28*28 -> 784
    x = x.astype('float32') # intからfloatに
    x /= 255                # 0-1の範囲のfloatに

    # 訓練済みモデル読み込み
    model_file = 'my_model.h5'
    model = load_model(model_file)

    # 予測
    predict_y = model.predict_classes(x)
    print('--------')
    print('テスト対象', im_file)
    print('予測ラベル', predict_y)

# 実行
predict_classes('images/image_0.jpg')
predict_classes('images/image_1.jpg')
predict_classes('images/image_2.jpg')
predict_classes('images/image_3.jpg')
predict_classes('images/image_4.jpg')
predict_classes('images/image_5.jpg')
predict_classes('images/image_6.jpg')
predict_classes('images/image_7.jpg')
predict_classes('images/image_8.jpg')
predict_classes('images/image_9.jpg')

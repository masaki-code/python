# 以下を参考に画像の読み込み
# https://note.nkmk.me/python-numpy-image-processing/
# https://note.nkmk.me/python-pillow-basic/
# https://note.nkmk.me/python-pillow-image-resize/

img_file = "./image.jpeg"

print()
print(':: --------------------')
print(':: ---- RGB ----')
print(':: --------------------')
print()

from PIL import Image
import numpy as np

im = np.array(Image.open(img_file))

# print(type(im))
# <class 'numpy.ndarray'>

# print(im.dtype)
# uint8

print('行（高さ）, 列（幅）, 色（チャンネル）::',im.shape)
# (225, 400, 3)

print()
print(':: ----------------------')
print(':: ---- グレースケール ----')
print(':: ----------------------')
print()

im_gray = np.array(Image.open(img_file).convert('L'))
print(im_gray.shape)

print()
print(':: --------------------')
print(':: ---- Image.open ----')
print(':: --------------------')
print()

im = Image.open(img_file)
print('(フォーマット、サイズ、モード) :: ', (im.format, im.size, im.mode))
print('(RBC各色の最小値と最大値) :: ', (im.getextrema()))
print('(指定した座標の色を取得) :: ', (im.getpixel((256, 256))))

print()
print(':: --------------------')
print(':: ---- 白黒変換 ----')
print(':: --------------------')
print()

im = im.convert('L')
print('(フォーマット、サイズ、モード) :: ', (im.format, im.size, im.mode))
print('(RBC各色の最小値と最大値) :: ', (im.getextrema()))
print('(指定した座標の色を取得) :: ', (im.getpixel((256, 256))))


im.show()

print()
print(':: --------------------')
print(':: ---- サイズ変換 ----')
print(':: --------------------')
print()

img_resize = im.resize((256, 256), Image.LANCZOS)
img_resize.show()

img_resize = im.resize((28, 28))
img_resize.show()

im = img_resize
print('(フォーマット、サイズ、モード) :: ', (im.format, im.size, im.mode))
print('(RBC各色の最小値と最大値) :: ', (im.getextrema()))
print('(指定した座標の色を取得) :: ', (im.getpixel((14, 14))))


# EOF
print()

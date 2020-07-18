# work
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from models import operation

print('================')
val = input('対象の番号: ')
print('================')
print()

try:
    num = int(val)
except:
    num = -1

if num > 9 or num < 0:
    num = 'none'
else:
    num = str(num)

file = 'image_' + num +'.jpeg'

operation.main_load_file(file)

# operation.main_load_file()
# operation.main_load_file('image_1.jpeg')
# operation.main_load_file('image_2.jpeg')

# operation.load_file_predict(file)
# operation.load_file_predict()
# operation.load_file_predict('image_none.jpeg')
# operation.load_file_predict('image_1.jpeg')
# operation.load_file_predict('image_2.jpeg')

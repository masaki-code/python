# work
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from models import operation

operation.main_load_file()

# operation.load_file_predict()
# operation.load_file_predict('image_none.jpeg')
# operation.load_file_predict('image_1.jpeg')
# operation.load_file_predict('image_2.jpeg')

from keras.models import load_model
from keras.preprocessing import image
import numpy as np

model = load_model('model.h5')

img = 'predictImg.jpg'

img = image.load_img(img, target_size=(128, 128))

img = image.img_to_array(img)

img = np.expand_dims(img, axis=0)

img = img / 255

print(model.predict_classes(img))

print(model.predict(img))
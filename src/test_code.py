import numpy as np
from keras.preprocessing import image
from keras_vggface.vggface import VGGFace
from keras_vggface import utils
from keras_squeezenet import SqueezeNet
import cv2

model = VGGFace(model='resnet50')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
_, buffer = cv2.imencode('.jpg', frame)

resized = cv2.resize(frame, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
x = image.img_to_array(resized)
x = np.expand_dims(x, axis=0)
x = utils.preprocess_input(x, version=2) # or version=2
preds = model.predict(x)
print('Predicted:', utils.decode_predictions(preds))

print("[INFO] loading network...")
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
model = SqueezeNet()
resized = cv2.resize(frame, dsize=(227, 227), interpolation=cv2.INTER_CUBIC)
x = image.img_to_array(resized)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
print('Predicted:', decode_predictions(preds))

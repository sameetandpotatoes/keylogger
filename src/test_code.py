import numpy as np
from keras.preprocessing import image
from keras_squeezenet import SqueezeNet
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
import cv2
import base64

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
_, buffer = cv2.imencode('.jpg', frame)
server_encoded = base64.b64encode(buffer)

server_buffer = np.frombuffer(base64.decodestring(server_encoded), dtype="uint8")
server_frame = cv2.imdecode(server_buffer, cv2.IMREAD_UNCHANGED)

model = SqueezeNet()
resized = cv2.resize(server_frame, dsize=(227, 227), interpolation=cv2.INTER_CUBIC)
x = image.img_to_array(resized)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = decode_predictions(model.predict(x))
for id, pred, score in preds[0]:
    print('Predicted: %s' % pred)

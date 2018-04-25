import platform
from uuid import getnode as get_mac
import cv2
import base64
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    arbitrary_addr = ('1.2.3.4', 1)
    try:
        s.connect(arbitrary_addr)
        ip = s.getsockname()[0]
    except:
        # If we can't find an IP, just set it as a local-host so we have something
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def get_mac_for_ip(ip=get_ip()):
    mac = get_mac()
    return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

"""
    Takes a picture of the user using the webcam (turns on the light)
    Returns a base64 string
"""
def get_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    _, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer)


class User:
    def __init__(self, ip=get_ip(), mac=get_mac_for_ip(),
                processor=platform.processor(), os=platform.system(),
                x86=platform.machine(), image=None):
        self.processor = processor
        self.os = os
        self.x86 = x86
        self.ip = ip
        self.mac = mac
        self.image = image

    @classmethod
    def from_json(cls, jd):
        return cls(**jd)

    def capture_image(self):
        self.image = get_image()

    def set_tags(self):
        """
            Run a convolutional neural network on the server-side per image
            to associate tags (doesn't take more than a few seconds), and
            runs in parallel since thread is started per client request
        """
        import numpy as np
        from keras.preprocessing import image
        from keras_squeezenet import SqueezeNet
        from keras.applications.imagenet_utils import preprocess_input, decode_predictions
        # dtype must be uint8
        # Encode image to ascii for Python 3 compatibility
        server_buffer = np.frombuffer(base64.decodestring(self.image.encode('ascii')), dtype="uint8")
        server_frame = cv2.imdecode(server_buffer, cv2.IMREAD_UNCHANGED)

        model = SqueezeNet()
        resized = cv2.resize(server_frame, dsize=(227, 227), interpolation=cv2.INTER_CUBIC)
        x = image.img_to_array(resized)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = decode_predictions(model.predict(x))
        # preds is an array containing an array of tags and scores
        self.tags = []
        for id, pred, score in preds[0]:
            self.tags.append(pred)

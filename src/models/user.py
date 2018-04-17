import platform
import cv2
import base64

def get_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    retval, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer)

class User:
    def __init__(self, processor=platform.processor(), os=platform.system(),
                x86=platform.machine(), image=get_image()):
        self.processor = processor
        self.os = os
        self.x86 = x86
        self.image = image

    @classmethod
    def from_json(cls, jd):
        return cls(**jd)

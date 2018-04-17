import socket
import socketserver
import logging
import threading
import struct
import json
import IPython
from server.app import start_flask_app
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
        logger.info(message)

    def recvall(self, sock, n):
        # Helper function to recv n bytes or return None if EOF is hit
        data = b''
        while len(data) < n:
            packet = sock.recv(n - len(data))
            if not packet:
                return None
            data += packet
        return data

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def main():
    server_address = ('0.0.0.0', SOCKET_PORT)
    server = ThreadedTCPServer(server_address, ThreadedTCPRequestHandler)
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    logger.info("Starting socket server on address {}".format(server_address))

    start_flask_app()

if __name__ == "__main__":
    main()

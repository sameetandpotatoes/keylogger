import socket
import threading
import socketserver
from app import start_flask_app

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024))
        cur_thread = threading.current_thread()
        print("{}: {}".format(cur_thread.name, data))
        # TODO write to mongo with data

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def main():
    server_address = ('localhost', 10000)
    server = ThreadedTCPServer(server_address, ThreadedTCPRequestHandler)
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()

    # TODO start Flask api now
    start_flask_app()

if __name__ == "__main__":
    main()

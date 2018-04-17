from server.app import start_flask_app
from server.socket_handler import start_socket_server

def main():
    start_socket_server()
    start_flask_app()

if __name__ == "__main__":
    main()

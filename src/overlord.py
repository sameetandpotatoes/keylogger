from server.app import start_flask_app
from server.socket_handler import start_socket_server
# TODO only added for testing, remove when integrated
from server.database import setup_database


def main():
    setup_database()
    start_socket_server()
    start_flask_app()


if __name__ == "__main__":
    main()

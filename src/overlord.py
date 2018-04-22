from server.app import start_flask_app
from server.socket_handler import start_socket_server
# TODO only added for testing, remove when integrated
from server.database import setup_database, insert_user, insert_phrase
from models.user import User
from models.phrasestroke import PhraseStroke

def main():
    #start_socket_server()
    #start_flask_app()
    users, phrases, db, client = None, None, None, None
    setup_database()
    UserOne = User()
    print(UserOne.__dict__)
    UserOne = {"processor" : "proc",
               "os" : "Windows",
               "x86" : "x86sure",
               "ip" : "123.456.789.111",
               "image" : "dfhdbc"}
    PhraseOne = {"end_timestamp" : "01/02/03:01:02:03",
                 "duration": "10",
                 "phrase" : "password",
                 "terminating" : "return"}
    PhraseTwo = {"end_timestamp" : "03/03/04:04:42:43",
                 "duration": "5",
                 "phrase" : "pwd",
                 "terminating" : "enter"}

if __name__ == "__main__":
    main()

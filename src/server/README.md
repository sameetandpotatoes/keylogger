# README

`overlord.py` is the main server that ingests all of the data from clients, and provides an interface to query such data.

It will be running on an IP address and will have two connections open:
- It will have a Flask API running on port `6969`.
- It will have a socket connection on port `9696`.

The socket connection will be to receive byte data from the clients, and store it in mongo.

The api will be able to learn important information about a user from mongo.

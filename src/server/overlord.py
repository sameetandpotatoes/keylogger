import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

sock.bind(server_address)
# TODO make it multithreaded
sock.listen(10)
client, client_info = sock.accept()
ip_addr, port = client_info

print("Connection from: {}".format(ip_addr))
buffer = ''
while True:
    data = client.recv(1024)
    if data:
        buffer += data
        print buffer
    else:
        break
print(buffer)

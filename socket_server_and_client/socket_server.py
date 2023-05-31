# Code to create a socket server using python

import socket

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Server started. Waiting for connections...")

    conn, address = server_socket.accept()
    print("Connected to client: {}".format(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected client: " + data)
        message = input('-> ')
        conn.send(message.encode())

    conn.close()

if __name__ == '__main__':
    server_program()

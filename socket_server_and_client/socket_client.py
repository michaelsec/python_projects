# Code to create a socket client using python

import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        message = input("-> ")
        client_socket.send(message.encode())
        if message.lower() == "exit":
            break

        data = client_socket.recv(1024).decode()
        print("Server response: " + data)

    client_socket.close()


if __name__ == '__main__':
    client_program()

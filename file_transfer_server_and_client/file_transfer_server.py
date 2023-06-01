import socket
import os

IP = '0.0.0.0' 
PORT = 5001
ADDR = (IP, PORT)
SIZE = 1024

def main():
    print("[STARTING] Server is starting.")

    """ Starting a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    """ Server is listening, i.e., server is now waiting for the client to connect. """
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()

        """ Start a new thread to handle the client connection. """
        handle_client(conn, addr)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    with conn:
        """ Receiving the filename and file size from the client. """
        filename_size_msg = conn.recv(SIZE).decode()
        filename, file_size = filename_size_msg.split("::")
        file_size = int(file_size)
        print(f"[RECV] Receiving the filename: {filename}")
        print(f"[RECV] Receiving the file size: {file_size} bytes")

        """ Add '(copy)' to the filename. """
        base_name, extension = os.path.splitext(filename)
        new_filename = f"{base_name}(copy){extension}"

        with open(new_filename, "wb") as file:
            conn.send(b"Filename and file size received.")

            """ Receiving the file data from the client. """
            received_bytes = 0
            while received_bytes < file_size:
                data = conn.recv(SIZE)
                received_bytes += len(data)
                print(f"[RECV] Receiving file data. Received: {received_bytes}/{file_size} bytes")
                file.write(data)

            conn.send(b"File data received.")

    print(f"[DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()

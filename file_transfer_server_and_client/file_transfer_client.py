import socket
import os
import time

IP = '0.0.0.0'
PORT = 5001
ADDR = (IP, PORT)
SIZE = 1024

def main():
    """ Starting a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    """ Opening and reading the file data. """
    file_name = ""  # Enter the file name here
    file_path = os.path.abspath(file_name)
    file_size = os.path.getsize(file_path)

    """ Sending the filename and file size to the server. """
    filename_size_msg = f"{file_name}::{file_size}"
    client.send(filename_size_msg.encode())
    msg = client.recv(SIZE).decode()
    print(f"[SERVER]: {msg}")

    time.sleep(1)  # Add a one second delay to allow the server to process the filename and file size

    """ Sending the file data to the server. """
    with open(file_path, "rb") as file:
        sent_bytes = 0
        while sent_bytes < file_size:
            data = file.read(SIZE)
            client.send(data)
            sent_bytes += len(data)
            print(f"[SENT] Sent {sent_bytes} bytes of data")

    msg = client.recv(SIZE).decode()
    print(f"[SERVER]: {msg}")

    """ Closing the connection from the server. """
    client.close()

if __name__ == "__main__":
    main()

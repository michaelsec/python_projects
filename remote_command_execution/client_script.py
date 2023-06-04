import socket

def send_command(server_address, command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(server_address)
        client_socket.sendall(command.encode())
        result = client_socket.recv(1024).decode()

        print("Command Output:")
        print(result)

    finally:
        client_socket.close()

server_address = ('<server_ip>', 8888)  # Replace with the server's IP address

while True:
    command = input("Enter a command (or 'exit' to quit): ")

    if command == 'exit':
        break

    send_command(server_address, command)

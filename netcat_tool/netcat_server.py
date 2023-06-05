import socket
import subprocess
import argparse


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started on {host}:{port}")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address[0]}:{client_address[1]}")

    while True:
        client_socket.sendall(b'$ ')
        command = client_socket.recv(1024).decode().strip()
        if not command:
            break
        print(f"Received command from client: {command}")

        if command.lower() == 'exit':
            break

        output = execute_command(command)
        client_socket.sendall(output.encode())

    client_socket.close()
    server_socket.close()


def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return str(e)


def main():
    parser = argparse.ArgumentParser(description='Python Netcat Server')
    parser.add_argument('host', help='Host to bind the server')
    parser.add_argument('-p', '--port', type=int, default=80, help='Port to bind the server (default: 80)')
    args = parser.parse_args()

    start_server(args.host, args.port)


if __name__ == '__main__':
    main()

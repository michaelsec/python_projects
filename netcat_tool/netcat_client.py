import argparse
import socket

def start_netcat(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print(f"Connected to {host}:{port}")

        while True:
            data = input("Enter your message: ")
            sock.sendall(data.encode())

            response = sock.recv(1024).decode()
            print("Received:", response)

    except KeyboardInterrupt:
        print("\nClosing connection...")
        sock.close()

def main():
    parser = argparse.ArgumentParser(description='Python Netcat Tool')
    parser.add_argument('host', help='Target host')
    parser.add_argument('-p', '--port', type=int, default=80, help='Target port (default: 80)')
    args = parser.parse_args()

    start_netcat(args.host, args.port)

if __name__ == '__main__':
    main()

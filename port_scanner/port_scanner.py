import socket

def scan_port(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        
        # Attempt to connect to the host and port
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        # Close the socket
        sock.close()
        
    except socket.error:
        print("Error occurred while connecting")

def scan_ports_range(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

# Enter the ports that you wish to start and end the scan with here
host = input("Enter the host to scan: ")
start_port = 1
end_port = 10000

scan_ports_range(host, start_port, end_port)

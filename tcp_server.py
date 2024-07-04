import socket

# Define the server's IP address and port
server_ip = '127.0.0.1'
server_port = 12345

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {server_ip}:{server_port}")

# Accept connections from clients
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    # Receive and record data from the client
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        received_data = data.decode('utf-8')
        print(f"Received data: {received_data}")

        # Here, you can store the received data in a file or database
        # For this example, we'll just print it

    print(f"Connection to {client_address} closed")
    client_socket.close()

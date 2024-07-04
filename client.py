import socket

# Define the server's IP address and port
server_ip = '127.0.0.1'
server_port = 12345

while(True):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server {server_ip}:{server_port}")

    # Send data to the server
    message = input()
    client_socket.send(message.encode('utf-8'))

    # Receive and print the response from the server
    response = client_socket.recv(1024)
    received_response = response.decode('utf-8')
    print(f"Received response: {received_response}")

    # Close the client socket
    client_socket.close()

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
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Receive data from the client
data = client_socket.recv(1024)
received_data = data.decode('utf-8')
print(f"Received data: {received_data}")

# Send a response back to the client
response = "Hallo Saya mengirim balik data"
client_socket.send(response.encode('utf-8'))

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()

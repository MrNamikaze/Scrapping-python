import socket
from datetime import datetime
import os

while(True):
    # Define the server's IP address and port
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%d-%m-%Y")
    formatted_time = current_date.strftime("%H:%M:%S")
    filename = formatted_date+".txt"
    server_ip = '192.168.88.21'
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

    if os.path.exists(filename):
        # Receive data from the client
        data = client_socket.recv(1024)
        received_data = data.decode('utf-8')
        with open(filename, 'a') as file:
            file.write("["+formatted_time+"]"+received_data+"\n")

        # Send a response back to the client
        response = "Hallo Saya mengirim balik data"
        client_socket.send(response.encode('utf-8'))

        # Close the client socket
        client_socket.close()
        # Close the server socket
        server_socket.close()
    else:
        # Receive data from the client
        data = client_socket.recv(1024)
        received_data = data.decode('utf-8')
        with open(filename, 'w') as file:
            file.write("["+formatted_time+"]"+received_data+"\n")

        # Send a response back to the client
        response = "Hallo Saya mengirim balik data"
        client_socket.send(response.encode('utf-8'))
        # Close the client socket
        client_socket.close()
        # Close the server socket
        server_socket.close()
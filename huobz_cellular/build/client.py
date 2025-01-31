import socket

def start_client(server_ip):
    port = 8080  # Port to connect to
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    # Send data to the server
    message = "Hello from HuobzMessenger!"
    client_socket.send(message.encode('utf-8'))

    # Receive the server's response
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {data}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    # Replace '192.168.1.1' with the server's IP address
    start_client('192.168.1.1')

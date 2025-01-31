import socket

def start_server():
    host = '0.0.0.0'  # Listen on all network interfaces
    port = 8080       # Port to listen on
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Allow only one connection at a time
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive data
    data = conn.recv(1024).decode('utf-8')
    print(f"Received: {data}")

    # Respond to the client
    conn.send("Message received!".encode('utf-8'))

    # Close the connection
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

#include <iostream>
#include <bluetooth/bluetooth.h>
#include <bluetooth/rfcomm.h>
#include <unistd.h>
#include <sys/socket.h>
#include <errno.h>

// Define a valid bdaddr_t variable to hold BDADDR_ANY
bdaddr_t any_addr = {{0, 0, 0, 0, 0, 0}};

void startBluetoothServer() {
    int sock, client;
    struct sockaddr_rc loc_addr = { 0 }, rem_addr = { 0 };
    char buffer[1024] = { 0 };
    socklen_t opt = sizeof(rem_addr);

    // Create Bluetooth socket
    sock = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM);
    if (sock < 0) {
        perror("Failed to create socket");
        return;
    }

    // Bind socket to the local Bluetooth adapter
    loc_addr.rc_family = AF_BLUETOOTH;
    bacpy(&loc_addr.rc_bdaddr, &any_addr); // Corrected line using a valid bdaddr_t variable
    loc_addr.rc_channel = (uint8_t)1;
    if (bind(sock, (struct sockaddr *)&loc_addr, sizeof(loc_addr)) < 0) {
        perror("Failed to bind socket");
        close(sock);
        return;
    }

    // Start listening for connections
    if (listen(sock, 1) < 0) {
        perror("Failed to listen");
        close(sock);
        return;
    }
    std::cout << "Waiting for connection..." << std::endl;

    // Accept connection
    client = accept(sock, (struct sockaddr *)&rem_addr, &opt);
    if (client < 0) {
        perror("Failed to accept connection");
        close(sock);
        return;
    }

    char client_addr[18] = { 0 };
    ba2str(&rem_addr.rc_bdaddr, client_addr);
    std::cout << "Connected to " << client_addr << std::endl;

    // Receive data
    memset(buffer, 0, sizeof(buffer));
    int bytes_read = read(client, buffer, sizeof(buffer));
    if (bytes_read > 0) {
        std::cout << "Received: " << buffer << std::endl;
    }

    // Close the connection
    close(client);
    close(sock);
}

int main() {
    startBluetoothServer();
    return 0;
}

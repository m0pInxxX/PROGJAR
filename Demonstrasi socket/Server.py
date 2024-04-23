import socket

def server_program():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server sedang menunggu koneksi...")

    while True:
        client_socket, addr = server_socket.accept()
        print('Terhubung dengan', addr)

        data = client_socket.recv(1024).decode()
        print('Diterima dari klien:', data)

        client_socket.send("Pesan diterima".encode())

        client_socket.close()

if __name__ == '__main__':
    server_program()

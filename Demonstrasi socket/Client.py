import socket

def client_program():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Masukkan pesan: ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print('Diterima dari server:', data)

    client_socket.close()

if __name__ == '__main__':
    client_program()

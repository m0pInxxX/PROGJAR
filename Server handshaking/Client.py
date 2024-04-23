import socket
import ssl

def client_program():
    host = 'localhost'
    port = 8000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.load_verify_locations("server.crt")
    secure_socket = ssl_context.wrap_socket(client_socket, server_hostname=host)
    secure_socket.connect((host, port))

    print("Koneksi terenkripsi dengan server.")

    while True:
        message = input("Anda: ")
        secure_socket.send(message.encode())

        if message.lower() == 'exit':
            break

        data = secure_socket.recv(1024).decode()
        print('Server:', data)

    secure_socket.close()

if __name__ == '__main__':
    client_program()

import socket
import ssl

def server_program():
    host = 'localhost'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server sedang menunggu koneksi...")

    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    while True:
        conn, addr = server_socket.accept()
        secure_socket = ssl_context.wrap_socket(conn, server_side=True)

        print('Terhubung dengan', addr)

        while True:
            data = secure_socket.recv(1024).decode()
            if not data:
                break

            print('Client:', data)

            message = input("Anda: ")
            secure_socket.send(message.encode())

            if message.lower() == 'exit':
                break

        secure_socket.close()
        print('Koneksi dengan', addr, 'ditutup.')

    server_socket.close()

if __name__ == '__main__':
    server_program()

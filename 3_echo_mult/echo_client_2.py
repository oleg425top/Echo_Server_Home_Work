import socket

HOST = '127.0.0.1'

PORT = 50432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        data_to_send = input("Message to send (exit - disconnect from server, stop - stop server!\n: ")
        if not data_to_send:
            data_to_send = ' '
        if data_to_send.lower() == 'exit':
            print("Отключение от сервера.")
            break
        data_bytes_send = data_to_send.encode()
        try:
            sock.sendall(data_bytes_send)
            data_bytes_received = sock.recv(1024)
        except ConnectionError:
            print('Сервер недоступен!')
            break
        data_received = data_bytes_received.decode()
        print("Received:", data_received)



import socket
import threading

HOST = '127.0.0.1'  # Использовать все адреса: виден и снаружи, и изнутри
PORT = 50432  # Port to listen on (non-privileged ports are > 1023)


# Проверяем, что скрипт был запущен на исполнение, а не импортирован

def handle_handle_connection(sock, addr):
    with sock:
        print("Подключение по", addr)
        # Receive
        while True:
            try:
                data = sock.recv(1024)
            except ConnectionError:
                print("Клиент внезапно отключился в процессе отправки данных на сервер")
                break
            print(f'Received: {data}, from: {addr}')
            data = data.upper()
            # Send
            print(f'Send: {data} to: {addr}')
            try:
                sock.sendall(data)
            except ConnectionError:
                print(f'Клиент внезапно отключился не могу отправить данные')
                break
        print("Отключению по", addr)


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen(1)
        while True:
            print('Waiting for connection...')
            sock, addr = serv_sock.accept()
            t = threading.Thread(target=handle_handle_connection, args=(sock, addr))
            print(t)
            t.start()
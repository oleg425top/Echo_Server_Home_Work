import socket
import time

HOST = '127.0.0.1'  # Использовать все адреса: виден и снаружи, и изнутри
PORT = 50432  # Port to listen on (non-privileged ports are > 1023)

# Проверяем, что скрипт был запущен на исполнение, а не импортирован
if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen()
        # Принимает множественные соединения, но только echo_server в текущий момент
        while True:
            print('Ожидаю подключения...')
            sock, addr = serv_sock.accept()
            with sock:
                print("Подключение по", addr)
                # Receive
                while True:
                    try:
                        data = sock.recv(1024)
                        message = data.decode().strip()
                        if not data:
                            print('Disconnect....')
                            break
                        elif message == 'stop':
                            print('Сервер отключен по команде от', addr)
                            sock.sendall(b'Server is off!!!')
                            raise SystemExit(0)  # Завершает работу сервера нашел в Google!!

                        else:
                            print(f'Received: {data}, from: {addr}')
                            data = data.upper()
                            # Send
                            print(f'Send: {data} to: {addr}')
                    except ConnectionError:
                        print("Клиент внезапно отключился в процессе отправки данных на сервер")
                        break

                    try:
                        time.sleep(5)  # добавил, чтобы успеть отключить клиента, проверял ошибку!!!
                        sock.sendall(data)
                    except ConnectionError:
                        print(f'Клиент внезапно отключился не могу отправить данные')
                        break
                print("Отключению по", addr)
            # break

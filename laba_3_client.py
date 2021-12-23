import socket, threading

import laba_3_Cezar

nickname = input("Введіть ім'я користувача: ")
nickname = " >"+nickname
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Инициализация сокета
client.connect(('192.168.1.10', 53261))  # Соединение клиента с сервером
def receive():
        s = input("a = розкодовувати , b = не зозкодовувати ")
        while True:  # Подтверждение соединения
            try:
                message = client.recv(1024).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(nickname.encode('utf-8'))
                else:
                    if s == "a":
                        print(laba_3_Cezar.cesar(message, -k))
                    else:
                        print(message)
            except:  # Если неправильный ip или порт
                print("Ошибка!")
                client.close()
                break
def write():
    while True:  # Вывод сообщений в чат
        message = laba_3_Cezar.cesar('{}: {}'.format(nickname, input('')), k)
        client.send(message.encode('utf-8'))

k = 1
receive_thread = threading.Thread(target=receive)  # Получение всех сообщений
receive_thread.start()
write_thread = threading.Thread(target=write) # Отправка всех сообщени
write_thread.start()

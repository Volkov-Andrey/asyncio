import asyncio
 
 HOST = 'localhost'  # Хост для подключения
 PORT = 9095         # Порт для подключения
 
 async def tcp_echo_client():
     """
     Асинхронная функция для подключения к серверу и обмена сообщениями.
     """
     reader = None
     writer = None
 
     loop = asyncio.get_running_loop()
 
     try:
         while True:
             # Пытаемся установить соединение с сервером
 @@ -24,35 +26,35 @@
 
         while True:
             # Читаем сообщение от пользователя в отдельном потоке, чтобы не блокировать цикл событий
             message = await asyncio.to_thread(input, "Введите сообщение (или 'exit' для выхода): ")
             message = await loop.run_in_executor(None, input, "Введите сообщение (или 'exit' для выхода): ")
             if message.lower() == 'exit':
                 # Если введена команда 'exit', выходим из цикла
                 print("Отключение от сервера.")
                 break
 
             # Отправляем сообщение серверу
             writer.write(message.encode())
             await writer.drain()  # Ждем, пока данные будут отправлены
 
             # Ожидаем ответ от сервера
             data = await reader.read(100)
             if not data:
                 # Если данных нет, сервер закрыл соединение
                 print("Сервер закрыл соединение.")
                 break
             print(f"Получено эхо: {data.decode()!r}")
 
     except KeyboardInterrupt:
         # Обрабатываем прерывание по Ctrl+C
         print("\nКлиент прерван пользователем (Ctrl+C)")
     except ConnectionResetError:
         # Обрабатываем случай, когда соединение было разорвано
         print("Соединение было закрыто сервером.")
     finally:
         if writer is not None:
             writer.close()  # Закрываем соединение
             await writer.wait_closed()
         print("Клиент завершил работу.")
 
 if __name__ == '__main__':
     # Запускаем асинхронную функцию tcp_echo_client с помощью asyncio.run()

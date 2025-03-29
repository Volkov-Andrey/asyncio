import asyncio
 
 HOST = 'localhost'  # Хост для подключения
 PORT = 9095         # Порт для подключения
 
 HOST = 'localhost'
 PORT = 9095
 async def tcp_echo_client(message):
     """
     Асинхронная функция для подключения к серверу и обмена сообщениями.
     """
     # Устанавливаем соединение с сервером
     reader, writer = await asyncio.open_connection(HOST, PORT)
 
     print(f'Отправка: {message!r}')
     writer.write(message.encode())  # Кодируем сообщение в байты и отправляем серверу
     await writer.drain()            # Ждем, пока данные будут отправлены
 
 async def tcp_echo_client(host, port):
     reader, writer = await asyncio.open_connection(host, port)
     message = 'Hello, world'
 
     writer.write(message.encode())
     await writer.drain()
 
     # Читаем ответ от сервера (до 100 байт)
     data = await reader.read(100)
     writer.close()
     # await writer.wait_closed()
     print(f'Получено: {data.decode()!r}')  # Декодируем данные и выводим
 
 # asyncio.run(tcp_echo_client(HOST, PORT))
     print('Закрытие соединения')
     writer.close()                # Закрываем соединение
     await writer.wait_closed()    # Ждем, пока соединение будет полностью закрыто
 
 loop = asyncio.get_event_loop()
 task = loop.create_task(tcp_echo_client(HOST, PORT))
 loop.run_until_complete(task)
 if __name__ == '__main__':
     message = 'Привет, мир!'     # Сообщение для отправки
     # Запускаем асинхронную функцию tcp_echo_client с помощью asyncio.run()
     asyncio.run(tcp_echo_client(message))

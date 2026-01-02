
import asyncio
import importlib
import json
import nest_asyncio
import os
import subprocess
import threading
import time
import uvicorn

from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse

from google.colab import files, output, userdata

from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.sessions import SessionMiddleware

server = None
thread = None
port_g = 5000

def run_server():
    global server, port_g
    config = uvicorn.Config(app, host="0.0.0.0", port=port_g, log_level="info")
    server = uvicorn.Server(config)
    server.run()  # блокирующий вызов

def start_server():
    global thread
    if thread and thread.is_alive():
        print("Сервер уже запущен")
        return
    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    print("Сервер запущен")

async def disconnect_all_clients(clients = {}):
    if not clients:
        print("Клиентов нет, отключение не требуется")
        return
    try:
        # Запускаем отключение с таймаутом, чтобы не зависнуть
        await asyncio.wait_for(
            asyncio.gather(*(client.disconnect() for client in list(clients.values()))),
            timeout=10
        )
        clients.clear()
        print("Все клиенты отключены")
    except asyncio.TimeoutError:
        print("Ошибка: отключение клиентов заняло слишком много времени")

#крашит среду для апп (сложных типа чайнлит) - нестыковки с дебаггером в колаб
def stop_server(): #только для фастАпи (простых - с хтмл и т.п.)
    global server, thread
    if server is None:
        print("Сервер не запущен")
        return

    print("Отключаем всех клиентов...")
    loop = asyncio.get_event_loop()

    if loop.is_running():
        # Запускаем отключение в уже работающем event loop через run_coroutine_threadsafe
        future = asyncio.run_coroutine_threadsafe(disconnect_all_clients(), loop)
        try:
            future.result(timeout=15)  # Ждём максимум 15 секунд
        except asyncio.TimeoutError:
            print("Ошибка: отключение клиентов превысило время ожидания")
    else:
        loop.run_until_complete(disconnect_all_clients())
    print("Все клиенты отключены или их не было")

    print("Останавливаем сервер...")
    server.should_exit = True

    thread.join(timeout=5)
    if thread.is_alive():
        print("Внимание: сервер не остановился за 5 секунд!")
    else:
        print("Сервер успешно остановлен")

    server = None
    thread = None

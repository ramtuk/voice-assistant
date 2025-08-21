import os
import requests
from pathlib import Path

def send_audio_to_assistant(file_path: str):
    """Отправка аудиофайла на сервер ассистента"""
    if not Path(file_path).exists():
        print(f"Ошибка: файл {file_path} не найден")
        print(f"Текущая директория: {os.getcwd()}")
        print(f"Доступные файлы: {os.listdir()}")
        return

    url = "http://localhost:8000/command"
    try:
        with open(file_path, "rb") as audio_file:
            files = {"file": audio_file}
            response = requests.post(url, files=files)
            print("Статус ответа:", response.status_code)
            print("Ответ сервера:", response.json())
    except Exception as e:
        print(f"Ошибка при отправке: {str(e)}")

if __name__ == "__main__":
    # Путь к тестовому файлу
    audio_file = "test_audio.wav"
    
    # Проверка существования файла
    if not os.path.exists(audio_file):
        print("Создаю тестовый аудиофайл...")
        os.system("arecord -D hw:2,0 -f S16_LE -c 1 -r 16000 -d 2 test_audio.wav")
    
    # Отправка файла
    send_audio_to_assistant(audio_file)
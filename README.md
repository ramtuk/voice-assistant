# voice-assistant
Voice Assistant - Open-source voice AI assistant built with Python, FastAPI, and Whisper. Features real-time speech recognition, command processing, and modular architecture. Supports custom skills, home automation integration, and runs on Raspberry Pi/Ubuntu. Perfect for smart home control and voice interfaces.

# Голосовой ассистент

🎯 Полностью функциональный голосовой ассистент с оффлайн распознаванием речи.

## Особенности

- 🗣️ Оффлайн распознавание русской речи через Vosk
- 🎙️ Поддержка USB микрофонов
- 🔧 Модульная архитектура
- ⚡ Быстрая обработка команд
- 📦 Легкая расширяемость

## Установка

git clone <repository-url>
cd voice-assistant
pip install -r requirements.txt

## Скачайте модель Vosk

mkdir -p models
cd models
wget https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip
unzip vosk-model-small-ru-0.22.zip
rm vosk-model-small-ru-0.22.zip
cd ..

## Запуск

python main.py

## Использование

Произнесите команды:

"Привет" - приветствие

"Время" - текущее время

"Стоп" - выход

## Архитектура

voice-assistant/
├── main.py              # Главный скрипт
├── assistant.py         # Основной класс
├── config.py           # Конфигурация
├── commands/           # Обработчики команд
├── utils/              # Вспомогательные утилиты
└── models/             # Модели AI


# voice-assistant
Voice Assistant - Open-source voice AI assistant built with Python, FastAPI, and Whisper. Features real-time speech recognition, command processing, and modular architecture. Supports custom skills, home automation integration, and runs on Raspberry Pi/Ubuntu. Perfect for smart home control and voice interfaces.

# Голосовой ассистент

🎯 Умный голосовой ассистент с продвинутым распознаванием речи.

## 🚀 Новые возможности

### Улучшенное распознавание
- Фильтрация ложных срабатываний (игнорирует отдельные звуки)
- Приоритетная система audio устройств
- Автоматический fallback на резервные методы

### Оптимизированная работа
- Быстрое переключение между устройствами
- Умная обработка ошибок
- Стабильная работа с USB микрофонами

### Поддерживаемые устройства
- `hw:CARD=PRO,DEV=0` - основное устройство
- `plughw:CARD=PRO,DEV=0` - с преобразованием sample rate
- `sysdefault:CARD=PRO` - системное устройство

## 🎙️ Распознаваемые команды
- "Привет" - приветствие
- "Время" - текущее время
- "Дата" - текущая дата  
- "Стоп" - выход из программы

## ⚙️ Настройка
Скопируйте и настройте `.env` файл:
```bash
cp .env.example .env

# Отредактируйте .env под вашу систему

## 📊 Логирование

Система использует многоуровневое логирование с записью в файл и консоль.

### Уровни логирования:
- `DEBUG` - отладочная информация
- `INFO` - основные события и диалоги  
- `ERROR` - ошибки и исключения

### Просмотр логов:
```bash
# В реальном времени
tail -f /var/log/voice-assistant/app.log

# Последние 20 записей
tail -20 /var/log/voice-assistant/app.log

# Поиск ошибок
grep "ERROR" /var/log/voice-assistant/app.log


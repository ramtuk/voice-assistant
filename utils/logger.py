import logging
import os
from datetime import datetime
from config import Config

def setup_logger():
    """Настройка системы логирования"""
    
    # Создаем папку для логов если ее нет
    log_dir = os.path.dirname(Config.LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Настраиваем форматирование
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Создаем логгер
    logger = logging.getLogger('voice_assistant')
    logger.setLevel(getattr(logging, Config.LOG_LEVEL.upper()))
    
    # Файловый handler (дописывание в конец)
    file_handler = logging.FileHandler(Config.LOG_FILE, mode='a', encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # Консольный handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Добавляем handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    # Логируем запуск
    logger.info("=" * 50)
    logger.info("🚀 Голосовой помощник запущен")
    logger.info(f"📝 Уровень логирования: {Config.LOG_LEVEL}")
    logger.info(f"💾 Файл логов: {Config.LOG_FILE}")
    logger.info("=" * 50)
    
    return logger

# Глобальный логгер
logger = setup_logger()

def log_command(user_text, assistant_response):
    """Логирование команды и ответа"""
    logger.info(f"👤 Пользователь: {user_text}")
    logger.info(f"🤖 Ассистент: {assistant_response}")
    logger.info("-" * 30)

def log_error(error_message, exception=None):
    """Логирование ошибок"""
    if exception:
        logger.error(f"❌ {error_message}: {exception}")
    else:
        logger.error(f"❌ {error_message}")

def log_debug(message):
    """Отладочное сообщение"""
    logger.debug(f"🐛 {message}")

def log_info(message):
    """Информационное сообщение"""
    logger.info(f"ℹ️ {message}")
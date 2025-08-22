import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Основные настройки
    APP_ENV = os.getenv('APP_ENV', 'production')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', '/var/log/voice-assistant/app.log')
    
    # Audio настройки
    AUDIO_DEVICE = os.getenv('AUDIO_DEVICE', 'hw:CARD=PRO,DEV=0')
    AUDIO_SAMPLE_RATE = int(os.getenv('AUDIO_SAMPLE_RATE', '16000'))
    AUDIO_CHANNELS = int(os.getenv('AUDIO_CHANNELS', '1'))
    AUDIO_BUFFER_SIZE = int(os.getenv('AUDIO_BUFFER_SIZE', '1024'))
    AUDIO_SILENCE_THRESHOLD = int(os.getenv('AUDIO_SILENCE_THRESHOLD', '500'))
    
    # Распознавание речи
    RECOGNITION_TYPE = os.getenv('RECOGNITION_TYPE', 'vosk')
    LANGUAGE = os.getenv('LANGUAGE', 'ru')
    VOSK_MODEL_PATH = os.getenv('VOSK_MODEL_PATH', 'models/vosk-model-small-ru-0.22')
    
    # Синтез речи
    TTS_ENGINE = os.getenv('TTS_ENGINE', 'none')
    VOICE_RATE = int(os.getenv('VOICE_RATE', '180'))
    VOICE_VOLUME = float(os.getenv('VOICE_VOLUME', '0.9'))
    TTS_VOICE = os.getenv('TTS_VOICE', 'ru')
    
    # Производительность
    LISTEN_TIMEOUT = int(os.getenv('LISTEN_TIMEOUT', '4'))
    COMMAND_TIMEOUT = int(os.getenv('COMMAND_TIMEOUT', '30'))
    MAX_RESPONSE_LENGTH = int(os.getenv('MAX_RESPONSE_LENGTH', '200'))
    
    # Безопасность
    API_KEY = os.getenv('API_KEY', 'your_secret_key_here')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    RATE_LIMIT = os.getenv('RATE_LIMIT', '100/minute')
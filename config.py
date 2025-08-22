import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Настройки распознавания
    RECOGNITION_TYPE = os.getenv('RECOGNITION_TYPE', 'vosk')  # vosk, whisper, google
    LANGUAGE = os.getenv('LANGUAGE', 'ru')
    
    # Пути к моделям
    VOSK_MODEL_PATH = os.getenv('VOSK_MODEL_PATH', '../models/vosk-model-small-ru-0.22')
    
    # Настройки Whisper
    WHISPER_MODEL_SIZE = os.getenv('WHISPER_MODEL_SIZE', 'base')
    
    # Настройки TTS
    TTS_ENGINE = os.getenv('TTS_ENGINE', 'pyttsx3')
    
    # Настройки голоса
    VOICE_RATE = int(os.getenv('VOICE_RATE', 180))
    VOICE_VOLUME = float(os.getenv('VOICE_VOLUME', 0.9))
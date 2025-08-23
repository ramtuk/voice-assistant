import speech_recognition as sr
import sounddevice as sd
import numpy as np
import os
from utils.logger import logger
from config import Config
from .vosk_recognizer import VoskRecognizer
from .whisper_recognizer import WhisperRecognizer

# Инициализация компонентов
vosk_recognizer = VoskRecognizer() if Config.RECOGNITION_TYPE == 'vosk' else None
whisper_recognizer = WhisperRecognizer() if Config.RECOGNITION_TYPE == 'whisper' else None

# Для Google распознавания
recognizer = None
if Config.RECOGNITION_TYPE == 'google':
    recognizer = sr.Recognizer()

# TTS отключен для упрощения
tts_engine = None

def listen():
    """Распознавание речи в зависимости от конфигурации"""
    logger.debug("Начало прослушивания...")

    if Config.RECOGNITION_TYPE == 'vosk' and vosk_recognizer:
        return vosk_recognizer.listen_vosk()
    elif Config.RECOGNITION_TYPE == 'whisper' and whisper_recognizer:
        return whisper_recognizer.listen_whisper()
    elif Config.RECOGNITION_TYPE == 'google':
        return listen_google()
    else:
        print(f"❌ Неизвестный тип распознавания: {Config.RECOGNITION_TYPE}")
        return ""

def listen_google():
    """Альтернативная реализация без pyaudio"""
    try:
        print("🎤 Слушаю (Google alternative)...")

        # Запись аудио с помощью sounddevice
        sample_rate = 16000
        duration = 5  # seconds

        audio_data = sd.rec(int(duration * sample_rate),
                           samplerate=sample_rate,
                           channels=1,
                           dtype='int16',
                           device=0)  # USB MIC PRO
        sd.wait()

        # Конвертация для speech_recognition
        audio_data_bytes = audio_data.flatten().tobytes()
        
        # Создаем AudioData объект для speech_recognition
        audio = sr.AudioData(audio_data_bytes, sample_rate, 2)

        try:
            query = recognizer.recognize_google(audio, language='ru-RU')
            print(f"👤 Вы сказали: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("❌ Речь не распознана")
            return ""
        except sr.RequestError as e:
            print(f"❌ Ошибка сервиса Google: {e}")
            return ""

    except Exception as e:
        print(f"❌ Ошибка при прослушивании: {e}")
        return ""

def say(text):
    """Синтез речи - только текстовый вывод"""
    logger.info(f"🤖 Ассистент: {text}")
    print(f"🤖 Ассистент: {text}")
    # Звуковой вывод отключен для упрощения
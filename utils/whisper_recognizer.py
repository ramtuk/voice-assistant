import whisper
import sounddevice as sd
import numpy as np
from config import Config

class WhisperRecognizer:
    def __init__(self):
        self.model = whisper.load_model(Config.WHISPER_MODEL_SIZE)
        self.sample_rate = 16000
        
    def listen_whisper(self):
        """Распознавание речи с помощью Whisper"""
        print("🎤 Слушаю (Whisper)...")
        
        try:
            # Запись аудио
            duration = 5  # seconds
            audio_data = sd.rec(int(duration * self.sample_rate), 
                               samplerate=self.sample_rate, 
                               channels=1, 
                               dtype='float32')
            sd.wait()
            
            # Распознавание
            result = self.model.transcribe(audio_data.flatten())
            text = result['text'].lower().strip()
            
            if text:
                print(f"👤 Вы сказали: {text}")
                return text
            
            return ""
            
        except Exception as e:
            print(f"❌ Ошибка Whisper распознавания: {e}")
            return ""
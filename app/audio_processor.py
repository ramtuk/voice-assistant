import whisper
import vosk
import numpy as np
import asyncio
from io import BytesIO

class AudioProcessor:
    def __init__(self):
        self.whisper_model = whisper.load_model("base")
        self.vosk_model = vosk.Model("models/vosk-model-ru-0.42")
    
    async def process_audio(self, audio_data: bytes) -> str:
        # Используем Whisper для качественного распознавания
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        result = self.whisper_model.transcribe(audio_array.astype(np.float32) / 32768.0)
        return result["text"]
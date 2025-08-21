import pyttsx3
import io
import threading

class TTSEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', 'ru')
    
    async def synthesize(self, text: str) -> bytes:
        loop = asyncio.get_event_loop()
        audio_data = await loop.run_in_executor(None, self._synthesize_sync, text)
        return audio_data
    
    def _synthesize_sync(self, text: str) -> bytes:
        audio_buffer = io.BytesIO()
        
        def callback(audio):
            audio_buffer.write(audio)
        
        self.engine.connect('started-utterance', callback)
        self.engine.say(text)
        self.engine.runAndWait()
        
        return audio_buffer.getvalue()
from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json
from app.audio_processor import AudioProcessor
from app.nlp_engine import NLEngine
from app.tts_engine import TTSEngine

app = FastAPI(title="Voice Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация компонентов
audio_processor = AudioProcessor()
nl_engine = NLEngine()
tts_engine = TTSEngine()

@app.websocket("/ws/voice")
async def websocket_voice(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            text = await audio_processor.process_audio(data)
            response = await nl_engine.process_command(text)
            
            if response.get('speak', False):
                audio_data = await tts_engine.synthesize(response['text'])
                await websocket.send_bytes(audio_data)
            else:
                await websocket.send_text(json.dumps(response))
                
    except Exception as e:
        print(f"WebSocket error: {e}")
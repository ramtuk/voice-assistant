import os
import logging
import tempfile
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Загрузка переменных окружения
load_dotenv()

app = FastAPI(title="Voice Assistant API")

# CORS настройки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.getenv("LOG_FILE", "app.log")),
        logging.StreamHandler()
    ]
)

# Глобальная переменная для модели
whisper_model = None

@app.on_event("startup")
async def startup_event():
    global whisper_model
    try:
        import whisper
        # Прямой путь к модели
        model_path = "/opt/voice-assistant/models/whisper/base.pt"
        
        if os.path.exists(model_path):
            logging.info(f"Loading model from: {model_path}")
            whisper_model = whisper.load_model(model_path)
        else:
            logging.warning("Model not found at custom path, using default")
            whisper_model = whisper.load_model("base")
            
        logging.info(f"Whisper model loaded successfully on {whisper_model.device}")
        
    except Exception as e:
        logging.error(f"Failed to load Whisper model: {e}")
        logging.exception("Full traceback:")

@app.post("/process_audio")
async def process_audio(file: UploadFile = File(...)):
    """Обработка аудио в текст"""
    if whisper_model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        result = whisper_model.transcribe(tmp_path, language="ru")
        os.unlink(tmp_path)
        
        return {
            "text": result["text"],
            "language": result["language"],
            "success": True
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audio processing error: {str(e)}")

@app.post("/process_command")
async def process_command(audio: UploadFile = File(...)):
    """Обработка голосовой команды"""
    if whisper_model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Сначала преобразуем аудио в текст
        transcription = await process_audio(audio)
        text = transcription["text"].lower()
        
        # Простая логика команд
        response = {"original_text": text, "action": None, "response": None}
        
        if "привет" in text:
            response.update({"action": "greeting", "response": "И вам привет!"})
        elif "время" in text:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            response.update({"action": "time", "response": f"Сейчас {current_time}"})
        elif "погода" in text:
            response.update({"action": "weather", "response": "На улице 25°C, солнечно"})
        else:
            response.update({"action": "unknown", "response": "Не понял команду"})
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Command processing error: {str(e)}")

@app.get("/")
async def root():
    return {"status": "running", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": whisper_model is not None}

@app.get("/routes")
async def get_routes():
    return [{"path": route.path, "methods": list(route.methods)} for route in app.routes]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
import os

class ModelConfig:
    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")
    WHISPER_DEVICE = os.getenv("WHISPER_DEVICE", "cpu")
    VOSK_MODEL_PATH = os.getenv("VOSK_MODEL_PATH", "/opt/voice-assistant/models")
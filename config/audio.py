import os

class AudioConfig:
    INPUT_DEVICE = os.getenv("AUDIO_INPUT", "hw:2,0")
    OUTPUT_DEVICE = os.getenv("AUDIO_OUTPUT", "hw:1,0")
    SAMPLE_RATE = int(os.getenv("AUDIO_SAMPLE_RATE", 16000))
    CHANNELS = int(os.getenv("AUDIO_CHANNELS", 1))
    BUFFER_SIZE = int(os.getenv("AUDIO_BUFFER_SIZE", 1024))
    SILENCE_THRESHOLD = int(os.getenv("AUDIO_SILENCE_THRESHOLD", 500))
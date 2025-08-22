import json
import vosk
import sounddevice as sd
import numpy as np
from config import Config
import subprocess
import tempfile
import os

class VoskRecognizer:
    def __init__(self):
        self.model = vosk.Model(Config.VOSK_MODEL_PATH)
        self.sample_rate = 16000  # Vosk требует именно 16000 Hz
        self.rec = vosk.KaldiRecognizer(self.model, self.sample_rate)

    def listen_vosk(self):
        """Оффлайн распознавание речи с помощью Vosk"""
        print("🎤 Слушаю (Vosk)...")

        # Пробуем разные устройства в порядке приоритета
        devices_to_try = [
            'plughw:CARD=PRO,DEV=0',  # Основное устройство
            'hw:CARD=PRO,DEV=0',      # Прямой доступ
            'default',                # Устройство по умолчанию
            'sysdefault:CARD=PRO',    # Системное устройство
        ]

        for device in devices_to_try:
            try:
                result = self.record_with_arecord_device(device)
                if result:
                    return result
                print(f"ℹ️ Устройство {device} не дало результата, пробуем следующее...")
            except Exception as e:
                print(f"❌ Ошибка с устройством {device}: {e}")
                continue

        # Если все устройства не сработали, пробуем fallback
        return self.record_with_sounddevice_fallback()

    def record_with_arecord_device(self, device):
        """Запись через arecord с указанным устройством"""
        try:
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmpfile:
                temp_path = tmpfile.name

            cmd = [
                'arecord',
                '-d', '5',
                '-f', 'S16_LE',
                '-r', '16000',
                '-c', '1',
                '-D', device,
                '-q',
                temp_path
            ]

            process = subprocess.run(cmd, check=True, timeout=7)

            file_size = os.path.getsize(temp_path)
            if file_size <= 44:
                os.unlink(temp_path)
                return ""

            with open(temp_path, 'rb') as f:
                audio_data = f.read()

            os.unlink(temp_path)

            if len(audio_data) > 44:
                audio_bytes = audio_data[44:]

                if self.rec.AcceptWaveform(audio_bytes):
                    result = json.loads(self.rec.Result())
                    text = result.get('text', '').lower()
                    if text:
                        print(f"👤 Вы сказали: {text}")
                        return text

            return ""

        except subprocess.TimeoutExpired:
            print("❌ Таймаут записи arecord")
            return ""
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode() if e.stderr else str(e)
            print(f"❌ Ошибка arecord: {error_msg}")
            return ""
        except Exception as e:
            print(f"❌ Ошибка с устройством {device}: {e}")
            return ""

    def record_with_sounddevice_fallback(self):
        """Резервный метод записи через sounddevice"""
        try:
            # Записываем с native sample rate устройства (48000 Hz)
            duration = 5
            device_sample_rate = 48000
            
            audio_data = sd.rec(int(duration * device_sample_rate),
                               samplerate=device_sample_rate,
                               channels=1,
                               dtype='int16',
                               device=0)
            sd.wait()
            
            # Resampling: 48000 -> 16000 (децимация 3:1)
            audio_data_16k = audio_data[::3].flatten()
            audio_bytes = audio_data_16k.tobytes()
            
            if self.rec.AcceptWaveform(audio_bytes):
                result = json.loads(self.rec.Result())
                text = result.get('text', '').lower()
                if text:
                    print(f"👤 Вы сказали: {text}")
                    return text
            
            return ""
            
        except Exception as e:
            print(f"❌ Ошибка sounddevice fallback: {e}")
            return ""

    def record_direct_48000(self):
        """Экспериментальный метод: пробуем использовать 48000 Hz напрямую"""
        try:
            # Создаем временный recognizer с 48000 Hz
            rec_48000 = vosk.KaldiRecognizer(self.model, 48000)
            
            duration = 5
            audio_data = sd.rec(int(duration * 48000),
                               samplerate=48000,
                               channels=1,
                               dtype='int16',
                               device=0)
            sd.wait()
            
            audio_bytes = audio_data.tobytes()
            
            if rec_48000.AcceptWaveform(audio_bytes):
                result = json.loads(rec_48000.Result())
                text = result.get('text', '').lower()
                if text:
                    print(f"👤 Вы сказали (48000): {text}")
                    return text
            
            return ""
            
        except Exception as e:
            print(f"❌ Ошибка direct 48000: {e}")
            return ""
import json
import vosk
import sounddevice as sd
import numpy as np
from config import Config
import subprocess
import tempfile
import os
from utils.logger import logger

class VoskRecognizer:
    def __init__(self):
        self.model = vosk.Model(Config.VOSK_MODEL_PATH)
        self.sample_rate = 16000
        self.rec = vosk.KaldiRecognizer(self.model, self.sample_rate)
        
        # Оптимальные устройства в порядке приоритета
        self.devices_priority = [
            'hw:CARD=PRO,DEV=0',      # Основное устройство - РАБОТАЕТ!
            'plughw:CARD=PRO,DEV=0',  # С преобразованием
            'sysdefault:CARD=PRO',    # Системное устройство
        ]

    def listen_vosk(self):
        """Оффлайн распознавание речи с помощью Vosk"""
        logger.debug("🎤 Слушаю (Vosk)...")
        
        
        # Пробуем все устройства по порядку
        for device in self.devices_priority:
            try:
                result = self.record_with_arecord_device(device)
                if result and self.is_valid_command(result):
                    print(f"✅ Успех с устройством: {device}")
                    return result
                elif result:
                    print(f"ℹ️ Устройство {device} распознало: '{result}' (не команда)")
                else:
                    print(f"ℹ️ Устройство {device} не распознало речь")
            except Exception as e:
                print(f"❌ Ошибка с устройством {device}: {e}")
                continue
        
        # Если все устройства не дали валидной команды, пробуем fallback
        print("🔄 Использую резервный метод записи...")
        return self.record_with_sounddevice_fallback()

    def is_valid_command(self, text):
        """Проверяет, является ли текст валидной командой"""
        if not text or len(text.strip()) < 2:
            return False
        
        # Игнорируем отдельные буквы и короткие звуки
        ignored_patterns = ['а', 'о', 'у', 'э', 'ы', 'и', 'к', 'на', 'да', 'нет']
        if text.lower() in ignored_patterns:
            return False
            
        return True

    def record_with_arecord_device(self, device):
        """Запись через arecord с указанным устройством"""
        try:
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmpfile:
                temp_path = tmpfile.name

            cmd = [
                'arecord',
                '-d', '3',           # Уменьшили до 3 секунд
                '-f', 'S16_LE',
                '-r', '16000',
                '-c', '1',
                '-D', device,
                '-q',
                temp_path
            ]

            process = subprocess.run(cmd, check=True, timeout=4, 
                                   stderr=subprocess.PIPE, stdout=subprocess.PIPE)

            # Проверяем размер файла
            file_size = os.path.getsize(temp_path)
            if file_size <= 44:
                os.unlink(temp_path)
                return ""

            with open(temp_path, 'rb') as f:
                audio_data = f.read()
            
            os.unlink(temp_path)

            if len(audio_data) > 44:
                audio_bytes = audio_data[44:]
                
                # Передаем данные порциями
                chunk_size = 4000
                for i in range(0, len(audio_bytes), chunk_size):
                    chunk = audio_bytes[i:i + chunk_size]
                    self.rec.AcceptWaveform(chunk)
                
                result = json.loads(self.rec.Result())
                text = result.get('text', '').lower().strip()
                
                if text:
                    print(f"👤 Распознано: {text}")
                    return text

            return ""

        except subprocess.TimeoutExpired:
            return ""
        except subprocess.CalledProcessError as e:
            # Игнорируем ошибки "нет такого устройства"
            if "Нет такого файла или каталога" not in str(e):
                print(f"❌ Ошибка arecord ({device}): {e}")
            return ""
        except Exception as e:
        #    print(f"❌ Ошибка обработки ({device}): {e}")
            logger.error(f"Ошибка с устройством {device}: {e}")
            return ""

    def record_with_sounddevice_fallback(self):
        """Резервный метод записи через sounddevice"""
        try:
            duration = 3
            device_sample_rate = 48000
            
            audio_data = sd.rec(int(duration * device_sample_rate),
                               samplerate=device_sample_rate,
                               channels=1,
                               dtype='int16',
                               device=0)
            sd.wait()
            
            # Resampling: 48000 -> 16000
            audio_data_16k = audio_data[::3].flatten()
            audio_bytes = audio_data_16k.tobytes()
            
            if self.rec.AcceptWaveform(audio_bytes):
                result = json.loads(self.rec.Result())
                text = result.get('text', '').lower().strip()
                if text and self.is_valid_command(text):
                    print(f"👤 Вы сказали (fallback): {text}")
                    return text
            
            return ""
            
        except Exception as e:
            print(f"❌ Ошибка sounddevice fallback: {e}")
            return ""
import time
from utils.speech import listen, say
from commands.base_commands import handle_base_command

class VoiceAssistant:
    def __init__(self):
        print("Инициализация голосового помощника...")
        self.setup()

    def setup(self):
        """Настройка ассистента"""
        print("✅ Ассистент инициализирован")

    def handle_command(self, command):
        """Обработка команд через модульную систему"""
        if not command:
            return False
        
        # Обработка базовых команд
        result = handle_base_command(command)
        if result:
            return True
        
        # Здесь можно добавить обработку других типов команд
        # Например: handle_weather_command(command)
        
        return False

    def run(self):
        """Основной цикл работы ассистента"""
        print("\n" + "="*50)
        print("🚀 Голосовой помощник запущен и готов к работе!")
        print("🔊 Говорите чётко и ясно после звукового сигнала")
        print("❌ Скажите 'стоп' или 'выход' для завершения работы")
        print("="*50)
        
        say("Голосовой помощник запущен. Готов к вашим командам!")
        
        while True:
            try:
                command = listen()
                
                if command:
                    result = self.handle_command(command)
                    if result and any(word in command for word in ['стоп', 'выход', 'закройся']):
                        break
                
                time.sleep(0.1)
                
            except KeyboardInterrupt:
                print("\n\n👋 Завершение работы по запросу пользователя")
                say("До свидания!")
                break
            except Exception as e:
                print(f"❌ Критическая ошибка: {e}")
                time.sleep(3)
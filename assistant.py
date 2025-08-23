import time
from utils.speech import listen, say
from commands.base_commands import handle_base_command
from utils.logger import logger, log_command  # Добавляем импорт

class VoiceAssistant:
    def __init__(self):
        logger.info("Инициализация голосового помощника...")
        self.setup()
        logger.info("✅ Ассистент инициализирован")

    def setup(self):
        """Настройка ассистента"""
        pass

    def handle_command(self, command):
        """Обработка команд через модульную систему"""
        if not command:
            return False
        
        # Обработка базовых команд
        result = handle_base_command(command)
        if result:
            log_command(command, result)  # Логируем команду и ответ
            return True
        
        return False

    def run(self):
        """Основной цикл работы ассистента"""
        logger.info("\n" + "="*50)
        logger.info("🚀 Голосовой помощник запущен и готов к работе!")
        logger.info("🔊 Говорите чётко и ясно после звукового сигнала")
        logger.info("❌ Скажите 'стоп' или 'выход' для завершения работы")
        logger.info("="*50)
        
        # Приветственное сообщение
        say("Голосовой помощник запущен. Готов к вашим командам!")
        logger.info("🤖 Ассистент: Голосовой помощник запущен. Готов к вашим командам!")
        
        while True:
            try:
                command = listen()
                
                if command:
                    result = self.handle_command(command)
                    if result and any(word in command for word in ['стоп', 'выход', 'закройся']):
                        break
                
                time.sleep(0.1)
                
            except KeyboardInterrupt:
                logger.info("\n\n👋 Завершение работы по запросу пользователя")
                say("До свидания!")
                logger.info("🤖 Ассистент: До свидания!")
                break
            except Exception as e:
                logger.error(f"❌ Критическая ошибка: {e}")
                time.sleep(3)
                continue
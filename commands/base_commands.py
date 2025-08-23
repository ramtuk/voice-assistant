import datetime
from utils.speech import say
from utils.logger import logger

def handle_base_command(command):
    """Обработка базовых команд"""
    command = command.lower()
    
    if any(word in command for word in ['привет', 'здравствуй', 'добрый день', 'hello']):
        say("Приветствую! Чем могу помочь?")
        logger.info(f"Обработана команда: привет")
        return True
        
    elif any(word in command for word in ['время', 'который час', 'сколько времени']):
        now = datetime.datetime.now().strftime("%H:%M")
        say(f"Сейчас {now}")
        logger.info(f"Обработана команда: время")
        return True
        
    elif any(word in command for word in ['дата', 'число', 'какое сегодня']):
        today = datetime.datetime.now().strftime("%d %B %Y")
        say(f"Сегодня {today}")
        logger.info(f"Обработана команда: дата")
        return True
        
    elif any(word in command for word in ['спасибо', 'молодец', 'умница']):
        say("Всегда рад помочь! Обращайтесь ещё!")
        logger.info(f"Обработана команда: спасибо")
        return True
        
    elif any(word in command for word in ['стоп', 'выход', 'закройся', 'пока']):
        say("До свидания! Буду ждать вашего возвращения.")
        logger.info(f"Обработана команда: стоп")
        return True
        
    return False
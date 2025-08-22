import datetime
from utils.speech import say

def handle_base_command(command):
    """Обработка базовых команд"""
    command = command.lower()
    
    if any(word in command for word in ['привет', 'здравствуй', 'добрый день', 'hello']):
        say("Приветствую! Чем могу помочь?")
        return True
        
    elif any(word in command for word in ['время', 'который час', 'сколько времени']):
        now = datetime.datetime.now().strftime("%H:%M")
        say(f"Сейчас {now}")
        return True
        
    elif any(word in command for word in ['дата', 'число', 'какое сегодня']):
        today = datetime.datetime.now().strftime("%d %B %Y")
        say(f"Сегодня {today}")
        return True
        
    elif any(word in command for word in ['спасибо', 'молодец', 'умница']):
        say("Всегда рад помочь! Обращайтесь ещё!")
        return True
        
    elif any(word in command for word in ['стоп', 'выход', 'закройся', 'пока']):
        say("До свидания! Буду ждать вашего возвращения.")
        return True
        
    return False
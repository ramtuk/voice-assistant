import re
from typing import Dict, Any

class NLEngine:
    def __init__(self):
        self.commands = {
            r'погод[ауы]': self.weather_handler,
            r'врем[яи]': self.time_handler,
            r'выключи свет': self.light_handler,
            r'привет': self.greeting_handler
        }
    
    async def process_command(self, text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        
        for pattern, handler in self.commands.items():
            if re.search(pattern, text_lower):
                return await handler(text)
        
        return {"text": "Не понял команду", "speak": True}
    
    async def weather_handler(self, text: str):
        return {"text": "Сейчас 25 градусов, солнечно", "speak": True}
    
    async def time_handler(self, text: str):
        from datetime import datetime
        time = datetime.now().strftime("%H:%M")
        return {"text": f"Сейчас {time}", "speak": True}
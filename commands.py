COMMANDS = {
    "включи музыку": "play_music",
    "какое время": "get_time",
    "остановись": "stop"
}

def recognize_command(text: str) -> str:
    for cmd in COMMANDS:
        if cmd in text.lower():
            return COMMANDS[cmd]
    return "unknown"
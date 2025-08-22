from assistant import VoiceAssistant

if __name__ == "__main__":
    try:
        assistant = VoiceAssistant()
        assistant.run()
    except Exception as e:
        print(f"❌ Не удалось запустить ассистент: {e}")
        print("Проверьте подключение микрофона и доступ к интернету")
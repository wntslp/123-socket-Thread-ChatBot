def chat_response(message):
    """ฟังก์ชันตอบกลับข้อความ"""
    message = message.lower()
    if "hello" in message:
        return "Hello! "
    elif "how are you" in message:
        return "I'm doing great!"
    elif "bye" in message:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that."
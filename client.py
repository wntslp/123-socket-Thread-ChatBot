import socket

def start_client():
    """Client เชื่อมต่อไปยัง Server และส่งข้อความ"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 25000))

    welcome_message = client.recv(1024).decode()
    print(welcome_message)

    while True:
        message = input("You: ")
        if message.lower() == "exit":
            client.send(message.encode())
            break
        client.send(message.encode())
        response = client.recv(1024).decode()
        print(f"Bot: {response}")

    client.close()

if __name__ == "__main__":
    start_client()

import socket
import threading
from chat_bot import chat_response

def handle_client(client_socket, addr):
    """ฟังก์ชันแยก Thread เพื่อรับข้อความจาก Client"""
    print(f"[NEW CONNECTION] {addr} connected.")
    client_socket.send("Welcome to ChatBot! Type 'exit' to quit.\n".encode())

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message or message.lower() == "exit":
                print(f"[DISCONNECTED] {addr} has left the chat.")
                break
            print(f"[{addr}] {message}")
            response = chat_response(message)
            client_socket.send(response.encode())
        except:
            break

    client_socket.close()

def start_server():
    """ตั้งค่า Server ให้รองรับหลาย Client"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 25000))
    server.listen(5)
    print("[SERVER STARTED] Listening on port 25000...")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()

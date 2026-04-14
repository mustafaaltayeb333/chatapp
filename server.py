import socket
import threading
import os

HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT', 50000))

clients = []
clients_lock = threading.Lock()

def broadcast(message, sender_conn=None):
    """Send message to all connected clients except the sender."""
    with clients_lock:
        for client in clients[:]:
            if client != sender_conn:
                try:
                    client.send(message)
                except:
                    clients.remove(client)

def handle_client(conn, addr):
    print(f"[+] Client connected: {addr}")
    with clients_lock:
        clients.append(conn)

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            msg = f"[{addr[0]}:{addr[1]}]: {data.decode()}"
            print(msg)
            broadcast(msg.encode(), sender_conn=conn)
        except:
            break

    print(f"[-] Client disconnected: {addr}")
    with clients_lock:
        if conn in clients:
            clients.remove(conn)
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[*] Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        t.start()

if __name__ == '__main__':
    main()

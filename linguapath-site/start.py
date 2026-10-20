"""One-command launcher for the LinguaPath local website."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import socket
import threading
import time
import webbrowser

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)


def find_server():
    # Prefer port 8000; if it is occupied, try a few nearby ports.
    for port in range(8000, 8011):
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler)
            return server, port
        except OSError:
            continue
    raise RuntimeError("Не удалось найти свободный порт в диапазоне 8000–8010.")


def main():
    server, port = find_server()
    url = f"http://127.0.0.1:{port}/"
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print("=" * 52)
    print("LinguaPath запущен!")
    print(f"Сайт: {url}")
    print("Чтобы остановить сервер, нажмите Ctrl+C в этом окне.")
    print("=" * 52)
    time.sleep(0.3)
    webbrowser.open(url)
    try:
        while thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nОстанавливаю LinguaPath...")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(exc)
        input("Нажмите Enter для выхода...")

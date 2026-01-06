"""
07) 배너 읽기(아주 기초)
- 어떤 서비스는 접속하자마자 첫 메시지를 보내기도 함 (예: 일부 FTP/SMTP)
- HTTPS(443)는 TLS라서 평문 배너가 바로 오지 않음 → 예제는 학습용으로만
"""
from __future__ import annotations
import argparse, socket

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="google.co.kr")
    ap.add_argument("--port", type=int, default=80)  # http는 평문이라 읽을 수 있음
    ap.add_argument("--timeout", type=float, default=5.0)
    args = ap.parse_args()

    with socket.create_connection((args.host, args.port), timeout=args.timeout) as s:
        s.settimeout(args.timeout)
        # HTTP는 배너를 먼저 주지 않으므로, 간단한 요청을 보내고 응답 첫 줄을 읽어봄
        s.sendall(b"POST / HTTP/1.1\r\nHost: google.co.kr\r\nConnection: close\r\n\r\n")
        data = s.recv(200)
        print("received(bytes):", len(data))
        print(data.decode("utf-8", errors="replace"))

if __name__ == "__main__":
    main()

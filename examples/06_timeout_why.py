"""
06) 타임아웃이 왜 중요한가?
- timeout 없으면 "끝없이 기다리는" 상황이 생길 수 있음
"""
from __future__ import annotations
import argparse, socket, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="127.0.0.1")  # 보통 응답이 없는 테스트용 주소 대역
    ap.add_argument("--port", type=int, default=8081)
    ap.add_argument("--timeout", type=float, default=1.0)
    args = ap.parse_args()

    t0 = time.time()
    try:
        socket.create_connection((args.host, args.port), timeout=args.timeout)
        print("connected")
    except Exception as e:
        print("failed:", e)
    finally:
        print("elapsed_ms:", int((time.time()-t0)*1000))

if __name__ == "__main__":
    main()

"""
05) 여러 포트 빠르게 체크(간단 버전)
- 교육용: allowlist(host)만 체크하도록 제한

github 에 파이썬 웹 서버 구성

"""
from __future__ import annotations
import argparse, socket, time

ALLOWLIST = {"127.0.0.1", "localhost"}

def check(host: str, port: int, timeout: float) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="localhost")
    ap.add_argument("--ports", default="80,443,8081")
    ap.add_argument("--timeout", type=float, default=0.8)
    args = ap.parse_args()

    if args.host not in ALLOWLIST:
        raise SystemExit(f"Blocked by allowlist: {args.host}")

    ports = [int(p.strip()) for p in args.ports.split(",") if p.strip()]
    for p in ports:
        ok = check(args.host, p, args.timeout)
        print(f"{args.host}:{p} -> {'OPEN' if ok else 'CLOSED'}")

if __name__ == "__main__":
    main()

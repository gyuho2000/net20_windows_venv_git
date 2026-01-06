"""
08) urllib로 HTTP GET (표준 라이브러리)
"""
from __future__ import annotations
import argparse
from urllib.request import urlopen, Request

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="https://naver.com")
    args = ap.parse_args()

    req = Request(args.url, headers={"User-Agent": "whale browser"})
    with urlopen(req, timeout=5) as r:
        body = r.read(200).decode("utf-8", errors="replace")
        print("status:", r.status)
        print("server:", r.headers.get("server", ""))
        print("body sample:", body.replace("\n", " "))

if __name__ == "__main__":
    main()

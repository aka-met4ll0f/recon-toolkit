#!/usr/bin/env python3
import os
import json
import subprocess
import pandas as pd
from concurrent.futures import ThreadPoolExecutor


def run_ffuf(url, wordlist, output_dir):
    output_file = os.path.join(output_dir, f"{url.replace('/', '_')}.json")
    command = ["ffuf", "-u", f"http://{url}/FUZZ", "-w", wordlist, "-mc", "200", "-o", output_file, "-of", "json"]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        return url, output_file
    except subprocess.CalledProcessError:
        return url, None


def parse_results(output_file):
    if not output_file:
        return []
    try:
        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [r["input"]["FUZZ"] for r in data.get("results", []) if r.get("status") == 200]
    except Exception:
        return []


def main():
    print("[DISCLAIMER] Solo para pentest autorizado.")
    print("Autor: met4ll0f | https://github.com/met4ll0f")
    url_file = input("Ruta del archivo con URLs: ").strip()
    wordlist = input("Ruta del diccionario: ").strip()
    output_dir = "ffuf_results"
    os.makedirs(output_dir, exist_ok=True)

    with open(url_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    rows = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(run_ffuf, url, wordlist, output_dir) for url in urls]
        for future in futures:
            url, output_file = future.result()
            rows.append({"URL": url, "Rutas_200": ";".join(parse_results(output_file))})

    pd.DataFrame(rows).to_excel(os.path.join(output_dir, "summary.xlsx"), index=False)
    print("[OK] Resumen generado")


if __name__ == "__main__":
    main()

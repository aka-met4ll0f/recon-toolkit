#!/usr/bin/env python3
import os
import pandas as pd
import subprocess
import re


BANNER = r"""
__        ___   _    _  _____        ________ ____    ____   ____    _    _   _
\ \      / / | | |  / \|_   _|      / / ____| __ )  / ___| / ___|  / \  | \ | |
 \ \ /\ / /| |_| | / _ \ | |       / /|  _| |  _ \  \___ \| |     / _ \ |  \| |
  \ V  V / |  _  |/ ___ \| |      / / | |___| |_) |  ___) | |___ / ___ \| |\  |
   \_/\_/  |_| |_/_/   \_\_|     /_/  |_____|____/  |____/ \____/_/   \_\_| \_|
"""


def clean_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)


def main():
    print(BANNER)
    print("[DISCLAIMER] Uso autorizado únicamente.")
    print("Autor: met4ll0f | https://github.com/aka-met4ll0f")
    input_file = input("Archivo con URLs sin protocolo: ").strip()
    if not os.path.isfile(input_file):
        print(f"[!] No existe: {input_file}")
        return

    output_dir = "whatweb_results"
    os.makedirs(output_dir, exist_ok=True)
    summary = []

    with open(input_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    for base_url in urls:
        safe = clean_name(base_url.strip("/"))
        txt_path = os.path.join(output_dir, f"{safe}.txt")
        content = []
        for proto in ["http://", "https://"]:
            full = f"{proto}{base_url}"
            try:
                result = subprocess.run(["whatweb", "-v", full], capture_output=True, text=True, timeout=30)
                content.append(result.stdout)
                summary.append({"URL": full, "Output": result.stdout[:500]})
            except Exception as e:
                content.append(f"Error: {e}")

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))

    pd.DataFrame(summary).to_excel("whatweb_summary.xlsx", index=False)
    print("[OK] Reportes generados.")


if __name__ == "__main__":
    main()

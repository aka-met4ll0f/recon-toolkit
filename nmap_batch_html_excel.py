#!/usr/bin/env python3
import sys
import nmap
from pathlib import Path
from openpyxl import Workbook


BANNER = r"""
 _   _ __  __    _    ____    ____  _____ ____   ___  ____ _____
| \ | |  \/  |  / \  |  _ \  |  _ \| ____|  _ \ / _ \|  _ \_   _|
|  \| | |\/| | / _ \ | |_) | | |_) |  _| | |_) | | | | |_) || |
| |\  | |  | |/ ___ \|  __/  |  _ <| |___|  __/| |_| |  _ < | |
|_| \_|_|  |_/_/   \_\_|     |_| \_\_____|_|    \___/|_| \_\|_|
"""


def process_xml(xml_path: Path):
    out_dir = Path(f"{xml_path.stem}_output")
    out_dir.mkdir(exist_ok=True)
    nm = nmap.PortScanner()
    nm.analyse_nmap_xml_scan(xml_path.read_text(encoding="utf-8", errors="ignore"))

    wb = Workbook()
    ws = wb.active
    ws.title = "Vulnerabilidades"
    ws.append(["IP", "Puerto", "Servicio", "Script"])

    html_lines = ["<html><body><h1>Reporte Nmap</h1>"]
    for host in nm.all_hosts():
        html_lines.append(f"<h2>{host}</h2>")
        for proto in nm[host].all_protocols():
            for port in sorted(nm[host][proto].keys()):
                serv = nm[host][proto][port]
                scripts = serv.get("script", {})
                filt = {k: v for k, v in scripts.items() if "vulnerable" in v.lower() or "cve" in v.lower()}
                if not filt:
                    continue
                html_lines.append(f"<p>{proto}/{port} - {serv.get('name','')}</p>")
                ws.append([host, port, serv.get("name", ""), "\n".join(f"{k}: {v}" for k, v in filt.items())])

    html_lines.append("</body></html>")
    (out_dir / "reporte.html").write_text("\n".join(html_lines), encoding="utf-8")
    wb.save(out_dir / "reporte.xlsx")


def main():
    print(BANNER)
    print("[DISCLAIMER] Solo para análisis autorizado.")
    print("Autor: met4ll0f | https://github.com/aka-met4ll0f")
    if len(sys.argv) != 2:
        print("Uso: python nmap_batch_html_excel.py <archivo.xml|directorio>")
        sys.exit(1)
    p = Path(sys.argv[1])
    if p.is_file() and p.suffix == ".xml":
        process_xml(p)
    elif p.is_dir():
        for xml in p.glob("*.xml"):
            process_xml(xml)
    else:
        print("Entrada inválida")


if __name__ == "__main__":
    main()

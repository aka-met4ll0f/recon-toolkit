# recon-toolkit

![CI](https://github.com/aka-met4ll0f/recon-toolkit/actions/workflows/ci.yml/badge.svg)
![Type](https://img.shields.io/badge/Type-Recon-green)

## Description
Toolkit for web recon, DNS checks, and technical enrichment.

## Included scripts
- `dns_info_check.sh`: parallel DNS checks with CSV summary.
- `whatweb_scan.py`: web technology detection with Excel export.
- `ffuf_fuzzer.py`: FFUF path fuzzing with 200-status summary.
- `recon_web.sh`: fast pipeline with `whatweb`, `nuclei`, and `feroxbuster`.
- `subdomains_onprem_cloud.py`: Cloud/On-premise classification with IP enrichment.
- `nmap_scan.sh`: batch Nmap scanning for active domains.
- `nmap_batch_html_excel.py`: converts Nmap XML into HTML/XLSX reports.

## Quick summary
| Script | Input | Output | Typical use |
|---|---|---|---|
| `dns_info_check.sh` | Domain list | Per-domain `.txt` + `dns_summary.csv` | DNS profiling and AXFR review |
| `whatweb_scan.py` | Host/URL list | `.txt` reports + `whatweb_summary.xlsx` | Web technology fingerprinting |
| `ffuf_fuzzer.py` | URLs + wordlist | FFUF JSON + `summary.xlsx` | Endpoint/path discovery |
| `recon_web.sh` | `urls.txt` | `whatweb/nuclei/feroxbuster` outputs | Bulk web recon pipeline |
| `subdomains_onprem_cloud.py` | `dominios.txt` | `resultados_dominios.xlsx` | Cloud vs On-premise classification |
| `nmap_scan.sh` | `urls.txt` | XML/GNMAP/NMAP + status CSV | Batch Nmap scanning |
| `nmap_batch_html_excel.py` | XML file or XML folder | `reporte.html` + `reporte.xlsx` | Executive vulnerability reporting |

## Requirements
- Python 3.10+
- `parallel`, `dig`, `curl`, `whatweb`, `ffuf`, `nmap`
- Python dependencies: `pip install -r requirements.txt`

## Usage
1. Install Python dependencies:
   - `pip install -r requirements.txt`
2. Prepare your input lists (`urls.txt`, `dominios.txt`) based on each script.
3. Run the scripts you need:
   - `bash dns_info_check.sh`
   - `python3 whatweb_scan.py`
   - `python3 ffuf_fuzzer.py`
   - `bash recon_web.sh`
   - `python3 subdomains_onprem_cloud.py`
   - `bash nmap_scan.sh`
   - `python3 nmap_batch_html_excel.py <xml-file|directory>`
4. Review outputs in generated folders and `.xlsx`, `.csv`, `.html` files.

## Author
- Author: **met4ll0f**
- GitHub: `https://github.com/aka-met4ll0f`

## Legal Notice
Use only with explicit owner authorization or in a controlled lab/CTF. The creator is not responsible for misuse.

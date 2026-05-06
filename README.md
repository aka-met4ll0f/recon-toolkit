# recon-toolkit

![CI](https://github.com/aka-met4ll0f/recon-toolkit/actions/workflows/ci.yml/badge.svg)

## Descripción
Toolkit para reconocimiento web, DNS y enriquecimiento técnico.

## Autor
- Autor: **met4ll0f**
- GitHub: `https://github.com/aka-met4ll0f`

## Scripts incluidos
- `dns_info_check.sh`: consultas DNS en paralelo y resumen CSV.
- `whatweb_scan.py`: detección de tecnologías web y exportación a Excel.
- `ffuf_fuzzer.py`: fuzzing de rutas con FFUF y resumen de rutas 200.
- `recon_web.sh`: pipeline rápido con `whatweb`, `nuclei` y `feroxbuster`.
- `subdomains_onprem_cloud.py`: clasificación Cloud/On-premise con enriquecimiento IP.
- `nmap_scan.sh`: escaneo Nmap batch de dominios activos.
- `nmap_batch_html_excel.py`: convierte XML de Nmap a reportes HTML/XLSX.

## Resumen rápido
| Script | Entrada | Salida | Uso típico |
|---|---|---|---|
| `dns_info_check.sh` | Lista de dominios | `.txt` por dominio + `dns_summary.csv` | Perfilado DNS y revisión AXFR |
| `whatweb_scan.py` | Lista de hosts/URLs | Reportes `.txt` + `whatweb_summary.xlsx` | Fingerprinting tecnológico web |
| `ffuf_fuzzer.py` | URLs + wordlist | JSON de FFUF + `summary.xlsx` | Descubrimiento de rutas y endpoints |
| `recon_web.sh` | `urls.txt` | Archivos de `whatweb/nuclei/feroxbuster` | Recon web masivo en pipeline |
| `subdomains_onprem_cloud.py` | `dominios.txt` | `resultados_dominios.xlsx` | Clasificación Cloud vs On-premise |
| `nmap_scan.sh` | `urls.txt` | XML/GNMAP/NMAP + CSV estado | Escaneo Nmap por lotes |
| `nmap_batch_html_excel.py` | XML o carpeta XML | `reporte.html` + `reporte.xlsx` | Presentación ejecutiva de vulnerabilidades |

## Requisitos
- Python 3.10+
- `parallel`, `dig`, `curl`, `whatweb`, `ffuf`, `nmap`
- Dependencias Python: `pip install -r requirements.txt`

## Uso
1. Instala dependencias Python:
   - `pip install -r requirements.txt`
2. Prepara tus listas (`urls.txt`, `dominios.txt`) según el script.
3. Ejecuta los scripts que necesites:
   - `bash dns_info_check.sh`
   - `python3 whatweb_scan.py`
   - `python3 ffuf_fuzzer.py`
   - `bash recon_web.sh`
   - `python3 subdomains_onprem_cloud.py`
   - `bash nmap_scan.sh`
   - `python3 nmap_batch_html_excel.py <archivo.xml|directorio>`
4. Revisa resultados en carpetas de salida y archivos `.xlsx`, `.csv` y `.html`.

## Aviso legal
Usar solo con autorización del dueño del objetivo o en laboratorio/CTF. El creador no se hace responsable por el uso indebido.

# recon-toolkit

![CI](https://github.com/aka-met4ll0f/recon-toolkit/actions/workflows/ci.yml/badge.svg)

Toolkit para reconocimiento web, DNS y enriquecimiento técnico.

- Autor: **met4ll0f**
- GitHub: `https://github.com/aka-met4ll0f`

## Scripts
- `dns_info_check.sh`: consultas DNS en paralelo y resumen CSV.
- `whatweb_scan.py`: deteccion de tecnologias web y exportacion a Excel.
- `ffuf_fuzzer.py`: fuzzing de rutas con FFUF y resumen de rutas 200.
- `recon_web.sh`: pipeline rapido con `whatweb`, `nuclei` y `feroxbuster`.
- `subdomains_onprem_cloud.py`: clasificacion Cloud/On-premise con enriquecimiento IP.
- `nmap_scan.sh`: escaneo Nmap batch de dominios activos.
- `nmap_batch_html_excel.py`: convierte XML de Nmap a reportes HTML/XLSX.

## Requisitos
- Python 3.10+
- `parallel`, `dig`, `curl`, `whatweb`, `ffuf`, `nmap`
- Dependencias Python: `pip install -r requirements.txt`

## Uso paso a paso
1. Instala dependencias Python:
   - `pip install -r requirements.txt`
2. Prepara tus listas (`urls.txt`, `dominios.txt`) segun el script.
3. Ejecuta los scripts que necesites:
   - `bash dns_info_check.sh`
   - `python3 whatweb_scan.py`
   - `python3 ffuf_fuzzer.py`
   - `bash recon_web.sh`
   - `python3 subdomains_onprem_cloud.py`
   - `bash nmap_scan.sh`
   - `python3 nmap_batch_html_excel.py <archivo.xml|directorio>`
4. Revisa resultados en carpetas de salida y archivos `.xlsx/.csv/.html`.

## Disclaimer
Usar solo con autorizacion del duenio del objetivo o en laboratorio/CTF. El creador no se hace responsable por el uso indebido.

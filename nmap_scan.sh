#!/usr/bin/env bash
set -euo pipefail

# DISCLAIMER: uso autorizado únicamente.
# Autor: met4ll0f | https://github.com/met4ll0f

INPUT="urls.txt"
OUTPUT_DIR="nmap_results"
RESULTS_CSV="resultados.csv"
THREADS=5

mkdir -p "$OUTPUT_DIR"
echo "Dominio,IP,Estado" > "$RESULTS_CSV"

scan_domain() {
  local url="$1"
  local domain ip
  domain=$(echo "$url" | sed 's|https\?://||;s|/.*||')
  ip=$(dig +short "$domain" | grep -E '^[0-9.]+$' | head -n 1 || true)
  if [ -z "$ip" ]; then
    echo "$domain,No-IP,Resolución fallida" >> "$RESULTS_CSV"
    return
  fi
  nmap -p 1-1000 -sCV --script vuln -T4 "$ip" -oA "$OUTPUT_DIR/$domain" \
    && echo "$domain,$ip,Escaneo completo" >> "$RESULTS_CSV" \
    || echo "$domain,$ip,Error en escaneo" >> "$RESULTS_CSV"
}

export -f scan_domain
export OUTPUT_DIR RESULTS_CSV
cat "$INPUT" | parallel -j "$THREADS" scan_domain {}

#!/usr/bin/env bash
set -euo pipefail

# DISCLAIMER: uso autorizado únicamente.
# Autor: met4ll0f | https://github.com/met4ll0f

read -r -p "Ingrese el archivo con lista de dominios: " input
output="dns_results"
csv_output="$output/dns_summary.csv"
tmp_dir="$output/.tmp"
mkdir -p "$output" "$tmp_dir"
echo "Dominio,IP,PTR,MX,AXFR" > "$csv_output"

process_domain() {
  local domain="$1"
  local filename outfile line_file ip ptr mx axfr_status nameservers ns result
  filename=$(echo "$domain" | tr -cd '[:alnum:]._-')
  outfile="$output/$filename.txt"
  line_file="$tmp_dir/$filename.csv"

  echo "=== Resultados para: $domain ===" > "$outfile"
  ip=$(dig +short A "$domain" | grep -E '^[0-9.]+$' | head -n1 || true)
  if [[ -z "$ip" ]]; then
    echo "$domain,NO_RESUELVE,,," > "$line_file"
    return
  fi

  ptr=$(dig +short -x "$ip" | sed 's/\.$//' | head -n1)
  mx=$(dig +short MX "$domain" | awk '{print $2}' | sed 's/\.$//' | paste -sd ';' -)
  [[ -z "$mx" ]] && mx="SIN_REGISTROS"
  axfr_status="NO"
  nameservers=$(dig +short NS "$domain" || true)
  for ns in $nameservers; do
    result=$(dig @"$ns" "$domain" AXFR +timeout=3 +tries=1 2>&1 || true)
    if echo "$result" | grep -q "XFR size"; then
      axfr_status="POTENCIAL"
      break
    fi
  done
  echo "$domain,$ip,$ptr,$mx,$axfr_status" > "$line_file"
}

export -f process_domain
export output tmp_dir
grep -Ev '^#|^$' "$input" | parallel -j 4 process_domain {}
cat "$tmp_dir"/*.csv >> "$csv_output" 2>/dev/null || true
echo "[OK] Resumen: $csv_output"

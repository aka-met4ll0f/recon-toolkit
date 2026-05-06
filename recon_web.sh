#!/usr/bin/env bash
set -euo pipefail

# DISCLAIMER: solo para auditoría autorizada.
# Autor: met4ll0f | https://github.com/met4ll0f

input="urls.txt"
output="web_recon"
mkdir -p "$output"

run_scan() {
  local domain="$1"
  local clean_name url
  clean_name=$(echo "$domain" | tr -cd '[:alnum:]._-')
  [[ -z "$domain" || "$domain" =~ ^# ]] && exit 0

  if curl -s --head --connect-timeout 5 "https://$domain" | grep -qi "HTTP/"; then
    url="https://$domain"
  elif curl -s --head --connect-timeout 5 "http://$domain" | grep -qi "HTTP/"; then
    url="http://$domain"
  else
    echo "$domain - No responde" > "$output/${clean_name}-ERROR.txt"
    exit 0
  fi

  whatweb -v "$url" > "$output/${clean_name}-tech.txt" 2>/dev/null || true
  nuclei -u "$url" -o "$output/${clean_name}-nuclei.txt" 2>/dev/null || true
  feroxbuster -u "$url" -w /usr/share/wordlists/dirb/common.txt -o "$output/${clean_name}-dirb.txt" -q 2>/dev/null || true
}

export -f run_scan
export output
grep -Ev '^#|^$' "$input" | parallel -j 4 run_scan {}

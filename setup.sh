#!/bin/bash

# --- [ SPY-E & 123Tool Auto Setup ] ---
# Author: 123Tool
# Project: WiFi-Exposer

# Warna untuk output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}[*] Memulai Instalasi WiFi-Exposer (SPY-RECON)...${NC}"

# 1. Update & Upgrade System
echo -e "${GREEN}[1/3] Memperbarui sistem...${NC}"
pkg update -y && pkg upgrade -y || sudo apt update -y

# 2. Install Python dan Dependency
echo -e "${GREEN}[2/3] Menginstal Python dan Library...${NC}"
pkg install python -y || sudo apt install python3 -y
pip install requests

# 3. Membuat file main.py jika belum ada
if [ ! -f "main.py" ]; then
    echo -e "${GREEN}[3/3] Menyiapkan file utama...${NC}"
    touch main.py
    echo "# Masukkan kode Python Anda di sini" > main.py
    echo -e "${BLUE}[!] File main.py berhasil dibuat. Silakan edit API Token Anda.${NC}"
else
    echo -e "${BLUE}[!] File main.py sudah ada, melewati pembuatan file.${NC}"
fi

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}      INSTALLASI SELESAI (FULL PRO)     ${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "Petunjuk:"
echo -e "1. Edit main.py: ${BLUE}nano main.py${NC}"
echo -e "2. Jalankan: ${BLUE}python main.py${NC}"
echo -e "3. Build EXE (Jika di Windows): ${BLUE}pyinstaller --onefile main.py${NC}"
echo -e "${GREEN}========================================${NC}"

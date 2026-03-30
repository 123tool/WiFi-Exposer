# 📡 WiFi-Exposer
**Automated Wi-Fi Password Extractor with Telegram Integration.**

WiFi-Exposer adalah alat audit keamanan sederhana yang dirancang untuk mengekstrak profil Wi-Fi yang tersimpan di sistem Windows dan mengirimkannya secara instan ke Telegram Bot pribadi Anda dalam format JSON.

## ✨ Fitur Utama
- **Silent Extraction:** Mengambil SSID dan Password (Cleartext).
- **JSON Structured:** Data rapi dan mudah diolah.
- **Telegram Notify:** Notifikasi real-time ke HP Anda.
- **Cross-Management:** Kode bisa dikelola via Termux/Linux, target eksekusi Windows.

## 🛠️ Instalasi & Persiapan

### 1. Persiapan Bot Telegram
1. Chat `@BotFather` di Telegram, buat bot, dan simpan **API Token**.
2. Chat `@userinfobot` untuk mendapatkan **Chat ID** Anda.
3. Masukkan Token dan Chat ID ke dalam `main.py`.

### 2. Install Library (Windows/Termux/Linux)
Pastikan Anda sudah menginstall Python, lalu jalankan:
```bash
pip install requests
chmod +x setup.sh
./setup.sh

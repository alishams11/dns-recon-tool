
# 🔍 DNS Recon Tool

A Python-based tool to enumerate DNS records and brute-force subdomains.

---

## ✨ Features

- Extract NS, MX, TXT, A records
- Brute-force subdomains from wordlist
- Save results to `outputs/results.json`
- Error handling for NXDOMAIN, NoAnswer, Timeout

---

## 📦 Usage

```bash
python3 main.py -d example.com --records
python3 main.py -d example.com --enum --wordlist wordlists/subdomains.txt


#📁 Output Example

Results are saved in outputs/results.json
Sample CLI output:


#⚙️ Requirements

pip install dnspython


# Passive-Recon-Module
The Passive Recon Module is a lightweight Python-based toolkit designed for non-intrusive information gathering during penetration testing and red team engagements. It gathers publicly available information about a target domain without direct interaction, making it stealthy and safe to use.

## 📁 Project Structure

Passive-Recon-Module/
├── scripts/
│ ├── whois_lookup.py # WHOIS record extraction
│ ├── dns_enum.py # A, MX, TXT, NS record enumeration
│ └── subdomain_enum.py # Subdomain enumeration via public APIs
├── requirements.txt # All dependencies listed here
├── README.md # You're reading it!
├── LICENSE # MIT License
└── .gitignore # Python cache and environment exclusions

yaml
Copy
Edit

---

                  🚀 Features

✅ WHOIS Lookup  
✅ DNS Enumeration (A, MX, NS, TXT records)  
✅ Subdomain Enumeration (via crt.sh, AlienVault OTX, etc.)  
✅ Clean, modular scripts (easy to plug into other tools)  
✅ CLI-ready (can be used manually or integrated into larger scripts)

---
                  ⚙️ Setup Instructions

 1. Clone the repository

```bash
git clone https://github.com/mahadzulfiqar/Passive-Recon-Module.git
cd Passive-Recon-Module
2. Install dependencies
Use a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

           🧪 How to Use

WHOIS Lookup
bash
Copy
Edit
python scripts/whois_lookup.py -d example.com
DNS Enumeration
bash
Copy
Edit
python scripts/dns_enum.py -d example.com
Subdomain Enumeration
bash
Copy
Edit
python scripts/subdomain_enum.py -d example.com

              📦 Dependencies

requests

dnspython

python-whois

Install them using:

bash
Copy
Edit
pip install -r requirements.txt

                📜 License

This project is licensed under the MIT License. See LICENSE for more details.

               ✍️ Author
Mahad Zulfiqar
Cybersecurity Intern | GitHub | LinkedIn

              🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

               🛡️ Disclaimer
This tool is intended for educational and authorized penetration testing purposes only. Do not use it on networks you do not own or have permission to test.

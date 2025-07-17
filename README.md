# Passive-Recon-Module
The Passive Recon Module is a lightweight Python-based toolkit designed for non-intrusive information gathering during penetration testing and red team engagements. It gathers publicly available information about a target domain without direct interaction, making it stealthy and safe to use.
## 🔍 Features

✅ WHOIS Lookup  
✅ DNS Enumeration (A, MX, NS, TXT Records)  
✅ Subdomain Enumeration using `crt.sh` and public APIs  

> ⚠️ Passive recon means no interaction with the target system — only querying public sources.

---

## 📁 Project Structure

Passive-Recon-Module/
│
├── whois_lookup.py # WHOIS Information Lookup
├── dns_enum.py # DNS Record Enumeration
├── subdomain_enum.py # Subdomain Finder (using crt.sh)
├── requirements.txt # Required Python libraries
└── README.md # You're reading it!

yaml
Copy code

---

## 🧰 Installation

1. **Clone the repo**:
```bash
git clone https://github.com/mahadzulfiqar/Passive-Recon-Module.git
cd Passive-Recon-Module
Create & activate virtual environment (recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
🚀 Usage
1. WHOIS Lookup
bash
Copy code
python whois_lookup.py
Input a domain (e.g., google.com) to see WHOIS information.

2. DNS Enumeration
bash
Copy code
python dns_enum.py
Retrieves A, MX, TXT, and NS records for the given domain.

3. Subdomain Enumeration
bash
Copy code
python subdomain_enum.py
Finds subdomains using crt.sh’s public certificate data.

📌 Notes
Internet connection is required.

crt.sh may throttle or block repeated queries — use responsibly.

This is passive only — no packet sending to target server.

👨‍💻 Author
Mahad Zulfiqar
🔗 GitHub | 📧 mahadzulfiqar2@gmail.com



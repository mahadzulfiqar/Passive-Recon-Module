# whois_lookup.py

import whois

def perform_whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print("\n[WHOIS Information]")
        print("--------------------")
        for key, value in w.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error during WHOIS lookup: {e}")

# Test the function directly
if __name__ == "__main__":
    domain = input("Enter domain for WHOIS lookup: ")
    perform_whois_lookup(domain)

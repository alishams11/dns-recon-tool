import argparse	
from scanner import record_lookup, subdomain_enum

def main():
    parser = argparse.ArgumentParser(description="DNS Recon Tool by Ali")
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    parser.add_argument("--records", action="store_true", help="Extract DNS records")
    parser.add_argument("--enum", action="store_true", help="Enumerate subdomains")
    parser.add_argument("--wordlist", help="Path to subdomain wordlist")

    args = parser.parse_args()

    if args.records:
        print(f"\n🔎 DNS Records for {args.domain}:\n")
        print("📘 NS Records:")
        print("\n".join(record_lookup.get_ns(args.domain)))

        print("\n📙 MX Records:")
        print("\n".join(record_lookup.get_mx(args.domain)))

        print("\n📕 TXT Records:")
        print("\n".join(record_lookup.get_txt(args.domain)))

        print("\n📗 A Records:")
        print("\n".join(record_lookup.get_a(args.domain)))
   
    if args.enum:
        print(f"\n🌐 Enumerating subdomains for {args.domain}...\n")
        if not args.wordlist:
            print("[!] Please provide a wordlist with --wordlist")
        else:
            subdomain_enum.enum_subdomains(args.domain, args.wordlist)

if __name__ == "__main__":
    main()

import argparse	
from scanner import record_lookup, subdomain_enum
from scanner.utils import save_results

def main():
    parser = argparse.ArgumentParser(description="DNS Recon Tool by Ali")
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    parser.add_argument("--records", action="store_true", help="Extract DNS records")
    parser.add_argument("--enum", action="store_true", help="Enumerate subdomains")
    parser.add_argument("--wordlist", help="Path to subdomain wordlist")

    args = parser.parse_args()

    if args.records:
        print(f"\n🔎 DNS Records for {args.domain}:\n")
       
        ns_records = record_lookup.get_ns(args.domain)
        mx_records = record_lookup.get_mx(args.domain)
        txt_records = record_lookup.get_txt(args.domain)
        a_records = record_lookup.get_a(args.domain)
       
        print("📘 NS Records:")
        print("\n".join(record_lookup.get_ns(args.domain)))

        print("\n📙 MX Records:")
        print("\n".join(record_lookup.get_mx(args.domain)))

        print("\n📕 TXT Records:")
        print("\n".join(record_lookup.get_txt(args.domain)))

        print("\n📗 A Records:")
        print("\n".join(record_lookup.get_a(args.domain)))

        dns_data = {
        "domain": args.domain,
        "type": "records",
        "NS": record_lookup.get_ns(args.domain),
        "MX": record_lookup.get_mx(args.domain),
        "TXT": record_lookup.get_txt(args.domain),
        "A": record_lookup.get_a(args.domain)
    }
    save_results(dns_data)


   
    if args.enum:
        print(f"\n🌐 Enumerating subdomains for {args.domain}...\n")
        if not args.wordlist:
            print("[!] Please provide a wordlist with --wordlist")
        else:
             found = subdomain_enum.enum_subdomains(args.domain, args.wordlist)
             enum_data = {
                "domain": args.domain,
                "type": "subdomain_enum",
                "found": found
            }
             save_results(enum_data)


if __name__ == "__main__":
    main()

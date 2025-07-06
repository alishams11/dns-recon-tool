import argparse
from scanner import record_lookup

def main():
    parser = argparse.ArgumentParser(description="DNS Recon Tool")
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    parser.add_argument("--records", action="store_true", help="Extract DNS records")
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

if __name__ == "__main__":
    main()

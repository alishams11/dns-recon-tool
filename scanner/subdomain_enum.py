import dns.resolver

def enum_subdomains(domain, wordlist_path):
    found = []
    try:
        with open(wordlist_path, 'r') as f:
            subdomains = f.read().splitlines()

        for sub in subdomains:
            full_domain = f"{sub}.{domain}"
            try:
                answers = dns.resolver.resolve(full_domain, 'A')
                ips = [rdata.to_text() for rdata in answers]
                found.append((full_domain, ips))
                print(f"[+] Found: {full_domain} -> {', '.join(ips)}")
            except:
                pass  # Ignore NXDOMAIN or failed lookups

    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
    return found

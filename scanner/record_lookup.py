import dns.resolver
import dns.exception

def get_ns(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS', lifetime=5)
        return [rdata.to_text() for rdata in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return ["[!] NS record not available."]

def get_mx(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX', lifetime=5)
        return [rdata.to_text() for rdata in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return ["[!] MX record not available."]

def get_txt(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT', lifetime=5)
        return [rdata.to_text().strip('"') for rdata in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return ["[!] TXT record not available."]

def get_a(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A', lifetime=5)
        return [rdata.to_text() for rdata in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return ["[!] A record not available."]

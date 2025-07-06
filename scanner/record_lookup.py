import dns.resolver

def get_ns(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        return [rdata.to_text() for rdata in answers]
    except Exception as e:
        return [f"[NS Error] {e}"]

def get_mx(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return [rdata.to_text() for rdata in answers]
    except Exception as e:
        return [f"[MX Error] {e}"]

def get_txt(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        return [rdata.to_text() for rdata in answers]
    except Exception as e:
        return [f"[TXT Error] {e}"]

def get_a(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [rdata.to_text() for rdata in answers]
    except Exception as e:
        return [f"[A Error] {e}"]

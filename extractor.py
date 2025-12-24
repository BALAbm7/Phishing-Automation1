import re

def extract_indicators(email_text):
    urls = re.findall(r'(http[s]?://[^\s]+)', email_text)
    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', email_text)

    domains = []
    for url in urls:
        domains.append(url.split("//")[-1].split("/")[0])

    return {
        "urls": list(set(urls)),
        "ips": list(set(ips)),
        "domains": list(set(domains))
    }

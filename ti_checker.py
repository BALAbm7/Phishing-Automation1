def check_threat_intel(indicators):
    return {
        "malicious_urls": indicators["urls"],
        "malicious_ips": indicators["ips"]
    }

def analyze_headers(email_text):
    return {
        "spf": "fail" if "spf=fail" in email_text else "pass",
        "dkim": "fail" if "dkim=fail" in email_text else "pass",
        "dmarc": "fail" if "dmarc=fail" in email_text else "pass"
    }

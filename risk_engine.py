def calculate_risk(ti, headers):
    score = len(ti["malicious_urls"]) * 30
    score += len(ti["malicious_ips"]) * 40

    for v in headers.values():
        if v == "fail":
            score += 20

    verdict = "MALICIOUS" if score >= 70 else "SUSPICIOUS" if score >= 40 else "BENIGN"
    return score, verdict

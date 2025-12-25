import json

def generate_report(indicators, ti, headers, score, verdict, case):
    report = {
        "case": case,
        "verdict": verdict,
        "risk_score": score,
        "indicators": indicators,
        "threat_intel": ti,
        "headers": headers
    }

    print("\n=== SOC REPORT ===")
    print("Case ID:", case["case_id"])
    print("Verdict:", verdict)
    print("Risk Score:", score)

    with open(case["case_id"] + ".json", "w") as f:
        json.dump(report, f, indent=4)

    print("Output saved as", case["case_id"] + ".json")

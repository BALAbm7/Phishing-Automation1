from msg_reader import read_msg_file
from extractor import extract_indicators
from ti_checker import check_threat_intel
from header_analysis import analyze_headers
from risk_engine import calculate_risk
from case_manager import create_case
from report_generator import generate_report

EMAIL_FILE = "example.msg"

def main():
    email_text = read_msg_file(EMAIL_FILE)

    indicators = extract_indicators(email_text)
    ti = check_threat_intel(indicators)
    headers = analyze_headers(email_text)
    score, verdict = calculate_risk(ti, headers)
    case = create_case(verdict)

    generate_report(indicators, ti, headers, score, verdict, case)

if __name__ == "__main__":
    main()

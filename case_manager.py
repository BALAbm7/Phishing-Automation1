import uuid
from datetime import datetime

def create_case(verdict):
    return {
        "case_id": f"CASE-{uuid.uuid4().hex[:8].upper()}",
        "created": datetime.utcnow().isoformat() + "Z",
        "status": "OPEN" if verdict != "BENIGN" else "CLOSED"
    }

import extract_msg

def read_msg_file(file_path):
    msg = extract_msg.Message(file_path)
    msg.process()

    email_text = f"""
From: {msg.sender}
To: {msg.to}
Subject: {msg.subject}

{msg.body}
"""
    return email_text

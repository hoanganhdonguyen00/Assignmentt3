import re

def redact_phone_numbers(text):
    pattern = r'(\+84\d+|\b\d{10}\b)'
    return re.sub(pattern, '[REDACTED]', text)
text = "Call me at 0987654321 or +84912345678 tomorrow."
print(redact_phone_numbers(text))
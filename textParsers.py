import re

# Extract emails from a string
def extract_emails(input_string):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails_found = re.findall(email_pattern, input_string)

    return emails_found

# Extract phone numbers from a string
def extract_phone_numbers(input_string):
    phone_pattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    phone_numbers_found = re.findall(phone_pattern, input_string)
    
    return phone_numbers_found

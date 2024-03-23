from bs4 import BeautifulSoup
import urllib.request
import re

def extract_emails(input_string):
    # Regex pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matches using the findall method from the re module
    emails_found = re.findall(email_pattern, input_string)

    return emails_found

def extract_phone_numbers(input_string):
    phone_pattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    phone_numbers_found = re.findall(phone_pattern, input_string)
    
    return phone_numbers_found


url = ""
text = urllib.request.urlopen(url).read()


soup = BeautifulSoup(text, 'html.parser')
emails = extract_emails(soup.get_text())
phone_numbers = extract_phone_numbers(soup.get_text())
print(soup.title.string)
print(emails)
print(phone_numbers)



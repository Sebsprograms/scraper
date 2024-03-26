from bs4 import BeautifulSoup
import urllib.request
from textParsers import extract_emails, extract_phone_numbers
from elementParsers import extract_website_routes

# Remove trailing slash from the URL for now
testUrl = ""

def extract_data_from_url(url):
    text = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(text, 'html.parser')
    title = soup.title.strings
    emails = extract_emails(soup.get_text())
    phone_numbers = extract_phone_numbers(soup.get_text())
    all_link_elements = soup.find_all("a", href=True)
    all_links = extract_website_routes(all_link_elements)
    for link in all_links:
        try:
            new_text = urllib.request.urlopen(url + link).read()
            new_soup = BeautifulSoup(new_text, 'html.parser')
            emails += extract_emails(new_soup.get_text())
            phone_numbers += extract_phone_numbers(new_soup.get_text())
        except:
            pass
    emails = list(set(emails))
    phone_numbers = list(set(phone_numbers))
    return {"title": title, "emails": emails, "phone_numbers": phone_numbers}


data = extract_data_from_url(testUrl)

print(data)
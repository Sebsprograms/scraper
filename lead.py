from bs4 import BeautifulSoup
import urllib.request
import re
class Lead:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description
        self.soup = None
        self.emails = []
        self.phone_numbers = []
        self.internal_links = []


    # URL operations
    def parse_url(self):
        try:
            text = urllib.request.urlopen(self.url).read()
            self.soup = BeautifulSoup(text, 'html.parser')
            self.get_data_from_soup()
        except:
            print('Something went wrong fetching the root url.')
        
    def get_data_from_soup(self):
        self.set_title(self.soup.title.string)
        soup_text = self.soup.get_text()
        self.get_emails_and_phone_numbers_from_string(soup_text)
        self.get_link_elements()
        for link in self.internal_links:
            try:
                response = urllib.request.urlopen(self.url + link).read()
                soup = BeautifulSoup(response, 'html.parser')
                soup_text = soup.get_text()
                self.get_emails_and_phone_numbers_from_string(soup_text)
            except:
                pass
        self.remove_duplicate_emails()
        self.remove_duplicate_phone_numbers()

    # Data setters 
    def get_emails_and_phone_numbers_from_string(self, text):
        self.extract_emails(text)
        self.extract_phone_numbers(text)

    # Title
    def set_title(self, title):
        self.title = title
    
    # Emails
    def add_emails(self, emails):
        self.emails += emails

    def remove_duplicate_emails(self):
        self.emails = list(set(self.emails))
    
    # Phone numbers
    def add_phone_numbers(self, phone_numbers):
        self.phone_numbers += phone_numbers
    
    def remove_duplicate_phone_numbers(self):
        self.phone_numbers = list(set(self.phone_numbers))

    # Links
    def add_internal_links(self, links):
        self.internal_links += links

    def get_link_elements(self):
        self.extract_internal_links(self.soup.find_all("a", href=True));


    # Data sanitizers
    # Extract emails from a string
    def extract_emails(self, input_string):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails_found = re.findall(email_pattern, input_string)
        self.add_emails(emails_found)

    # Extract phone numbers from a string
    def extract_phone_numbers(self, input_string):
        phone_pattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
        phone_numbers_found = re.findall(phone_pattern, input_string)
        self.add_phone_numbers(phone_numbers_found)
    
    # Takes a list of link elements and returns paths that are internal to the website
    def extract_internal_links(self, links):
        cleaned_links = list(filter(lambda x: not x['href'].startswith('http'), links))
        cleaned_links = list(filter(lambda x: x['href'].startswith('/'), cleaned_links))
        final_links = []
        for link in cleaned_links:
            final_links.append(link['href'])
        final_links = list(set(final_links))
        self.add_internal_links(final_links)

    # Data getters
    def get_data(self):
        return {
            'url': self.url,
            'title': self.title,
            'description': self.description,
            'emails': self.emails,
            'phone_numbers': self.phone_numbers,
        }
    
    def __str__(self):
        return str(self.get_data())
    
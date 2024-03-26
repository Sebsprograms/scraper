class Lead:
    def __init__(self):
        self.title
        self.emails = []
        self.phone_numbers = []
    
    def add_emails(self, emails):
        self.emails += emails
    
    def add_phone_numbers(self, phone_numbers):
        self.phone_numbers += phone_numbers

    def set_title(self, title):
        self.title = title

    def get_data(self):
        return {"title": self.title, "emails": self.emails, "phone_numbers": self.phone_numbers}
    
    def __str__(self):
        return str(self.get_data())
    
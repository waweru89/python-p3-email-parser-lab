import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split the string by commas and spaces
        raw_emails = re.split(r"[,\s]+", self.email_addresses.strip())
        # Filter out any empty strings and return unique, sorted emails
        return sorted(set(email for email in raw_emails if email))

# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', self.email_string)
        parsed_emails = sorted(list(set(email_list)))

        return parsed_emails






# import re

# class EmailAddressParser:
#     def __init__(self, email_string):
#         self.email_string = email_string

#     def parse(self):
#         email_list = self.email_string.split(',')
#         parsed_emails = []

#         for email in email_list:
#             parsed_emails += [addr.strip() for addr in email.split() if addr.strip()]

#         unique_emails = list(set(parsed_emails))
#         sorted_emails = sorted(unique_emails)
#         return sorted_emails
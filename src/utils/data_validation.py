import re

class DataValidation:
    @staticmethod
    def is_email_valid(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def is_phone_number_valid(phone):
        pattern = r'^\+?[1-9]\d{1,14}$'
        return re.match(pattern, phone) is not None

    @staticmethod
    def is_non_empty_string(value):
        return isinstance(value, str) and bool(value.strip())

    @staticmethod
    def is_positive_integer(value):
        return isinstance(value, int) and value > 0

# Usage
# is_valid_email = DataValidation.is_email_valid("test@example.com")

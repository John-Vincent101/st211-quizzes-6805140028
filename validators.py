import re

def validate_email(email):
    """
    Validate an email address using a regular expression.
    Returns True if the email is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError(f"Invalid email address: {email}")
    return True

def validate_age(age):

    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError("Age must be 0-150")
    return True
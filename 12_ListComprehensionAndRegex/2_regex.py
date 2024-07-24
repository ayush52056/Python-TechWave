import re

# Check if the string contains 'hello'
pattern = r'hello'
text = 'hello world'
match = re.search(pattern, text)
if match:
    print("Match found!")  # Output: Match found!
else:
    print("No match found.")



# Validate an email address
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = 'test@example.com'
if re.match(pattern, email):
    print("Valid email address!")  # Output: Valid email address!
else:
    print("Invalid email address.")


# Replace all whitespace with a single space
pattern = r'\s+'
text = 'This    is  a   test.'
new_text = re.sub(pattern, ' ', text)
print(new_text)  # Output: This is a test.



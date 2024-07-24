import csv
import re

# Define the regex pattern to match Indian phone numbers
phone_pattern = r'\+91 \d{10}'

# Function to check if a phone number is valid
def is_valid_phone_number(phone_number):
    if re.fullmatch(phone_pattern, str(phone_number)):
        return "Valid"
    else:
        return "Invalid"

# Load the CSV file (replace 'your_file.csv' with your actual file path)
input_file = '12_ListComprehensionAndRegex/test.csv'
output_file = '12_ListComprehensionAndRegex/output_with_validation_results.csv'

# Open the CSV file for reading
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Open the CSV file for writing results
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Write header for the output file
        writer.writerow(['PhoneNumber', 'ValidationResult'])

        # Read each row and process
        for row in reader:
            if row:
                phone_number = row[0]
                validation_result = is_valid_phone_number(phone_number)
                # Write the phone number and its validation result to the output file
                writer.writerow([phone_number, validation_result])
                # Print the result to the terminal
                print(f"Phone Number: {phone_number} - Validation Result: {validation_result}")

print(f"Results saved to {output_file}")

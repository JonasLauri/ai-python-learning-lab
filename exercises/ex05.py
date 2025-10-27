# Exercise 5 — Email Validator & Counter (strings + loops + conditionals)
emails = [
    "jonas@",
    "milda@example.com",
    "tomas@gmail",
    "austeja@gmail.com",
    "lukas@domain.lt",
]

# Filter out valid emails in refactored way
valid_emails = [email for email in emails if "@" in email and "." in email]
# Filter out non-valid emails in classic way
no_valid_emails = []
for email in emails:
    if "@" not in email or "." not in email:
        no_valid_emails.append(email)
# Print both lists and totals clearly
print(
    f"Valid list of emails - {valid_emails} has {len(valid_emails)} items\n"
    f"Non-valid list of emails - {no_valid_emails} has {len(no_valid_emails)} items"
)

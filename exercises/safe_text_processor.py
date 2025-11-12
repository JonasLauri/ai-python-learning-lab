# Create a script that:
# Takes a user’s sentence as input.
# Removes punctuation and returns a list of words in lowercase.
# Validates that input isn’t empty or numeric.
# Raises an error if invalid.
# Wrap logic inside a function with a clean return.
# Hint: combine string methods, conditional checks, try/except, and loops.
import re


def get_user_input(prompt: str, input_type=str) -> any:
    """
    Take validated user input - not empty/numeric
    Do string cleaning, lowercase and return words in list.
    """
    user_input = input(prompt)

    if user_input:
        try:
            user_text = input_type(user_input)
            clean_text = re.sub(r"[^\w\s]", "", user_text)
            return clean_text.split()
        except TypeError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}")
        finally:
            print("Your text got processed successfully!")
    else:
        raise ValueError("Empty input")


user_words = get_user_input("Enter your text: ")
print(user_words)

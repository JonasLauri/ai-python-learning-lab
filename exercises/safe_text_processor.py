# Create a script that:
# Takes a user’s sentence as input.
# Removes punctuation and returns a list of words in lowercase.
# Validates that input isn’t empty or numeric.
# Raises an error if invalid.
# Wrap logic inside a function with a clean return.
# Hint: combine string methods, conditional checks, try/except, and loops.
import re


def is_numeric_only(s: str) -> bool:
    """Check whether the string is purely numeric."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_user_words(prompt: str = "Enter your text: ") -> list[str]:
    """
    Take validated user input - not empty/numeric
    Do string cleaning, lowercase and return words in list.
    """
    user_input = input(prompt).strip()

    if not user_input:
        raise ValueError("Empty input!")

    if is_numeric_only(user_input):
        raise ValueError("Input must not be numeric")

    clean_text = re.sub(r"[^\w\s]", "", user_input)
    words = clean_text.lower().split()

    return words


def main():
    try:
        user_words = get_user_words()
        print(user_words)
    except ValueError as e:
        print("Validation error:", e)


if __name__ == "__main__":
    main()

# Write a function add_expense(category, amount) that:

# Validates that amount is a positive number.

# Stores results into a dictionary structure ({category: total}) each time it’s called.

# Uses a closure or global dict — your choice — so that totals accumulate.

# Returns a summary string like: "Total for Food: 124.50".
dict_expenses = {}


def is_numeric_only(s: str) -> bool:
    """Check whether the string is purely numeric."""

    try:
        float(s)
        return True
    except ValueError:
        return False


def is_positive_amount(amount: float) -> bool:
    """Validates that amount is a positive number"""

    if amount >= 0:
        return True
    else:
        return False


def get_user_input() -> tuple[str, float]:
    """
    Take validated user inputs - not empty/positive amount
    """

    category = input("Enter category: ").strip()
    amount_str = input("Enter amount: ").strip()

    if not category or not amount_str:
        raise ValueError("Please privide nesseccary input!")

    if is_numeric_only(category):
        raise ValueError("Category must not be numeric")

    if not is_numeric_only(amount_str):
        raise ValueError("Amount must be numeric")

    amount = float(amount_str)

    if not is_positive_amount(amount):
        raise ValueError("The amount must be positive")

    return category, amount


def add_expense(category: str, amount: float):
    """
    Add-ups expenses based by category
    Store results into dict
    """

    dict_expenses[category] = dict_expenses.get(category, 0) + amount

    return dict_expenses

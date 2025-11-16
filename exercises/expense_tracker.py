# Write a function add_expense(category, amount) that:
# Validates that amount is a positive number.
# Stores results into a dictionary structure ({category: total}) each time it’s called.
# Uses a closure or global dict — your choice — so that totals accumulate.
# Returns a summary string like: "Total for Food: 124.50".
# Updated: Improved my way as a whole program to track expenses
dict_expenses: dict[str, float] = {}


def is_numeric_only(s: str) -> bool:
    """Check whether the string is purely numeric."""

    try:
        float(s)
        return True
    except ValueError:
        return False


def is_positive_amount(amount: float) -> bool:
    """Validates that amount is a positive number"""

    if amount > 0:
        return True
    else:
        return False


def get_menu_choice() -> int:
    """Get user option command"""

    while True:
        input_option = input(
            "Choose option:\n"
            "- Add expenses - enter 1\n"
            "- Show expenses - enter 2\n"
            "- End the program - enter 3\n"
        )

        option = input_option.strip()

        if option in ["1", "2", "3"]:
            return int(option)

        print("Please enter 1, 2 or 3 option")


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


def add_expense(category: str, amount: float) -> str:
    """
    Add-ups expenses based by category
    Stores results into global dict
    Prints results
    """

    dict_expenses[category] = dict_expenses.get(category, 0) + amount
    return f"Total for {category}: {dict_expenses[category]:.2f}"


def print_expenses():
    """Print out all expenses"""

    if not dict_expenses:
        print("No expenses recorded yet.")
        return None

    print("Current expenses based by category are:\n")
    for category, amount in dict_expenses.items():
        print(f"{category}: {amount:.2f}")


def run_expenses_tracker():
    """Program controls"""

    while True:
        option = get_menu_choice()

        match option:
            case 1:
                try:
                    category, amount = get_user_input()
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                added_summary = add_expense(category, amount)
                print(added_summary)

            case 2:
                print_expenses()

            case 3:
                print("Program ended!")
                break


if __name__ == "__main__":
    run_expenses_tracker()

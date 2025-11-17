# Write a function add_expense(category, amount) that:
# Validates that amount is a positive number.
# Stores results into a dictionary structure ({category: total}) each time it’s called.
# Uses a closure or global dict — your choice — so that totals accumulate.
# Returns a summary string like: "Total for Food: 124.50".
# Updated: Improved my way as a whole program to track expenses


def is_numeric_only(s: str) -> bool:
    """Check whether a string is purely numeric."""

    try:
        float(s)
        return True
    except ValueError:
        return False


def is_positive_amount(amount: float) -> bool:
    """Validates amount is a positive number."""

    if amount > 0:
        return True
    else:
        return False


def get_menu_choice() -> int:
    """Handle correct user choice for program routes"""

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


def handle_add_expense(expenses: dict[str, float]) -> None:
    """Handle user interaction for adding a new expense."""

    # Ask for category & amount
    category = input("Enter category: ").lower().strip()
    raw_amount = input("Enter amount: ").lower().strip()

    # Validate input results: not empty, category not numeric, amount numeric & positive
    if not category or not raw_amount:
        print("Please provide nesseccary input!")
        return
    if is_numeric_only(category):
        print("Category must not be numeric")
        return
    if not is_numeric_only(raw_amount):
        print("Amount must be numeric")
        return
    # Cast amount to float
    amount = float(raw_amount)
    if not is_positive_amount(amount):
        print("The amount must be positive")
        return

    # Call core/logic function
    add_expense(expenses, category, amount)

    # Show handled result
    print(f"Added {amount:.2f} to {category}. Total now: {expenses[category]:.2f}")


def add_expense(expenses: dict[str, float], category: str, amount: float) -> None:
    """Add or update an expense amount in the expenses dictionary."""

    expenses[category] = expenses.get(category, 0.0) + amount


def handle_show_summary(expenses: dict[str, float]) -> None:
    """Display the current list of expenses to the user."""

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("Current expenses by category:")
    for category, amount in expenses.items():
        print(f"{category}: {amount:.2f}")


def main():
    """The program entry point with loop controller"""

    expenses: dict[str, float] = {}

    while True:
        option = get_menu_choice()

        match option:
            case 1:
                handle_add_expense(expenses)
            case 2:
                handle_show_summary(expenses)
            case 3:
                print("Program ended!")
                break


if __name__ == "__main__":
    main()

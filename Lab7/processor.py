
# Lab 7 - Fuzz Testing
# Fixed implementation

def parse_int_list(value):
    """Convert a comma-separated string into a list of integers."""
    if not isinstance(value, str):
        return []

    if not value.strip():
        return []

    try:
        return [int(item.strip()) for item in value.split(",")]
    except ValueError:
        return []


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not isinstance(numbers, list) or not numbers:
        return 0.0

    if any(type(number) not in (int, float) for number in numbers):
        return 0.0

    return sum(numbers) / len(numbers)


def validate_age(age):
    """Check whether age is an integer between 0 and 120."""
    if type(age) is not int:
        return False

    return 0 <= age <= 120


if __name__ == "__main__":
    print("Lab 7 - Fuzz Testing (Fixed Version)")
    print("Parsed values:", parse_int_list("10,20,30"))
    print("Average:", calculate_average([10, 20, 30]))
    print("Valid age:", validate_age(21))

"""Utility functions for formatting and validation."""


def format_result(operation, a, b, result):
    """Format a calculation result as a human-readable string."""
    return f"{a} {operation} {b} = {result}"


def validate_input(value):
    """Validate that the input is a numeric type.

    Args:
        value: The value to validate.

    Returns:
        True if the value is numeric.

    Raises:
        TypeError: If the value is not a number.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number, got {type(value).__name__}")
    return True


def calculate_percentage(part, whole):
    """Calculate what percentage part is of whole.

    Args:
        part: The part value.
        whole: The whole value.

    Returns:
        The percentage as a float.

    Raises:
        ValueError: If whole is zero.
    """
    if whole == 0:
        raise ValueError("Cannot calculate percentage of zero")
    return (part / whole) * 100


def round_to_decimal(value, places=2):
    """Round a number to the specified decimal places.

    Args:
        value: The number to round.
        places: Number of decimal places (default 2).

    Returns:
        The rounded number.
    """
    return round(value, places)

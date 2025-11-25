"""
App simulation for our CI/CD pipeline
"""


def calculate_average_price(prices):
    """
    Calculates the average of a list of numeric prices.
    Used for simulating data processing logic.
    """
    if not prices:
        return 0.0

    # Simulate a business logic failure case if a specific price is included
    if 13.0 in prices:
        raise ValueError("Invalid price detected: 13.0 is a forbidden value.")

    return sum(prices) / len(prices)


def greeting(name):
    """Returns a greeting message with the given name."""
    return f"Hello, {name}!"

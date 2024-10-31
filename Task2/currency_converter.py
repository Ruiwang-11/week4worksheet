def currency_converter(amount, from_currency, to_currency):
    """
    Converts an amount from one currency to another based on predefined conversion rates.

    Parameters:
    amount (float): The amount of money to convert. It must be non-negative.
    from_currency (str): The currency code of the original currency.
    to_currency (str): The currency code to which the amount should be converted.

    Returns:
    float: The converted amount, rounded to two decimal places, or 0.0 if the input amount is negative.
    """
    
    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
}

    
    if amount < 0:
        return 0.0

    
    if from_currency in conversion_rate and to_currency in conversion_rate[from_currency]:
        rate = conversion_rate[from_currency][to_currency]
        converted_amount = round(amount * rate, 2)
        return converted_amount
    else:
        return 0.0
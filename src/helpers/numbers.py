def shorten_number(value):
    """
    Converts large numbers into a shortened format.
    Example: 1500000 -> 1.5M, 1500000000 -> 1.5B
    """
    try:
        value = int(value)
        if value >= 1_000_000_000_000:
            formatted_value = value / 1_000_000_000_000
            suffix = 'T'
        elif value >= 1_000_000_000:
            formatted_value = value / 1_000_000_000
            suffix = 'B'
        elif value >= 1_000_000:
            formatted_value = value / 1_000_000
            suffix = 'M'
        elif value >= 1_000:
            formatted_value = value / 1_000
            suffix = 'K'
        else:
            return str(value)

        # Round the formatted value
        formatted_value = round(formatted_value, 1)

        # Check if the formatted value is a whole number
        if formatted_value.is_integer():
            return '{:.0f}{}'.format(formatted_value, suffix)
        else:
            return '{:.1f}{}'.format(formatted_value, suffix)

    except (ValueError, TypeError):
        return str(value)

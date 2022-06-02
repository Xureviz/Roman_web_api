from api.helpers.roman_number_utils import word


def biggest_number(roman_numbers):
    """
    Returns the biggest number from a list of roman numbers
    """
    roman_number_values = word(roman_numbers)
    decresent_list = sorted(roman_number_values, key=lambda d: d['value'], reverse=True)
    return decresent_list[0]

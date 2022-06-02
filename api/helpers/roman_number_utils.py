def word(roman_numbers):
    """
    Validates the word entered by the user.
    """
    is_word_valid(roman_numbers)
    return calculate_roman_number(roman_numbers)


def is_word_valid(roman_numbers):
    """
    is_word_valid function checks if the word is valid
    """
    if roman_numbers.isalpha():
        return True
    return False


def calculate_roman_number(roman_numbers):
    """
    calculate the roman number
    """

    roman_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    roman_number_values = []
    for i in range(len(roman_numbers)):
        try:
            value = roman_dict[roman_numbers[i]]
            if i + 1 < len(roman_numbers) and roman_numbers[i + 1] in roman_dict.keys():
                if roman_numbers[i: i + 2] in roman_dict:
                    value = roman_dict[roman_numbers[i: i + 2]]
                    roman_number_values.append(
                        {"number": roman_numbers[i: i + 2], "value": value}
                    )
                    i += 2
                    continue
                value += roman_dict[roman_numbers[i + 1]]
                roman_number_values.append(
                    {"number": roman_numbers[i: i + 2], "value": value}
                )
                i += 1
                continue
            if i == len(roman_numbers) - 1:
                roman_number_values.append({"number": roman_numbers[i], "value": value})
        except KeyError:
            continue

    return roman_number_values

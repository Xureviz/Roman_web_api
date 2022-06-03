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
    i = 0
    total = 0
    while i < len(roman_numbers):
        try:
            value = roman_dict[roman_numbers[i]]
            if (
                i + 1 < len(roman_numbers) and roman_numbers[i + 1] in roman_dict.keys()
            ):  # verifica se o proximo numero é romando
                if (
                    roman_numbers[i : i + 2] in roman_dict
                ):  # verifica se os dois juntos constam na tabela
                    value = roman_dict[roman_numbers[i : i + 2]]
                    total += value
                    roman_number_values.append(
                        {"number": roman_numbers[i : i + 2], "value": total}
                    )  # adiciona na lista
                    i += 2
                    continue
                total += value
                i += 1
                continue
            total += value
            roman_number_values.append({"number": roman_numbers[i], "value": total})
            i += 1
            continue
        except (KeyError, IndexError):
            total = 0
            i += 1

    return roman_number_values

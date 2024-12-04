CARD_HOLDER_RULES = {
    "max_length": 36,
    "min_length": 5,
    "pattern": "(^[A-Za-z]{1,}[A-Za-z\s\-'\.]*[A-Za-z]{1,}$)",
    "pattern_error_message": "Card Holder Name can only contain letters, spaces, hyphens, apostrophes, and periods, and must start and end with a letter",
    "null": False,
    "blank": False,
}


CARD_NUMBER_RULES = {
    "max_length": 16,
    "min_length": 16,
    "pattern": "^[0-9]+$",
    "pattern_error_message": "The Card Number can only contain digits",
    "null": False,
    "blank": False,
}


CVV_CODE_RULES = {
    "max_length": 3,
    "min_length": 3,
    "pattern": "^[0-9]+$",
    "pattern_error_message": "The CVV Code can only contain digits",
    "null": False,
    "blank": False,
}

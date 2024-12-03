FIRST_NAME_RULES = {
    "max_length": 255,
    "min_length": 2,
    "pattern": "(^[A-Za-z]{2,}$)|(^[A-Za-z]{1,}[\s\-]?[A-Za-z]{1,}$)",
    "pattern_error_message": "First Name can only contain letters, spaces, hyphens, and must start and end with a letter",
    "null": False,
    "blank": False,
}

LAST_NAME_RULES = {
    "max_length": 255,
    "min_length": 2,
    "pattern": "(^[A-Za-z]{2,}$)|(^[A-Za-z]{1,}[\s\-]?[A-Za-z]{1,}$)",
    "pattern_error_message": "Last Name can only contain letters, spaces, hyphens, and must start and end with a letter",
    "null": False,
    "blank": False,
}

PHONE_NUMBER_RULES = {
    "max_length": 15,
    "min_length": 7,
    "pattern": "^[0-9]+$",
    "pattern_error_message": "This field can only contain digits",
    "null": False,
    "blank": False,
}

STREET_ADDRESS_RULES = {
    "max_length": 255,
    "min_length": 8,
    "pattern": "^([A-Za-z0-9]{1,})([A-Za-z0-9\s\-\.']{6,})([A-Za-z0-9])$",
    "pattern_error_message": "This field can only contain letters, spaces, hyphens, apostrophes, and periods, and must start and end with a letter or digit",
    "null": False,
    "blank": False,
}

APARTMENT_RULES = {
    "max_length": 10,
    "min_length": 1,
    "pattern": "^([A-Za-z0-9]{1,5})([A-Za-z0-9\s\-\.]{0,4})([A-Za-z0-9]?)$",
    "pattern_error_message": "This field can only contain letters, spaces, hyphens, and periods, and must start and end with a letter or digit",
    "null": True,
    "blank": True,
}

POSTAL_CODE_RULES = {
    "max_length": 15,
    "min_length": 3,
    "pattern": "^([A-Za-z0-9]{1,})([A-Za-z0-9\s\-\.\,]{0,12})([A-Za-z0-9]{1})$",
    "pattern_error_message": "This field can only contain letters, spaces, hyphens, commas, and periods, and must start and end with a letter or digit",
    "null": False,
    "blank": False,
}

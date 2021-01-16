import re

ISBN_TEN = "X"
ISBN_PATTERN = "\d{1}-?\d{3}-?\d{5}-?[\d%s]" % ISBN_TEN
pattern = re.compile(ISBN_PATTERN)


def is_valid(isbn: str) -> bool:
    if not pattern.fullmatch(isbn):
        return False

    checksum = 0
    for (char, times) in zip(isbn.replace("-", ""), reversed(range(11))):
        val = 10 if char == ISBN_TEN else int(char)
        checksum += val * times

    if checksum % 11 == 0:
        return True

    return False

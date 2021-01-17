import re
from string import ascii_lowercase


def is_pangram(sentence: str) -> bool:

    return (
        True
        if set(re.findall("[a-zA-Z]", sentence.lower())) == set(ascii_lowercase)
        else False
    )

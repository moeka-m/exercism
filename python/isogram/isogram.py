import re


def is_isogram(string: str) -> bool:
    allow_pattern = "[- ]"
    target = re.sub(allow_pattern, "", string).lower()

    if len(target) == len(set(target)):
        return True
    return False

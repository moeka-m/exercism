def is_isogram(string: str) -> bool:
    target = [c.lower() for c in string if c.isalpha()]

    if len(target) == len(set(target)):
        return True
    return False

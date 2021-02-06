def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("accept only sequences of equal length.")

    return sum(1 for a, b in zip(strand_a, strand_b) if a != b)

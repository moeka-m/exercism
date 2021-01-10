from typing import List


def slices(series: str, length: int) -> List[str]:
    if length <= 0:
        raise ValueError("'length' required greater than 0")
    if len(series) < length:
        raise ValueError("'length' required 'len(series)' or less")

    return [series[i : i + length] for i in range(len(series) - length + 1)]

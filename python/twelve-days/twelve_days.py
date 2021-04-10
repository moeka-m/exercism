ORDINAL_DICT = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}
START_SINGING = "On the {} day of Christmas my true love gave to me:"
PHRASE_LIST = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]


def recite(start_verse: int, end_verse: int) -> list[str]:
    if not (1 <= start_verse <= end_verse <= 12):
        raise ValueError("required: 1 <= start_verse <= end_verse <= 12")

    ret: list[str] = []
    for i in range(start_verse, end_verse + 1):
        ret.append(_recite_single(i))

    return ret


def _recite_single(verse: int) -> str:
    recite_str: list[str] = []
    recite_str.append(START_SINGING.format(ORDINAL_DICT.get(verse)))
    recite_str.append(_phrases_join(PHRASE_LIST[verse - 1 :: -1]))
    return " ".join(recite_str)


def _phrases_join(phrases: list[str]) -> str:
    assert 0 < len(phrases) <= 12
    if len(phrases) > 1:
        phrases[-1] = "and " + phrases[-1]
    return ", ".join(phrase for phrase in phrases) + "."

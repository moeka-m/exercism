def convert(number: int):
    ret = ""
    if number % 3 == 0:
        ret = "Pling"
    if number % 5 == 0:
        ret = ret + "Plang"
    if number % 7 == 0:
        ret = ret + "Plong"

    if ret == "":
        return str(number)
    return ret

from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = _toMatrix(matrix_string)

    def row(self, index: int) -> List[int]:
        return list(self.matrix[index - 1])  # list()で包まないとself.matrixの参照がそのまま返ってしまう

    def column(self, index: int) -> List[int]:
        return [x[index - 1] for x in self.matrix]

    def print(self):
        print("-----")
        for row in self.matrix:
            print(row)
        print("-----")


def _toMatrix(matrix_string: str) -> List[List[int]]:
    matrix_string_sprit = [x.split() for x in matrix_string.splitlines()]
    return [[int(strval) for strval in row] for row in matrix_string_sprit]

# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"
MASKED_CHAR_DISPLAY = "_"


class Hangman:
    def __init__(self, word: str):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guesses: list[str] = []

    def guess(self, char: str):
        if not self.status == STATUS_ONGOING:
            raise ValueError("The game already finished.")

        if char in set(self.guesses) or char not in self.word:
            self.remaining_guesses -= 1
            if self._is_hanged():
                self.status = STATUS_LOSE

        self.guesses.append(char)
        if all(c in self.guesses for c in self.word):
            self.status = STATUS_WIN

    def _is_hanged(self) -> bool:
        return self.remaining_guesses < 0

    def get_masked_word(self) -> str:
        return "".join(
            c if c in self.guesses else MASKED_CHAR_DISPLAY for c in self.word
        )

    def get_status(self):
        return self.status

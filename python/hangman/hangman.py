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
        self.mask = [True] * len(word)

    def guess(self, char: str):
        if not self.status == STATUS_ONGOING:
            raise ValueError("The game already finished.")

        is_correct_guess = False

        for correct_char, masked, index in zip(
            self.word, self.mask, range(len(self.word))
        ):
            if masked:
                if correct_char == char:
                    self.mask[index] = False
                    is_correct_guess = True

        if is_correct_guess:
            if not any(self.mask):
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self._is_hanged():
                self.status = STATUS_LOSE

    def _is_hanged(self) -> bool:
        return self.remaining_guesses < 0

    def get_masked_word(self) -> str:
        masked_word: list[str] = []
        for (char, masked) in zip(self.word, self.mask):
            if masked:
                masked_word.append(MASKED_CHAR_DISPLAY)
            else:
                masked_word.append(char)

        return "".join(masked_word)

    def get_status(self):
        return self.status

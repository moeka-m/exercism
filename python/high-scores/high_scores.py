from typing import List


def latest(scores: List[int]) -> int:
    return scores[-1]


def personal_best(scores: List[int]) -> int:
    return max(scores)


def personal_top_three(scores: List[int]) -> List[int]:
    sortedScores = sorted(scores, reverse=True)
    return sortedScores[:3]

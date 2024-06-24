from collections import Counter


def get_frequencies(text, letters):
    counts = Counter()
    for letter in letters:
        counts[letter] += text.count(letter)
    total = sum(counts.values())
    return {letter: counts[letter] / total for letter in letters}


def score_text(text: bytes, frequencies: dict) -> float:
    score = 0.0
    length = len(text)

    for letter, frequency_expected in frequencies.items():
        frequency_actual = text.count(ord(letter)) / length
        err = abs(frequency_expected - frequency_actual)
        score += err

    return score

from crypto.stats import score_text


def xor(left: bytes, right: bytes) -> bytes:
    return bytes(b1 ^ b2 for b1, b2 in zip(left, right))


def crack_xor_cipher(ciphertext: bytes, frequencies: dict) -> bytes:
    best_guess = (float('inf'), None)

    for candidate_key in range(256):
        full_key = bytes([candidate_key]) * len(ciphertext)
        plaintext = xor(full_key, ciphertext)
        score = score_text(plaintext, frequencies)
        curr_guess = (score, plaintext)
        best_guess = min(best_guess, curr_guess)

    if best_guess[1] is None:
        exit("no key found")
    return best_guess[1]


def crack_xor_cipher_worse(ciphertext: bytes, frequencies: dict, number: int) \
        -> list[tuple[float, bytes]]:
    results = []

    for candidate_key in range(256):
        full_key = bytes([candidate_key]) * len(ciphertext)
        plaintext = xor(full_key, ciphertext)
        score = score_text(plaintext, frequencies)
        curr_guess = (score, plaintext)
        results.append(curr_guess)

    results.sort()
    return results[:number]

from base64 import b16decode, b64encode, b16encode, b64decode


def hex_to_b64(data_hex: bytes) -> bytes:
    return b64encode(b16decode(data_hex, casefold=True))


def b64_to_hex(data_b64: bytes) -> bytes:
    return b16encode(b64decode(data_b64))


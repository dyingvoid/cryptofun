import codecs
from crypto.variables import letter_frequencies
from crypto.single_xor import crack_xor_cipher

with codecs.open('./data/pg1.txt', 'rb', 'utf_8_sig') as f:
    book = f.read()

with open('./data/single-byte-xor') as cipher_file:
    cipher = bytes.fromhex(cipher_file.read())

crack_xor_cipher(cipher, letter_frequencies)

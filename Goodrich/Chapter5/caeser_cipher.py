"""Code Fragment 5.11: A complete Python class for the Caesar cipher."""
from typing import Union, List


# noinspection PyMethodMayBeStatic
class CaesarCipher:
    """Class for doing encryption and decryption using a Caecar cipher."""
    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder: Union[List[str], List[None]] = [None] * 26     # Temporary encryption and
        decoder: Union[List[str], List[None]] = [None] * 26     # decryption array.
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = "".join(encoder)                        # Will store as string
        self._backward = "".join(decoder)                       # since fixed.

    def encrypt(self, message):
        """Return strong representing encypted message."""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')                      # Index from 0 to 25.
                msg[k] = code[j]                                # Replace this character.
        return "".join(msg)


if __name__ == "__main__":
    cipher = CaesarCipher(3)
    text = "THE EAGLE IS IN PLAY; MEET AT JOE S."
    coded = cipher.encrypt(text)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print("Message: ", answer)

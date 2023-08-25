class CeaserCipher:
    """Class for doing encryption and decryption using Ceaser cipher."""

    def __init__(self, shift):
        """Construct Ceaser cipher using the given integer shift for rotation."""
        # encoder = [None] * 26   # temp array for encryption
        # decoder = [None] * 26   # temp array for decryption

        # for k in range(26):
        #     encoder[k] = chr((k + shift) % 26 + ord('A'))
        #     decoder[k] = chr((k - shift) % 26 + ord('A'))

        encoder = [chr((k+shift) % 26 + ord('A')) for k in range(26)]
        decoder = [chr((k-shift) % 26 + ord('A')) for k in range(26)]

        self._foward = "".join(encoder)     # we will store as a string
        self._backward = "".join(decoder)   # since fixed

    def encrypt(self, message):
        """Return string representation of encrypted message."""
        return self._transform(message, self._foward)
    
    def decrypt(self, secret):
        """Return decrypted message given encrypted message."""
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 255
                msg[k] = code[j]
            elif msg[k].islower():
                j = ord(msg[k]) - ord('a')
                msg[k] = code[j].casefold()

        return "".join(msg)


if __name__ == '__main__':
    cipher = CeaserCipher(3)

    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    message = "the eagle is in play; meet at joe's."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)

    answer = cipher.decrypt(coded)
    print('Message: ', answer)

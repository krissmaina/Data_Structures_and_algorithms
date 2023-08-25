from random import randrange


class SubstitutionCipher:
    """Class for doing encryption and decryption using Substition Cipher given the encryption."""

    def __init__(self, encryption: str):
        """Instantiate the class with the given encryption."""
        self._foward = list(encryption)

        decoder = [None] * 26

        for i in range(26):
            origin_index = i + ord('A')
            origin_char = chr(origin_index)

            char = self._foward[i]
            char_index = ord(char) - ord('A')

            decoder[char_index] = origin_char
        
        self._backward = decoder

        
    def encrypt(self, message: str):
        """Encrypts the message according to the encryption provided during construction."""
        return self._transform(message, self._foward)

    def decrypt(self, message: str):
        """Performs a decryption of an encryption."""
        return self._transform(message, self._backward)

    def _transform(self, message: str, code: list):
        """Transforms the message according to the code(self._foward or self._backward) list."""
        msg = list(message)

        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]

        return "".join(msg)


class CeasarCipher(SubstitutionCipher):
    """P-5.36 Challenge -> Redesigning the CeasarCipher class as a subclass of Substitution class."""

    def __init__(self, shift: int):
        encoder = [chr((k + shift) % 26 + ord('A')) for k in range(26)]
        encryption = "".join(encoder)

        super().__init__(encryption)


class RandomCipher(SubstitutionCipher):
    """P-5.37 Challenge -> Each instance of this class relies on a random permutaion of letters for its mapping."""

    def __init__(self):
        encoder = [chr(i + ord('A')) for i in range(26)]

        # shuffle the encoder list
        for i in range(26):
            random_num = randrange(26)
            
            # swap the values at indexes i and random_num
            encoder[i], encoder[random_num] = encoder[random_num], encoder[i]
        
        encryption = "".join(encoder)
        super().__init__(encryption)


if __name__ == '__main__':
    sub_cipher = SubstitutionCipher("QWERTYUIOPASDFGHJKLZXCVBNM")

    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = sub_cipher.encrypt(message)
    print('Secret: ', coded)

    answer = sub_cipher.decrypt(coded)
    print('Answer: ', answer)

    print('*' * 80)
    print('CeasarCipher Encryption: ')

    ceasar_cipher = CeasarCipher(3)
    ceasar_coded = ceasar_cipher.encrypt(message)
    print('CeasarCipher Encoded: ', ceasar_coded)

    ceasar_answer = ceasar_cipher.decrypt(ceasar_coded)
    print('CeasorCipher Decoded: ', ceasar_answer)

    print('*' * 80)
    print('RandomCipher Encryption.')

    random_cipher = RandomCipher()
    random_coded = random_cipher.encrypt(message)
    print('RandomCipher Encoded: ', random_coded)

    random_answer = random_cipher.decrypt(random_coded)
    print('RandomCipher Answer: ', random_answer)
    

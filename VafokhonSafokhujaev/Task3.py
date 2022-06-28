
import string


class Cipher:

    def __init__(self, keyword: str) -> None:
        alphabet = list(string.ascii_lowercase)
        self.txt_to_enc = {}
        self.enc_to_txt = {}

        keyword = keyword.lower()
        letters_in = []
        cipher = []

        for letter in keyword:
            if letter not in letters_in and letter in alphabet:
                letters_in.append(letter)

        cipher = letters_in[::]
        for letter in alphabet:
            if letter not in letters_in:
                cipher.append(letter)

        self.txt_to_enc = {key: val for key, val in zip(alphabet, cipher)}
        copy = self.txt_to_enc.copy()
        
        for key, val in copy.items():
            self.txt_to_enc[key.upper()] = val.upper()

        for key, val in self.txt_to_enc.items():
            self.enc_to_txt[val] = key


    def encode(self, str):
        encoded = ""

        for c in str:
            if c in self.txt_to_enc:
                encoded += self.txt_to_enc[c]
            else:
                encoded += c

        return encoded

    def decode(self, str):
        decoded = ""

        for c in str:
            if c in self.enc_to_txt:
                decoded += self.enc_to_txt[c]
            else:
                decoded += c

        return decoded
        

ciph = Cipher("Crypto")
print(ciph.encode("Hello world"))
print(ciph.decode("Fjedhc dn atidsn"))
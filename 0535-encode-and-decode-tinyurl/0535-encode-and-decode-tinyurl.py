import random
import string

class Codec:
    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits
        self.base_url = "http://tinyurl.com/"
        self.url_to_code = {}
        self.code_to_url = {}

    def _generate_code(self) -> str:
        return ''.join(random.choices(self.alphabet, k=6))

    def encode(self, longUrl: str) -> str:
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]

        code = self._generate_code()
        while code in self.code_to_url:
            code = self._generate_code()

        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl

        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url[code]
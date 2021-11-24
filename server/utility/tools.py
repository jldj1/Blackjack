import random
import string
class Tools:
    @staticmethod
    def get_random_id(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

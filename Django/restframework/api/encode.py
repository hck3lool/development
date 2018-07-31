from jose import jwt


class Encode:
    def __init__(self):
        print("JWT Encode")

    @staticmethod
    def encoding(key, value):
        encoding = jwt.encode({key: value}, "secret-xyz", algorithm="HS256")
        return encoding

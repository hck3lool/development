from jose import jwt


class Decode:
    def __init__(self):
        print("JWT Decode")

    @staticmethod
    def decoding(token):
        decoding = jwt.decode(token, "secret-xyz", algorithms=["HS256"])
        return decoding

from math import floor

class FlagReader:
    @staticmethod
    def read(num: int) -> list:
        binary = []
        while True:
            binary.append(num % 2)
            num = floor(num / 2)
            if num == 0:
                break

        result = []
        for i in range(len(binary)):
            x = binary[i] * (2**i)
            if x > 0:
                result.append(x)

        return result
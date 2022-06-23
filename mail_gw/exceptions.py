EmailAlreadyUsed = 'address: This value is already used'


class EmailAlreadyUsedError(Exception):
    def __init__(self, address: str):
        self.address = address

    def __str__(self):
        return f'{EmailAlreadyUsed}: {self.address}'
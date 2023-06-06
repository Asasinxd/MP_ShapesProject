class MyExceptions(Exception):
    def __init__(self, data: int, message: str = "Invalid input "):
        self.message = message
        self.data = data
        self.message = self.message + str(self.data)
        super().__init__(self.message)

    @staticmethod
    def validInputCircle(r):
        # if int(r):
        #     raise MyExceptions(r, "Invalid type ")

        if r <= 0:
            raise MyExceptions(r)

    @staticmethod
    def validInput(a1, a2, b1, b2):
        # if int(a1):
        #     raise MyExceptions(a1, "Invalid type ")
        #
        # if int(a2):
        #     raise MyExceptions(a2, "Invalid type ")
        #
        # if int(b1):
        #     raise MyExceptions(b1, "Invalid type ")
        #
        # if int(b2):
        #     raise MyExceptions(b2, "Invalid type ")

        if a1 <= 0:
            raise MyExceptions(a1)

        if a2 <= 0:
            raise MyExceptions(a2)

        if b1 <= 0:
            raise MyExceptions(b1)

        if b2 >= 0:
            raise MyExceptions(b2)

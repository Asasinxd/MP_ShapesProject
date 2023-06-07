class MyExceptions(Exception):
    def __init__(self, data: int, message: str = "Invalid input "):
        '''
        Initialize object Exception and passes message to parent class
        :param data: not valid number
        :param message: Custom message
        '''
        self.message = message
        self.data = data
        self.message = self.message + str(self.data)
        super().__init__(self.message)

    @staticmethod
    def validInputCircle(r):
        '''
        Function validates input for functions drawing circle
        :param r: circle radius to validate
        :return: None
        '''
        # if int(r):
        #     raise MyExceptions(r, "Invalid type ")

        if r <= 0:
            raise MyExceptions(r)

    @staticmethod
    def validInput(a1, a2, b1, b2):
        '''
        Function validates input for functions drawing triangle and parallelogram
        :param a1: x value of 'a' vector to validate
        :param a2: y value of 'a' vector to validate
        :param b1: x value of 'b' vector to validate
        :param b2: y value of 'b' vector to validate
        :return:
        '''
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

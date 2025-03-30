"""
Module responsible for defining an object model
to be followed for error handling.
"""


class ErrorHandler(Exception):
    """
    Class that defines the structure of a error.
    """

    def __init__(self, error_code: int, message: str):
        self.error_code = error_code
        self.message = message

    def get_error_description(self) -> str:
        """
        Method responsible for generating an error description message.
        """
        return f"Message: {self.message}. Error Code: {self.error_code}."

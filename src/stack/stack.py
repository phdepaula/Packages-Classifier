"""
Module responsible for classifying packages
into stacks.
"""

from typing import List

from src.package.package import Package
from src.util.error_handler import ErrorHandler


class Stack:
    """
    Class that defines the structure of a Stack.
    """

    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

    def __init__(self, packages: List[Package]):
        self.packages = packages
        self.__stack = []

    def get_stack(self) -> List[str]:
        """
        Method responsible for getting stack.
        """
        return self.__stack

    def __check_if_package_is_bulky(
        self, width: float, height: float, length: float, volume: float
    ) -> bool:
        """
        Method responsible for checking if a package is
        bulky.
        """
        if volume >= 1000000 or width >= 150 or height >= 150 or length >= 150:
            return True

        return False

    def __check_if_package_is_heavy(self, mass: float) -> bool:
        """
        Method responsible for checking if a package is
        heavy.
        """
        if mass >= 20:
            return True

        return False

    def sort(self, width: float, height: float, length: float, mass: float) -> str:
        """
        Method that returns the name of the stack
        where the package should go.
        """
        volume = width * height * length

        bulky = self.__check_if_package_is_bulky(width, height, length, volume)
        heavy = self.__check_if_package_is_heavy(mass)

        if bulky and heavy:
            return self.REJECTED
        elif bulky or heavy:
            return self.SPECIAL

        return self.STANDARD

    def process_packages(self) -> None:
        """
        Method responsible for processing packages.
        """

        try:
            for package in self.packages:
                width, height, length = package.get_dimensions()
                mass = package.get_mass_value()

                stack = self.sort(width, height, length, mass)
                self.__stack.append(stack)
        except Exception as error:
            error_code = 3
            message = "Error processing packages"

            raise ErrorHandler(error_code, message) from error

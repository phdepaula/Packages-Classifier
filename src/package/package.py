"""
Module responsible for defining an object model
to be followed for all packages.
"""

from typing import Dict

from src.util.error_handler import ErrorHandler


class Package:
    """
    Class that defines the structure of a package.
    """

    HEIGHT = "height"
    WIDTH = "width"
    LENGTH = "length"
    UNIT_OF_MEASURE = "unit_of_measure"
    VALUE = "value"
    BULKY = "bulky"
    HEAVY = "heavy"

    def __init__(self, dimensions: Dict, mass: Dict):
        self.dimensions = dimensions
        self.mass = mass
        self.__height = None
        self.__width = None
        self.__length = None
        self.__errors = []

    def __validate_dimensions(self) -> None:
        """
        Method responsible for validating whether the height, width
        and length dimensions have been correctly provided and are
        expressed in centimeters (cm).
        """
        required_dimensions = [self.HEIGHT, self.WIDTH, self.LENGTH]

        for dimension in required_dimensions:
            data = self.dimensions.get(dimension, None)

            if not data:
                self.__errors.append(f"The dimension {dimension} was not reported")
            else:
                unit_of_measure = data.get(self.UNIT_OF_MEASURE, None)
                value = data.get(self.VALUE, None)

                if not unit_of_measure:
                    self.__errors.append(
                        f"The unit of measure of the dimension {dimension}"
                        " was not reported"
                    )
                elif not value:
                    self.__errors.append(
                        f"The value of the dimension {dimension}" " was not reported"
                    )
                elif unit_of_measure != "cm":
                    self.__errors.append(
                        f"The unit of measure of the dimension {dimension}"
                        + " is not in centimeters (cm)"
                    )

    def __validate_mass(self) -> None:
        """
        Method responsible for validating whether the mass
        value has been correctly provided and is expressed
        in kilograms (kg).
        """
        data = self.mass.get(self.VALUE, None)

        if not data:
            error_code = 3
            message = "Package mass was not reported"

            raise ErrorHandler(error_code, message)
        else:
            unit_of_measure = self.mass.get(self.UNIT_OF_MEASURE, None)

            if not unit_of_measure:
                self.__errors.append(f"The unit of measure of mass" " was not reported")
            elif unit_of_measure != "kg":
                self.__errors.append(
                    f"The unit of measure of mass" + " is not in kilograms (kg)"
                )

    def __set_dimensions(self) -> None:
        """
        Method responsible for obtaining the values
        for the dimensions.
        """
        self.__height = self.dimensions[self.HEIGHT][self.VALUE]
        self.__width = self.dimensions[self.WIDTH][self.VALUE]
        self.__length = self.dimensions[self.LENGTH][self.VALUE]

    def get_dimensions(self) -> tuple:
        """
        Method responsible for getting dimensions.
        """
        return self.__width, self.__height, self.__length

    def get_mass_value(self) -> tuple:
        """
        Method responsible for getting mass value.
        """
        return self.mass[self.VALUE]

    def start_package(self) -> None:
        """
        Method responsible for starting a package.
        """
        try:
            self.__validate_dimensions()
            self.__validate_mass()

            if len(self.__errors) > 0:
                error_code = 2
                message = "Error in package data: " f"{", ".join(self.__errors)}"

                raise ErrorHandler(error_code, message)

            self.__set_dimensions()
        except ErrorHandler as error_handler:
            raise error_handler from error_handler
        except Exception as error:
            error_code = 1
            message = "Error starting package"

            raise ErrorHandler(error_code, message) from error

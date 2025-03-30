"""
Module responsible for testing stack
generation.
"""

from typing import List

from src.package.package import Package
from src.stack.stack import Stack
from src.util.error_handler import ErrorHandler


def package_generator(data: List) -> tuple:
    """
    Method responsible for instantiating packages and
    returning a list of packages.
    """
    list_of_packages = []
    errors = []

    for package_data in data:
        dimensions = package_data[0]
        mass = package_data[1]

        package_instance = Package(dimensions, mass)

        try:
            package_instance.start_package()
        except ErrorHandler as error_handler:
            errors.append(error_handler.get_error_description())

            continue

        list_of_packages.append(package_instance)

    return list_of_packages, errors


def test_stack_generation_successfully():
    """
    Test that generates a packet queue without errors.
    """
    dimension_1 = {
        "height": {"value": 100, "unit_of_measure": "cm"},
        "width": {"value": 100, "unit_of_measure": "cm"},
        "length": {"value": 100, "unit_of_measure": "cm"},
    }
    mass_1 = {"value": 20, "unit_of_measure": "kg"}
    package_1 = [dimension_1, mass_1]

    dimension_2 = {
        "height": {"value": 100, "unit_of_measure": "cm"},
        "width": {"value": 100, "unit_of_measure": "cm"},
        "length": {"value": 100, "unit_of_measure": "cm"},
    }
    mass_2 = {"value": 15, "unit_of_measure": "kg"}
    package_2 = [dimension_2, mass_2]

    dimension_3 = {
        "height": {"value": 10, "unit_of_measure": "cm"},
        "width": {"value": 10, "unit_of_measure": "cm"},
        "length": {"value": 10, "unit_of_measure": "cm"},
    }
    mass_3 = {"value": 15, "unit_of_measure": "kg"}
    package_3 = [dimension_3, mass_3]

    dimension_4 = {
        "height": {"value": 150, "unit_of_measure": "cm"},
        "width": {"value": 10, "unit_of_measure": "cm"},
        "length": {"value": 10, "unit_of_measure": "cm"},
    }
    mass_4 = {"value": 15, "unit_of_measure": "kg"}
    package_4 = [dimension_4, mass_4]

    dimension_5 = {
        "height": {"value": 150, "unit_of_measure": "cm"},
        "width": {"value": 10, "unit_of_measure": "cm"},
        "length": {"value": 10, "unit_of_measure": "cm"},
    }
    mass_5 = {"value": 21, "unit_of_measure": "kg"}
    package_5 = [dimension_5, mass_5]

    data = [package_1, package_2, package_3, package_4, package_5]
    list_of_packages, errors = package_generator(data)

    stack_instance = Stack(list_of_packages)
    stack_instance.process_packages()

    stack = stack_instance.get_stack()

    assert stack == ["REJECTED", "SPECIAL", "STANDARD", "SPECIAL", "REJECTED"]
    assert errors == []


def test_stack_generation_error():
    """
    Test that generates a packet queue without errors.
    """
    dimension_1 = {
        "height": {"value": 100, "unit_of_measure": "m"},
        "width": {"value": 100, "unit_of_measure": "cm"},
        "length": {"value": 100, "unit_of_measure": "m"},
    }
    mass_1 = {"value": 20, "unit_of_measure": "kg"}
    package_1 = [dimension_1, mass_1]

    dimension_2 = {
        "height": {"value": 100, "unit_of_measure": "cm"},
        "width": {"value": 100, "unit_of_measure": "cm"},
        "length": {"value": 100, "unit_of_measure": "cm"},
    }
    mass_2 = {"value": 15, "unit_of_measure": "g"}
    package_2 = [dimension_2, mass_2]

    dimension_3 = {
        "height": {"value": 10, "unit_of_measure": "cm"},
        "width": {"value": 10, "unit_of_measure": "cm"},
        "length": {"value": 10, "unit_of_measure": "cm"},
    }
    mass_3 = {"value": 15, "unit_of_measure": "kg"}
    package_3 = [dimension_3, mass_3]

    dimension_4 = {
        "height": {"value": 150, "unit_of_measure": "cm"},
        "width": {"value": 10, "unit_of_measure": "m"},
        "length": {"value": 10, "unit_of_measure": "cm"},
    }
    mass_4 = {"value": 15, "unit_of_measure": "kg"}
    package_4 = [dimension_4, mass_4]

    dimension_5 = {
        "height": {"value": 150, "unit_of_measure": "cm"},
        "width": {"value": 10, "unit_of_measure": "cm"},
        "length": {"value": 10, "unit_of_measure": "cm"},
    }
    mass_5 = {"value": 21, "unit_of_measure": "g"}
    package_5 = [dimension_5, mass_5]

    data = [package_1, package_2, package_3, package_4, package_5]
    list_of_packages, errors = package_generator(data)

    instance_success = len(list_of_packages)
    instance_of_error = len(errors)

    assert instance_success == 1
    assert instance_of_error == 4

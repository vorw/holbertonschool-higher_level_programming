#!/usr/bin/python3
"""
Module that contains the function say_my_name.

The function prints the full name after validating input types.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Bob")
        My name is Bob
        >>> say_my_name(12, "White")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")

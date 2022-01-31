#!/usr/bin/env python3
"""
Type-annotated function  which takes a list input_list of floats
as argument and returns their sum as a float.
"""
from typing import List  # NewType helper class to create distinct types


def sum_list(input_list: List[float]) -> float:
    """ Returns their sum as a float """
    return sum(input_list)

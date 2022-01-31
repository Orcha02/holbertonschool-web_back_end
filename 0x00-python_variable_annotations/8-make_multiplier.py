#!/usr/bin/env python3
"""
Type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """
    return lambda f_num: f_num * multiplier


"""
NORMAL PYTHON FUNCTION:

def function(f_num):
   return f_num * multiplier
"""

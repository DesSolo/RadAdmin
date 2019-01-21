"""
OPERATOR_CHOICE - https://wiki.freeradius.org/config/Operators
"""
from .utils import include

OPERATORS = [':=', '=', ',=', '==', '+=', '!=', '>', '>=', '<', '<=', '=~', '!~', '=*', '!*']
OPERATORS_CHOICE = include(OPERATORS)


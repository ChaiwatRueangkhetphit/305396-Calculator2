"""Token"""

# Standard library
from enum import Enum
from collections import namedtuple

# 3rd Party library

# Project library


TokenType = Enum(    
    "TokenType",
    [
        "ERROR",
        "UNKNOWN",
        "EMPTY",
        "LEFT_PAREN",
        "RIGHT_PAREN",
        "ADD_OP",
        "MUL_OP",
        "POWER_OP",
        "FAC_OP",
        "NUMBER",
    ]
)


Token = namedtuple(
    "Token",
    [
        "token_type",
        "lexeme",
    ]
)

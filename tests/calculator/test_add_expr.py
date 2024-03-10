"""Test cases for multiplication expression."""

# Standard library

# 3rd Party library
import pytest

# Project library
from calculator.data_type import FactExpr, Number
from calculator.data_type import PowerExpr
from calculator.data_type import AddExpr
from calculator.data_type import UnaryExpr


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "op, left, right, expected",
    [
        ("+", Number(1), Number(0), 1),
        ("-", Number(5), Number(0), 5),
        ("+", Number(0), Number(7), 7),
        ("-", Number(22), Number(6), 16),
        ("+", Number(2), FactExpr(Number(3)), 8),
        ("-", FactExpr(Number(3)), UnaryExpr("-", Number(5)), 11),
        ("+", PowerExpr(FactExpr(Number(3)), Number(2)), UnaryExpr("+", Number(1)), 37),
    ]
)
def test_add_expr(op, left, right, expected):
    """Calculate the value of the Additional expression."""
    # Arrange
    expr = AddExpr(op, left, right)

    # Act
    result = expr.eval()

    # Assert
    assert result == expected

"""Test cases for lexical analyzer."""

# Standard library

# 3rd Party library
from typing import Literal
import pytest

# Project library
from calculator.token import Token, TokenType
from calculator.lexer import Lexer


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.NUMBER, "456"), 3),
        ("705", 1, Token(TokenType.NUMBER, "05"), 3),
        ("-+", 1, Token(TokenType.ERROR, ""), 1),
    ]
)
def test_number(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_number(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
    
# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("!", 0, Token(TokenType.FAC_OP, "!"), 1),
        ("5!", 1, Token(TokenType.FAC_OP, "!"), 2),
    ]
)
def test_get_fac_op(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    

# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("*", 0, Token(TokenType.MUL_OP, "*"), 1),
        ("/", 0, Token(TokenType.MUL_OP, "/"), 1),
        ("%", 0, Token(TokenType.MUL_OP, "%"), 1),
        ("5*5", 0, Token(TokenType.ERROR, ""), 0),
        ("5*5", 1, Token(TokenType.MUL_OP, "*"), 2),
        ("0/2", 1, Token(TokenType.MUL_OP, "/"), 2),
        ("6%2", 1, Token(TokenType.MUL_OP, "%"), 2),
        ("*/", 0, Token(TokenType.MUL_OP, "*"), 1),
    ]
)
def test_get_mul_op(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
    
# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("^", 0, Token(TokenType.POWER_OP, "^"), 1),
        ("5^5", 0, Token(TokenType.ERROR, ""), 0),
        ("2^5", 1, Token(TokenType.POWER_OP, "^"), 2),
        ("10^2", 2, Token(TokenType.POWER_OP, "^"), 3),
        ("1^2", 1, Token(TokenType.POWER_OP, "^"), 2),
        ("^465", 0, Token(TokenType.POWER_OP, "^"), 1),
    ]
)
def test_get_power(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    

# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("+", 0, Token(TokenType.ADD_OP, "+"), 1),
        ("+-", 1, Token(TokenType.ADD_OP, "-"), 2),
    ]
)
def test_get_add(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    
    
# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("(456)", 0, Token(TokenType.LEFT_PAREN, "("), 1),
        ("()", 0, Token(TokenType.LEFT_PAREN, "("), 1),
        ("()", 1, Token(TokenType.RIGHT_PAREN, ")"), 2),
        ("123*(456)", 0, Token(TokenType.ERROR, ""), 0),
        ("123*(456)", 4, Token(TokenType.LEFT_PAREN, "("), 5),
        ("123*(456)", 8, Token(TokenType.RIGHT_PAREN, ")"), 9),
    ]
)
def test_get_paren(text, pos, expected_token, expected_pos):
    """Extract number from text strting at pos."""
    # Arrange
    lexer = Lexer()
    
    # Act
    token, new_pos = lexer.get_token(text, pos)
    
    # Assert
    assert token == expected_token
    assert new_pos == expected_pos
    

# -----------------------------------------------------------------------------    
@pytest.mark.parametrize(
    "text, pos, new_pos",
    [
        (" abc ", 0, 1),
        (" xyz ", 0, 1),
        (" xyz ", 1, 1),
        (" xyz ", 2, 2),
        (" xyz ", 3, 3),
        (" xyz ", 4, 5),
        (" xyz ", 5, 5),
        ("   pqr", 0, 3),
    ]
)
def test_skip_white_space(text,pos,new_pos):
    """Extract an addition operator from text starting at pos"""
    # Arrange
    lexer = Lexer()
    
    # Act
    result = lexer.skip_white_space(text, pos)
    
    # Assert
    assert result == new_pos
    
    
    
    # -------------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_tokens",
    [
        ("123 + (32 / 4)",0,[
        Token(TokenType.NUMBER, "123"),
        Token(TokenType.ADD_OP, "+"),
        Token(TokenType.LEFT_PAREN, "("),
        Token(TokenType.NUMBER, "32"),
        Token(TokenType.MUL_OP, "/"),
        Token(TokenType.NUMBER, "4"),
        Token(TokenType.RIGHT_PAREN, ")"),
    ])
    ]
)
def test_get_token_list(text,pos,expected_tokens):
    # Arrange
    lexer = Lexer()
    
    # Act
    result = lexer.get_token_list(text,pos)
    
    # Assert
    assert result == expected_tokens
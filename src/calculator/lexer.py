"""A simple lexical analyzer."""

# Standard library

# 3rd Party library

# Project library
from calculator.token import Token,TokenType


class Lexer:
    """A simple lexical analyzer."""
    
    def get_number(self, text, pos):
        """Extract numbrt from text starting at pos.
        
        Args:
            text (str): Text to be scanned.
            pos (int): The starting position to scan.
            
        Returns:
            token:      The extracted token
            pos:        The position after the scanning
        """
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if not text[pos].isdigit():
            return Token(TokenType.ERROR, lexeme), pos
        
        while pos < length and text[pos].isdigit():
            lexeme = lexeme + text[pos]
            pos = pos + 1
            
        return Token(TokenType.NUMBER, lexeme), pos
    
    
    def get_token(self, text, pos):
        """Extract a token."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if text[pos] == "!":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.FAC_OP, lexeme), pos
        elif text[pos] == "^":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.POWER_OP, lexeme), pos
        elif text[pos] == "*":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == "/":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == "%":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == "+":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.ADD_OP, lexeme), pos
        elif text[pos] == "-":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.ADD_OP, lexeme), pos
        elif text[pos] == "(":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.LEFT_PAREN, lexeme), pos
        elif text[pos] == ")":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.RIGHT_PAREN, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos
        
        
    def skip_white_space(self, text, pos):
        """Skip all white spaces.
       
        Args:
            text (str): Text to be scanned.
            pos (int):  The starting position to scan.
           
        Return:
            new_pos (int)   The position after the last white space
       
        """
        length = len(text)
        while pos < length and text[pos].isspace():
            pos += 1
        return pos


    def get_token_list(self, text, pos):
        """
        Extract all tokens from the text.
       
        Args:
            text (str): Text to be scanned.
            pos (int):  The starting position to scan.
           
        Return:
            list_of_tokens   The list of all tokens
       
        """
        list_of_tokens = []
        length = len(text)

        while pos < length:
            # Skip white spaces before extracting the next token
            pos = self.skip_white_space(text, pos)

            if pos >= length:
                break  # Reached the end of the text

            # Try to extract a number
            if text[pos].isdigit():
                token, pos = self.get_number(text, pos)
            else:
                # Extract a token
                token, pos = self.get_token(text, pos)

            list_of_tokens.append(token)

        return list_of_tokens

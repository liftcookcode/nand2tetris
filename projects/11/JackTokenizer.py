import re 
import sys
from collections import namedtuple

# test 
Token = namedtuple('Token',('type', 'value'))

class JackTokenizer:
    ''' A tokenizer for the Jack programming language'''

    # The regular expressions for lexical elements in Jack
    RE_INTEGER = '\d+'
    RE_STRING = '"[^"]*"'
    RE_IDENTIFIER = '[A-z][A-z_\d]*'
    RE_SYMBOL = '\{|\}|\(|\)|\[|\]|\.|,|;|\+|-|\*|/|&|\||\<|\>|=|~'
    RE_KEYWORD = '|'.join(keyword for keyword in [
        'class', 'method', 'constructor', 'function', 'field', 'static', 'var', 
        'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'that',
        'let', 'do', 'if', 'else', 'while', 'return'
    ]) 

    # A list of tuples of a regular expression and its type of string
    LEXICAL_TYPES = [
        (RE_KEYWORD, 'keyword'),
        (RE_SYMBOL, 'symbol'),
        (RE_IDENTIFIER, 'identifier'),
        (RE_INTEGER, 'integerConstant')
        (RE_STRING, 'stringConstant')
    ]

    # A regular expression to spilt between lexical components/tokens
    RE_SPILT = '(' + '|'.join(expr for expr in [RE_SYMBOL,RE_STRING]) + ')|\s+'

    @staticmethod
    def remove_comments(file):
        ''' Remove the comments from a given Jack file '''

        # Use non-greedy regex  to avoid eating lines of code
        uncommented = re.sub('//.*?\n', '\n', file)
        uncommented = re.sub('/\*.*?\*/', '', uncommented, flags=re.DOTALL)
        return uncommented
    
    def __init__(self, file):
        ''' Initialize the tokenizer for a given file, provided as utf-8 encoded python string '''
        self.code = JackTokenizer.remove_comments(file)
        self.tokens = self.tokenize()

    def tokenize(self):
        ''' Tokenize the given input file without comments '''
        split_code = re.split(self.RE_SPILT, self.code)
        tokens = []

        for lex in split_code:
            # Skip non-tokens
            if lex is None or re.match('^\s*$', lex):
                continue

            # Check all possible lexical types, if
            for expr, lex_type in self.LEXICAL_TYPES:
                if re.match(expr, lex):
                    tokens.append(Token(lex_type, lex))
                    break
            else:
                print('Error: unknown token', lex)
                sys.exit(1)

        return tokens
    
    def current_token(self):
        ''' Return the current token, if not existent return None '''
        return self.tokens[0] if self.tokens else None
    
    def advance(self):
        ''' Advance to the next token, return current token '''
        return self.tokens.pop(0) if self.tokens else None
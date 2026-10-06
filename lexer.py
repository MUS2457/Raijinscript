from module import Token

class Lexer :
    def __init__(self, text) :
        self.text = text
        self.position = 0
        self.OP_SYMBOL_TO_TYPE = {
                "+": "Plus",
                "-": "Minus",
                "*": "Star",
                "**": "Power",
                "/": "Slash",
                "=": "Equal",
                "==": "EqEq",
                "!=": "NotEq",
                "<": "Lt",
                "<=": "Lte",
                ">": "Gt",
                ">=": "Gte"
            }


    def current_char(self, offest = 0) :
        pos = self.position + offest
        if pos >= len(self.text) :
            return None
        return self.text[pos]

    def indexplus(self,x) :
        return self.current_char(x) # look ahead is a flexible 

    def advance(self) :
        self.position += 1

    def skip_whiteSpace(self) :
        while self.current_char() is not None :
            if self.current_char() == " " :
                self.advance()
            else :
                break

    def identifier(self, method_name):
        word = ""

        while self.current_char() is not None:
            if getattr(self.current_char(), method_name)():  # )( is needed when a method is called
                word += self.current_char()
                self.advance()
            else:
                break

        return word

    def read_identifier(self, x = "isalpha") :
        return self.identifier(x)

    def number_identifier(self, x = "isdigit") :
        return self.identifier(x)

    def operator_identifier(self):
        c1 = self.current_char()
        c2 = self.indexplus(1)

        two_char = c1 + c2 if c2 is not None else None  # two_char become None if c2 not exit

        if two_char in self.OP_SYMBOL_TO_TYPE:  #if two_chat is None its skip if block work as if False
            op_type = self.OP_SYMBOL_TO_TYPE[two_char]
            self.advance()
            self.advance()
            return (op_type, two_char)

        if c1 in self.OP_SYMBOL_TO_TYPE:
            op_type = self.OP_SYMBOL_TO_TYPE[c1]
            self.advance()
            return (op_type, c1)

        raise Exception(f"Unknown operator: {c1}")



    def string_identifier(self):
        string = ""
        quote = self.current_char()   # ' or "

        if self.indexplus(1) == quote and self.indexplus(2) == quote:
        
            for i in range(3) : # Skip opening triple quotes
                self.advance()

            while self.current_char() is not None:
                if (self.current_char() == quote and
                    self.indexplus(1) == quote and
                    self.indexplus(2) == quote):   # skip closing triple quotes
                    for i in range(3) :
                        self.advance()
                    break

                string += self.current_char()
                self.advance()

            return string

    
        elif self.indexplus(1) == quote : # double qoutes
            for i in range(2) :
                self.advance()

            while self.current_char() is not None :
                if (self.current_char() == quote and
                    self.indexplus(1) == quote) :
                    for i in range(2) :
                        self.advance()
                    break

                string += self.current_char()
                self.advance()

            return string

        self.advance()

        while self.current_char() is not None : # normale quote
            if self.current_char() == quote :
                self.advance()
                break

            string += self.current_char()
            self.advance()

        return string
                    

    def skip_comment(self) :
        x = "#"
        if self.current_char() == x :
            while self.current_char() is not None and self.current_char() != "\n" :
                self.advance()

        return


    def get_next_token(self) :
    
        while self.current_char() is not None :

            if self.current_char() == "(":
                self.advance()
                return Token("LPAREN", "(")

            if self.current_char() == ")":
                self.advance()
                return Token("RPAREN", ")")

            if self.current_char() == " " :
                self.skip_whiteSpace()
                continue

            if self.current_char() == "#" :
                self.skip_comment()
                continue

            if self.current_char() in ("'", '"') :
                value = self.string_identifier()
                return Token("String", value)

            if self.current_char().isdigit() :
                value = self.number_identifier()
                return Token("Number", value)

            if self.current_char().isalpha() :
                value = self.read_identifier()
                return Token("Indentifier", value)


            if self.current_char() == self.OPERATORS[0]:
                value = self.operator_identifier()
                return Token("Plus",value)

            if self.current_char() == self.OPERATORS[1]:
                value = self.operator_identifier()
                return Token("Minus",value)

            if self.current_char() == self.OPERATORS[2] and self.indexplus(1) != self.OPERATORS[2] :
                value = self.operator_identifier()
                return Token("Star",value)

            else :
                self.advance()
                return Token("Power", "**")

            self.advance()

        return Token("EOF", None)  # End of file / no char left!

    def tokenize(self) :
        token = self.get_next_token()
        tokens = []

        while token.type != "EOF" :
            tokens.append(token)
            token = self.get_next_token()

        return tokens

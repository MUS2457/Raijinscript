class Lexer :
    def __init__(self, text) :
        self.text = text
        self.position = 0
        self.OPERATORS = "+-*/=<>!"


    def current_char(self, offest = 0) :
        pos = self.position + offest
        if pos >= len(self.text) :
            return None
        return self.text[pos]

    def indexplus(self) :
        return self.current_char(1)

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
        operators = ""

        while self.current_char() is not None :

            if self.current_char() in self.OPERATORS :
                operators += self.current_char()
                self.advance()

            else :
                break

        return operators


    def string_identifier(self):
        string = ""
        quote = self.current_char()   # ' or "

    # Detect triple quotes
        if self.peek() == quote and self.peek(2) == quote:
        # Skip opening triple quotes
            self.advance()
            self.advance()
            self.advance()

        # Read until closing triple quotes
            while self.current_char() is not None:
                if (self.current_char() == quote and
                    self.peek() == quote and
                    self.peek(2) == quote):
                    self.advance()
                    self.advance()
                    self.advance()
                    break

                string += self.current_char()
                self.advance()

            return string

    # Normal single/double quote
        self.advance()  # skip opening quote

        while self.current_char() is not None:
            if self.current_char() == quote:
                self.advance()  # skip closing quote
                break

            string += self.current_char()
            self.advance()

        return string

                



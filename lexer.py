class Lexer :
    def __init__(self, text) :
        self.text = text
        self.position = 0
        self.OPERATORS = "+-*/=<>!"


    def current_char(self) :
        if self.position >= len(self.text) :
            return None
        return self.text[self.position]

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


    


class Lexer :
    def __init__(self, text) :
        self.text = text
        self.position = 0

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

    def read_identifier(self):
        word = ""

        while self.current_char() is not None:
            if self.current_char().isalpha():
                word += self.current_char()
                self.advance()
            else:
                break

        return word


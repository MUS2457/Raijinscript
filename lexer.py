class Lexer :
    def __init__(self, text) :
        self.text = text
        self.position = 0

    def current_char(self) :
        if self.position >= len(self.text) :
            return None
        return self.text[self.position]

class Parser :
    def __init__(self, tokens) :
        self.tokens = tokens
        self.index = 0
        self.current_token = self.tokens[self.index] if self.tokens else None

    def advance(self) :
        self.index += 1

        if self.index < len(self.tokens) :
            self.current_token = self.tokens[self.index]

        else :
            self.current_token = None

    def indexplus(self) :
        next_index = self.index
        if next_index < len(self.tokens) :
            return self.tokens[next_index]
        else :
            return None
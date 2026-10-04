from ast_nodes import NumberNode, AssignmentNode, ProgramNode, IdentifierNode, BinaryOpNode,StringNode

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

    def parse_factor(self):
        token = self.current_token

        if token.type == "NUMBER":
            self.advance()
            return NumberNode(token.value)

        if token.type == "STRING":
            self.advance()
            return StringNode(token.value)

        if token.type == "IDENTIFIER":
            self.advance()
            return IdentifierNode(token.value)

        if token.type == "LPAREN":
            self.advance()
            expr = self.parse_expression()
            if self.current_token.type != "RPAREN":
                raise Exception("Expected ')'")
            self.advance()
            return expr

        if token.type == "MINUS":
            self.advance()
            factor = self.parse_factor()
            return BinaryOpNode(NumberNode(0), "-", factor)

        if token.type == "PLUS":
            self.advance()
            return self.parse_factor()

        raise Exception(f"Unexpected token in factor: {token}")

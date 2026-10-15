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
        next_index = self.index + 1
        if next_index < len(self.tokens) :
            return self.tokens[next_index]
        else :
            return None

    def parse_factor(self):
        token = self.current_token

    # Number literal
        if token.type == "Number":
            self.advance()
            return NumberNode(token.value)

    # String literal
        if token.type == "String":
            self.advance()
            return StringNode(token.value)

    # Identifier
        if token.type == "Identifier":
            self.advance()
            return IdentifierNode(token.value)

    # Parenthesized expression
        if token.type == "LPAREN":
            self.advance()

            expr = self.parse_expression()

            if self.current_token is None or self.current_token.type != "RPAREN":
                raise Exception("Expected ')'")

            self.advance()
            return expr

    # Unary minus
        if token.type == "Minus":
            self.advance()

            factor = self.parse_factor()

            return BinaryOpNode(
                NumberNode(0),
                "-",
                factor
            )

    # Unary plus
        if token.type == "Plus":
           self.advance()
           return self.parse_factor()

        raise Exception(f"Unexpected token in factor: {token}")

    

    def parser_term(self) :
        # i follow mathematical operations handling (precedence):
        # *, / and ** must be grouped before + and -  ex 3*2 +2 == 6 + 2
    
        node = self.parse_factor()

        while (self.current_token is not None and self.current_token.type in ("Star", "Slash", "Power")) :

            op = self.current_token.value # this equal to /, *..
            self.advance() 
            right_node = self.parse_factor() # right node

            # node stores the AST built so far, ex Number(5) can be later BinaryOpNode(5, "*", 3)
            # Each iteration wraps the previous node into a bigger BinaryOpNode.

            node = BinaryOpNode(node, op, right_node)

        return node  # combine 2 nodes that are related with op

    
    def parser_expression(self) :
        node = self.parser_term() # parser_term not always return a full node like Binaryopnode
                        # if while condition didnt run parser_term == parser_fctor, output Number(5) or IdentifierNode("x")

        while self.current_token is not None and self.current_token.type  in ("Minus", "Plus") :

            op = self.current_token.value
            self.advance()

            right = self.parser_term()

            node = BinaryOpNode(node, op, right)

        return node

               
    def parser_assignment(self) :
        name = ""
        if self.current_token.type == "Identifier" and self.indexplus() is not None and self.indexplus().type == "Equal" :
            name += self.current_token.value
            for i in range(2) :
                self.advance() 
            node = self.parser_expression()
            assign = AssignmentNode(name, node)

            return assign

        else :
            node = self.parser_expression()
            return node



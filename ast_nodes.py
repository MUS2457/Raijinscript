class NumberNode :
    def __init__(self, value) :
        self.value = value


class StringNode :
    def __init__(self, value) :
        self.value = value

class IdentifierNode :
    def __init__(self, value) :
        self.value = value

class BinaryOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class AssignmentNode :
    def __init__(self, name, value) :
        self.value = value
        self.name = name

class ProgramNode :
    def __init__(self, statements) :
        self.statements = statements

    

value_map = {
    "T": True,
    "F": False,
}

operations_map = {
    "&": lambda x,y: x and y,
    "|": lambda x,y: x or y,
    "^": lambda x,y: (x or y) and not (x and y)
}

class BooleanExpression:
    def __init__(self, operation, left, right):
        self.operation = operation
        self.left = left
        self.right = right

    def evaluate_expression(self):
        left_val = value_map[self.left] if self.left in value_map else self.left.evaluate_expression()
        right_val = value_map[self.right] if self.right in value_map else self.right.evaluate_expression()
        evaluation = operations_map[self.operation](left_val, right_val)
        return evaluation

    def __repr__(self):
        return "(%s %s %s)" % (self.left.__repr__(), self.operation, self.right.__repr__())

class BooleanExpressionEvaluator():
    def __init__(self):
        self.partitions = []
        super().__init__()

    def reset(self):
        self.partitions = []

    def evaluate_items(self, items):
        if (len(items) == 1 and isinstance(items[0], BooleanExpression)):
            item = items[0]
            evaluation = item.evaluate_expression()
            self.partitions.append((item, evaluation))

        for index, item in enumerate(items):
            if (is_operation(item)):
                left_val = items[index - 1]
                right_val = items[index + 1]
                operation = items[index]
                expression = BooleanExpression(operation, left_val, right_val)
                new_items = flatten_array([items[:index - 1], [expression], items[index + 2:]])
                self.evaluate_items(new_items)

    def find_valid_partitions(self, items):
        self.reset()
        self.evaluate_items(items)
        return list(filter(lambda x: x[1], self.partitions))


def is_operation(item):
    return item in operations_map

def is_value(item):
    return item in value_map

def flatten_array(array):
    return [val for sub_array in array for val in sub_array]

items = ["F", "|", "T", "&", "T", "&", "T"] # ((F | T) & T) & T, (F | T) & (T & T), F | (T & T) & T, F | (T & (T & T))
items2 = ["T", "|", "T", "&", "F"] # (F | T) & T, F | (T & T)
evaluator = BooleanExpressionEvaluator()
valid_partitions = evaluator.find_valid_partitions(items2)
print(valid_partitions)

class MinStack:

    def __init__(self):
        self.stack = []     # list of dict objects {"val": val of element, "min": min value from this current point in the stack}

    def push(self, val: int) -> None:
        if not self.stack:
            min_val = val
        else:
            top_index = len(self.stack) - 1
            top_index_val = self.stack[top_index]
            min_val = min(top_index_val["min"], val)

        self.stack.append({"val": val, "min": min_val})

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        if self.stack:
            return self.stack[len(self.stack) - 1]["val"]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[len(self.stack) - 1]["min"]

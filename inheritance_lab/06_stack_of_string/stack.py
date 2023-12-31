from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str):
        self.element = element

        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

def reverse_string(input_string):
    stack = Stack()
    reversed_string = ""

    for char in input_string:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# 사용자로부터 문자열 입력 받기
input_string = input("문자열을 입력하세요: ")

# 문자열을 역순으로 출력
reversed_str = reverse_string(input_string)
print("역순으로 출력된 문자열:", reversed_str)

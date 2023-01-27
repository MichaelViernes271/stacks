# class Stack:
#
#     def __init__(self):
#         self.stack_list = []
#
#     def print(self):
#         print(self.stack_list)
#
#     def push(self, item):
#         self.stack_list.append(item)
#
#     def pop(self):
#         return self.stack_list.pop()
#
#     def peek(self):
#         if (self.isEmpty()):
#             return None
#         else:
#             return self.stack_list[-1]
#
#     def isEmpty(self):
#         return self.stack_list == []
#
#     def length(self):
#         return len(self.stack_list)


class Stack(object):
    """the stack data structure - it follow the fifo (first in, first out) rule"""

    def __init__(self):
        """initialize the stack through blank list
        initialize the number of items in stack = 0; stack index
        """
        self.stack = []
        self.number_of_items= 0


    def is_empty(self):
        """ check if stack is empty
        if empty, return true else false
        """
        return self.stack == []

    def push(self, data):
        """put data on top of stack"""
        # insert it at index "num of items". first, at index = 0
        self.stack.insert(self.number_of_items, data)
        # increment index size
        self.number_of_items+= 1
        return '{} pushed to Stack'.format(data)

    def pop(self):
        """remove first element"""
        # decrement the index to point to top of stack
        self.number_of_items-= 1
        # pop out the data from that index
        data = self.stack.pop(self.number_of_items)
        return '{} removed.'.format(data)

    def peek(self):
        if (self.isEmpty()):
            return None
        else:
            return self.stack_list[-1]

    def stack_size(self):
        """returns size of stack/length of stock items"""
        return len(self.stack)

    def display(self):
        """show content"""
        print("The content of stack as follows: ")
        for item in self.stack:
            print(item, end=" | ")
        print("")

def infix2postfix(formula):
    arithmetics_ops = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
    formula = formula.replace(' ', '')
    print("Formula: ", formula)
    result = ''
    stack = []
    stringAdder = ''
    for i in range(len(formula)):
        if (formula[i] == ')'):
            top = stack.pop()
            while (top != '('):
                result += top
                top = stack.pop()
        elif (formula[i] not in arithmetics_ops):
            result += formula[i]

        elif (formula[i] == '('):
            stack.append('(')
        else:
            while (len(stack) > 0 and arithmetics_ops[formula[i]] <= arithmetics_ops[stack[-1]]):
                result += stack.pop()
            stack.append(formula[i])
    while (len(stack) > 0):
        result += stack.pop()

    return result

if __name__ == "__main__":

    problem = ["A * B / 2 + C - D", "(A + B) * C / D + E ^ A / B", "(A + B) + C / D * E ^ A / B", "(A + B) / C / D * E ^ A / B",
               "(A + B) - C / D - E ^ A / B", "(A + B) + C / D * E ^ A / B"]
    print("INFIX 2 POSTFIX CONVERTER".center(60, "="))
    print("SAMPLE IN (e.g: A*B/2+C-D) / OUT (e.g: AB*2/C+D-)".center(60, "="))
    print("="*60)

    for i in problem:
        exprn = input("Enter an expression: ")
        print(infix2postfix(exprn))

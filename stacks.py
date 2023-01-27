import os, time

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

    def stack_size(self):
        """returns size of stack/length of stock items"""
        return len(self.stack)

    def display(self):
        """show content"""
        print("The content of stack as follows: ")
        for item in self.stack:
            print(item, end=" | ")
        print("")

# if __name__ == '__main__':
#
#     stack = Stack()
#
#     # first test
#     print(stack.push("f"))
#     print(stack.push("c"))
#     print(stack.push(6))
#     print(stack.push(9))
#
#     # second test
#     print(stack.pop())
#     print(stack.pop())
#     print('Stack size: ',stack.stack_size())
#     print(stack.pop())
#     print('Stack size: ',stack.stack_size())


class Main:
    """main program for the stack app"""
    def __init__(self):
        self.stack = Stack()

    def display_menu(self):
        """for printing a stylized menu"""

        # for the scribbles wrtten in the menu display
        menu_titles = ["STACK APPLICATION",
        "Programmed by: Viernes, Michael", "BSCOE 2-1", "<<< MAIN MENU >>>", 
        "(1) PUSH", "(2) POP", "(3) DISPLAY", "(4) EXIT"]

        for i in menu_titles:
            if i == menu_titles[0]:
                i = i.center(60, "=")
                print(i)
                continue
            elif i == menu_titles[3]:
                print("=", " "*56, "=")
            i = i.center(56, " ")
            print("=", i, "=")
        print("=" * 60)
        
    def menu_options(self, usr_input):
        try:
            if usr_input == 1: # PUSH
                self.stack.push(input("Enter data: "))
            elif usr_input == 2: # POP
                print(self.stack.pop())
            elif usr_input == 3: # RETURN SIZE
                print("The size of stack is ", self.stack.stack_size())
                self.stack.display()
            elif usr_input == 4: # EXIT1
                quitting = input("Do you want to try again? [y/n] => If yes, the program redisplay the main menu. Otherwise, program exits.")
                if quitting.lower() == "n":
                    print("EXITING...")
                    time.sleep(1)
                    return True
        except Exception:
            input("Please use correct input.")
        input("CLEARING CONSOLE...")
        self.clear_console()
        
    def clear_console(self):
        time.sleep(1)
        os.system("cls") # for windows_os / os.name==nt
        # call("cls" if os.name == "nt" else "clear") # this sometimes not work
        
        
if __name__ == "__main__":
    m = Main()
    while True:
        try:            
            m.display_menu()         
            program = m.menu_options(int(input(">>> Select an option: ")))
            if program:
                break
        except Exception:
            print("Use an appropriate option.")
            time.sleep(1)
            m.clear_console()
    exit()
import parser
import expression

def main():
    """Main calculator program, you shouldn't have to modify it, but feel free to."""
    rpn_parser = parser.Parser()
    while True:
        user_input = input('Enter a postfix expression (or quit): ')
        if user_input.lower() == 'quit':
            break
        print(rpn_parser.parse(user_input).evaluate())


if __name__ == '__main__':
    main()
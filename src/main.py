import sys
import os
from eval import *


def runner(code: str, visitor: EvalVisitor):
    input_stream = InputStream(code)
    lexer = twelveLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = twelveParser(stream)
    tree = parser.program()
    visitor.visit(tree)


def repl():
    visitor = EvalVisitor()
    print("Twelve v25.6.12")
    buffer = ""
    try:
        while True:
            code = input(">>> ")
            buffer += code + "\n"
            if ";" in code:
                runner(buffer, visitor)
                buffer = ""
    except (EOFError, KeyboardInterrupt):
        print("\nExiting Twelve REPL.")
        sys.exit(0)


def main():
    if len(sys.argv) == 1:
        repl()
        return

    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        base, ext = os.path.splitext(input_file)
        if ext.lower() != ".12":
            print(f"Error: Input file '{input_file}' must have a .12 extension")
            sys.exit(1)

        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' does not exist")
            sys.exit(1)

        code = open(input_file, "r", encoding="utf-8").read()
        visitor = EvalVisitor()
        runner(code, visitor)
        return


if __name__ == "__main__":
    main()

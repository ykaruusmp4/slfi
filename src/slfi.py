import os
import subprocess
import sys

from lark import Lark, Transformer

grammar = r"""
    ?start: program

    program: package_decl command* main_function command*

    package_decl: "package" IDENTIFIER

    main_function: "init" "main" "(" ")" "{" command* "}"

    ?command: print_statement

    print_statement: "print" TEXT ";"

    # Strictly defined uppercase terminals
    IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
    TEXT: /"[^"\\]*"/
    COMMENT: /\$[^\n]*/

    %import common.WS
    %ignore WS
    %ignore COMMENT
"""


class SLFITranspiler(Transformer):
    def TEXT(self, token):
        return token.value

    def print_statement(self, args):
        text_content = args[0]
        return f'    printf("%s\\n", {text_content});\n'

    def main_function(self, args):
        inner_commands = "".join(args)
        return inner_commands

    def program(self, args):
        main_body = ""
        for item in args:
            if isinstance(item, str) and "package" not in item:
                main_body += item

        return f"""#include <stdio.h>

int main() {{
{main_body}    return 0;
}}"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python slfi.py <file.slfi>")
        sys.exit(1)

    slfi_file = sys.argv[1]

    if not slfi_file.endswith(".slfi"):
        print("Error: Target file must have a `.slfi` extension.")
        sys.exit(1)

    if not os.path.exists(slfi_file):
        print(f"Error: File '{slfi_file}' not found.")
        sys.exit(1)

    with open(slfi_file, "r") as f:
        slfi_code = f.read()

    try:
        parser = Lark(grammar, parser="lalr")
        syntax_tree = parser.parse(slfi_code)

        transpiler = SLFITranspiler()
        c_code = transpiler.transform(syntax_tree)

        with open("temp_output.c", "w") as f:
            f.write(c_code)

        binary_name = slfi_file.replace(".slfi", "")

        subprocess.run(["gcc", "temp_output.c", "-o", binary_name])

        if os.path.exists("temp_output.c"):
            os.remove("temp_output.c")

        print(f"[SLFI] '{slfi_file}' compiled successfully into './{binary_name}'!")

    except Exception as e:
        print(f"[SLFI] Compilation Error:\n{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

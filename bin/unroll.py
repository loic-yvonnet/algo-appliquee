""" Ridiculously on-purpose complex code.
This is to demonstrate bad practices.
We see all too often this kind of awful code in real world code bases.
Please (please) don't do that...
Instead, use a fully fledged code parser and do not reinvent the wheel.
There are fantastic code parser generators in Python where you just 
need to specify a grammar, and a code generator generates a valid parser.
If you need to implement a parser, follow the best practices with a
tokenizer that generates an abstract syntax tree and use an interpreter
design pattern.
"""

# %%
input_string = """
sum = 0
for i in range(10):
    sum += i
print(sum)
"""

# %%
before = ""
after = ""
loop_declaration = ""
loop_body = ""
loop_variable = ""
loop_indent = 4
range_start = 0
range_increment = 1
range_end = 0
current_indent = 0
previous_word = ""
current_word = ""
in_loop_declaration = False
in_loop_body = False
in_range = False
begin_line = True
check_previous_word = False

# %%
# Split the input string in sections:
# - Before the loop
# - Loop declaration
# - Loop body
# - After the loop
for c in input_string:
    # If not a special character
    if c not in { ",", ":", "(", ")", ";", "\n", " ", "=", "<", ">", "{", "}",
                  "[", "]", "+", "-", "*", "/", "%", "#", "\t", "\r", "\"", "\'" }:
        # Save that character to form the next keyword to analyse
        current_word += c
    elif current_word != "":
        # If this is a special character, we need to analyse the last keyword
        previous_word, current_word = current_word, ""
        check_previous_word = True

    # On a newline character
    if c == "\n":
        # We are about to restart a new line
        current_indent = 0
        begin_line = True

        # If we were in a loop declaration, we move on to the loop body
        if in_loop_declaration:
            in_loop_declaration = False
            in_range = False
            in_loop_body = True

    # Not a new line...
    else:
        # On a space character
        if c == " ":
            # At the beginning of a line, we count the space, which is the indentation
            if begin_line:
                current_indent += 1
        else:
            # The first non-space character breaks the beginning of the line
            begin_line = False

            # A loop body is stopped as soon as the indentation is backward
            if in_loop_body and current_indent < loop_indent + 4:
                in_loop_body = False

    # If the last keyword has to be analysed
    if check_previous_word:
        # Just to be sure that we are in a loop
        if previous_word == "for":
            in_loop_declaration = True
            loop_indent = current_indent
            
            # The last 3 characters were copied to the wrong place so we must fix that
            before = before[:-3]
            loop_declaration = "for"

        # If we are in a loop declaration, the next keyword should be the loop iterator
        elif in_loop_declaration and len(loop_variable) == 0:
            loop_variable = previous_word

        # Keep track of whether we are in a range definition
        elif in_loop_declaration and previous_word == "range":
            in_range = True

        # Weird assumption that the reminder of the current line is about the range
        elif in_range:
            range_end = int(previous_word)

        # The keyword was analyzed (sort of...)
        previous_word = ""
        check_previous_word = False

    # Try to store the next character in the related category
    if in_loop_body:
        loop_body += c
    elif in_loop_declaration:
        loop_declaration += c
    elif len(loop_declaration) == 0:
        before += c
    else:
        after += c

# %%
# Post-processing: decrement indentation + loop unrolling (with bugs...)
final_code = before
lines = loop_body.split("\n")
for i in range(range_start, range_end, range_increment):
    for line in lines:
        if len(line) > 4:
            final_code += line[4:].replace(loop_variable, str(i)) + "\n"
final_code += after

print(final_code)
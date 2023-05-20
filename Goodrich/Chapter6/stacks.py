# Miscellanious scripts from Section 6.1 - Stacks
from Goodrich.Chapter6.array_stack import ArrayStack


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip("\n"))       # Reinisert newlines when writing.
    original.close()
    output = open(filename, 'w')        # Reopening file overwrites original.
    while not S.is_empty():
        output.write(S.pop() + "\n")    # Reinsert newline characters
    output.close()


def is_matched(expr):
    """Return ``True`` if all delimeters are properly matched; ``False`` otherwise."""
    lefty, righty = "({[", ")}]"        # Opening/closing delimeters.
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)                   # Push left delimeter on stack.
        elif c in righty:
            if S.is_empty():
                return False            # Nothing to match with.
            if righty.index(c) != lefty.index(S.pop()):
                return False            # Mismatched.
    return S.is_empty()                 # Were all symbols matched?


# data = """<body> <center> <h1> The Little Boat </h1> </center> <p> The storm tossed the little boat like a cheap sneaker in an old washing machine. The three drunken fishermen were used to such treatment, of course, but not the tree salesman, who even as a stowaway now felt that he had overpaid for the voyage. </p> <ol> <li> Will the salesman die? </li> <li> What color is the boat? </li> <li> And what about Naomi? </li> </ol> </body>"""
def is_matched_html(raw: str):
    """Return ``True`` if all HTML tags are properly matched, ``False`` otherwise."""
    S = ArrayStack()
    j = raw.find("<")                   # Find first '<' character (if any).
    while j != -1:
        k = raw.find(">", j+1)          # Find next '>' character.
        if k == -1:
            return False                # Invalid tag.
        tag = raw[j+1: k]               # Strip away <>
        if not tag.startswith("/"):     # This is opening tag.
            S.push(tag)
        else:                           # This is closing tag.
            if S.is_empty():
                return False            # Nothing to match with.
            if tag[1:] != S.pop():
                return False            # Mismatched delimeter.
        j = raw.find("<", k+1)          # Find next "<" character (if any).
    return S.is_empty()                 # Were all opening tags matched?

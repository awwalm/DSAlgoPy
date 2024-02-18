def test_string_formatting_justification():
    for i, j, k in zip([i for i in range(90, 110)], [i for i in range(90, 110)], [i for i in range(90, 110)]):
        print("%+6s %+6s %+6s" % (i, j, k))

def reverse_string(s):
    sout = []
    recrusive_reversal(s, 0, sout)
    return "".join(sout)

def recrusive_reversal(s: str, ndx: int, output: list):
    if ndx < len(s):
        recrusive_reversal(s, ndx+1, output)
        output.append(s[ndx])


for w in ("racecar", "madam", "radar", "olayinka", "america", "python"):
    print(reverse_string(w))

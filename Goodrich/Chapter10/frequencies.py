"""Code Fragment 10.1: A program for counting word frequencies in a document,
and reporting the most frequent word. We use Python’s dict class for the map.
We convert the input to lowercase and ignore any non-alphabetic characters."""

def get_word_frequency(filename):
    freq = {}
    for piece in open(filename).read().lower().split():
        word = "".join(c for c in piece if c.isalpha())     # Only consider alphabetic characters within piece
        if word:                                            # Require at least one alphabetic character
            freq[word] = 1 + freq.get(word, 0)
    max_word = ""
    max_count = 0
    for (w,c) in freq.items():                              # (key, value) tuples represent (word, count)
        if c > max_count:
            max_word = w
            max_count = c
    print(f"The most frequent word is: {max_word}")
    print(f"Its number of occurences is {max_count}")

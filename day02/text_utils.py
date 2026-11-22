"""
Task 1: text_utils.py

I give you 2 asserts per function; you write the 3rd as an edge case you think of yourself.

"""

def word_count(text):
    pass

text = ""
word_count(text)

assert word_count("hello world") == 2
assert word_count("  many   spaces here ") == 3
assert word_count("") == 0

def chat_frequency(text):
    # text = Aab b
    text_process = text.lower()
    empty_dict = {}
    for ch in text_process:
        if ch.isspace():
            continue
        elif ch in empty_dict:
            empty_dict[ch] += 1
        else:
            empty_dict[ch] = 1

text = ""
chat_frequency(text)

assert chat_frequency("Aab b") == {"a": 2, "b": 2}
assert chat_frequency("") == {}
assert chat_frequency("   ") == {}


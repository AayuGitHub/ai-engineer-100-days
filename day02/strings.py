# A. Strings are immutable sequences

s = "prompt"

print(s[0])
print(s[-1])
print(s[1:4])
print(s[::2])
print(s[::-1])
print("rom" in s)
# s[0] = "P"

# Every string method returns a new string. The classic beginner bug:

name = "  asha  "
name = name.strip()
print(name)

# B. The string methods you’ll use every day

print("a  b  c".split()) # # ['a', 'b', 'c']: no argument splits on any whitespace and drops empties
print("a,,b".split(",")) # ['a', '', 'b']:  with a separator, empty pieces are kept
print(", ".join(["rag", "llm"])) # 'rag, llm': join is called on the SEPARATOR
print("  hi \n".strip())  # 'hi'; also lstrip() and rstrip()
print("v1.2.3".replace(".", "-")) # 'v1-2-3'
print("hello".find("z")) # -1, returns -1 when not found
# print("hello".index("z")) # ValueError: index raises an error instead
# print("doc.md".endswith(".md", ".txt")) # True: accepts a tuple of options
print("model=gpt".partition("=")) # ('model', '=', 'gpt=4'): splits at the FIRST '=' only
print("Straße".casefold()) # 'strasse': stronger than lower(), best for comparing text
print("202".isdigit()) # True
print("banana".count("a")) # 3``

# One important thing to remember: strip() removes characters, not words
print("www.example.com".strip("w.moc")) # 'example'. Surprise!
print("report.pdf".removesuffix(".pdf")) # 'report': the right way to remove an exact ending


# C. f-strings, raw strings and multi-line strings

# Format specs: the part after the colon controls how a value is displayed.

cost, score, x = 1234.5678, 0.8734, 5
print(f"{cost:.2f}") # '1234.57':   2 decimal places
print(f"{cost:,.2f}") # '1,234.57':  thousands separator
print(f"{score:.1%}") # '87.3': as a pecentage
print(f"{'hi':.>6}") #  '    hi|':   right-align in 6 spaces (< left, ^ centre)
print(f"{x=}") # 'x=5':       quick debug print
print(f"P{'hi!r'}") # "'hi'":      shows the repr, with quotes

# Raw strings: a backslash is treated as a normal character, not as an escape code. Always use them for regex patterns.

print(len("\n"))
print(len(r"\n"))

# Multi-line strings: this is how prompt templates are usually written.

PROMPT = """You are a support assistant.
Answer only from the context.

Context:
{context}

Question: {question}"""

PROMPT.format(context="...", question="...")

# Use .format() when the template is written before the values exist. An f-string fills in values immediately.
# AI gotcha: if your prompt contains literal curly braces, such as a JSON example, double them as {{ and }}. Otherwise .format() breaks.

# D. Unicode: str vs bytes
# - A str is a sequence of Unicode characters (code points).
# - bytes are raw numbers from 0 to 255: what actually gets stored on disk and sent over the network.
# - .encode() turns a str into bytes; .decode() turns bytes back into a str.

print("café".encode("utf-8"))
print(len("café"), len("café".encode("utf-8")))
print(len("🙂"), len("🙂".encode("utf-8")))

# UTF-8 uses a variable number of bytes per character: 1 for English letters, 2 for é, 3 for Devanagari, 4 for emoji. Hindi characters take 3 bytes each. And what looks like one Hindi letter can be more than one character in Python. Task 5 lets you see that for yourself.

"""
Where you’ll meet bytes in real work:

Files opened in "rb" mode
response.content (bytes) vs response.text (str) in HTTP libraries
Images base64-encoded for vision APIs
Hashing, for example a cache key for LLM responses: hashlib.sha256(prompt.encode()).hexdigest()
"""

"""
E. Why "".join(parts) beats += in a loop
Strings are immutable, so s += piece builds a brand-new string every time and copies everything so far. Over a loop the copying adds up, roughly n² work.
"".join(parts) works out the final size once and builds the string in one go.

CPython has a special optimisation that sometimes rescues +=, so your benchmark may show a smaller gap than this theory suggests. That optimisation isn't guaranteed, which is why join is the reliable habit.
"""

# +=
words = ["A", "B", "C", "D"]
s = ""
for w in words:
    s += w

# "".join()
# the fast, reliable way
words = ["A", "B", "C", "D"]
s = "".join(words)
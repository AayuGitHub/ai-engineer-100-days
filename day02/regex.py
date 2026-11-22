"""
F. Regex basics with re

The building blocks:

Pattern	Matches
\d \w \s	a digit / a letter, digit or _ / whitespace
\D \W \S	the opposite of each
.	any character except a newline
[abc] [^abc] [a-z]	one of these / none of these / a range
^ $ \b	start of string / end of string / word boundary
* + ? {3} {2,4}	0 or more / 1 or more / optional / exactly 3 / 2 to 4
( ) (?: ) |	capture a group / group without capturing / or
"""

import re
text = "Order ORD-1042 shipped, ORD-2210 pending."

print(re.findall(r"ORD-\d+", text)) # ['ORD-1042', 'ORD-2210']
print(re.findall(r"ORD-(\d+)", text))  # ['1042', '2210']: with a group, findall returns ONLY the group

m = re.search(r"ORD-(\d+)", text)
print(m)
print(m.group(0), m.group(1))
print(re.match(r"ORD", text))
print(re.fullmatch(r"ORD-\d{4}", "ORD-1042"))
print(re.sub(r"\s+", " ", "too    many   spaces"))

ORDER_RE = re.compile(r"ORD-(\d+)")
print(ORDER_RE.findall(text))


html = "<b>bold</b> and <i>italic</i>"
print(re.findall(r"<.+>", html) )
print(re.findall(r"<.+>?", html) )
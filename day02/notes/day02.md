The examples here deliberately use different numbers from your Build tasks, so your predictions there are real tests.

## A. The four kinds of numbers

**int:** whole numbers of any size. Python integers never overflow; they just grow.

```python
print(10 ** 30 + 1)    # 1000000000000000000000000000001, exact
```

**float:** 64-bit binary floating point (IEEE-754).

Many decimal fractions like `0.1` can’t be stored exactly in binary, the same way 1/3 can’t be written exactly in decimal (0.333…).
Tiny errors appear in the results.

```python
print(0.1 + 0.7)                          # 0.7999999999999999
import math
math.isclose(0.1 + 0.7, 0.8)              # True:  the right way to compare floats
math.isclose(1e-12, 0.0)                  # False: relative tolerance fails near zero
math.isclose(1e-12, 0.0, abs_tol=1e-9)    # True:  near zero, add abs_tol
```

**Decimal:** exact decimal arithmetic, for money and anywhere decimal places must be exact.

```python
from decimal import Decimal
Decimal("0.1") + Decimal("0.7")   # Decimal('0.8')
Decimal(0.1)                      # Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

Always build a `Decimal` from a string. Building it from a float copies the float’s error in.

**Fraction:** exact ratios.

```python
from fractions import Fraction
Fraction(1, 3) * 3                # Fraction(1, 1)
```

## B. Operators

### Division: `/`, `//` and `%`

```python
9 / 4     # 2.25: / ALWAYS returns a float
9 // 4    # 2:    floor division
-9 // 4   # -3:   rounds DOWN toward minus infinity (-2.25 becomes -3), not toward zero
-9 % 4    # 3:    the remainder takes the sign of the divisor
9 % -4    # -3
```

They always satisfy this rule: `a == (a // b) * b + (a % b)`. If you’re unsure of a result, check it with this.

### Other arithmetic

```python
divmod(17, 5)   # (3, 2): floor division and remainder in one call
pow(3, 4)       # 81, same as 3 ** 4
pow(3, 4, 5)    # 1:  (3 ** 4) % 5, computed efficiently
```

### Precedence, the two rules people get wrong:

- `**` binds tighter than a leading minus sign, so `-x ** 2` means `-(x ** 2)`.
- A chain of `**` is evaluated right to left.

**Augmented assignment:** `+= -= *= /= //= %= **=`. Remember Day 1: on immutable types these create a new object.

**Walrus `:=`** assigns a value inside an expression:

```python
scores = [0.82, 0.91, 0.77]
if (n := len(scores)) >= 3:
    print(f"{n} scores, enough to average")
```

**Chained comparisons:**

```python
temperature = 0.7
print(0 <= temperature <= 2)   # True; means 0 <= temperature and temperature <= 2
```

## C. Truthiness

Every value counts as either `True` or `False` when used in an `if`.

**Falsy:** `None`, `False`, `0`, `0.0`, `Decimal(0)`, `""`, `[]`, `()`, `{}`, `set()`, `range(0)`

**Truthy:** everything else, including every non-empty string and every non-empty collection

`and` and `or` return one of their operands, not necessarily `True` or `False`:

- `a or b` gives back `a` if `a` is truthy, otherwise `b`.
- `a and b` gives back `a` if `a` is falsy, otherwise `b`.
- `not x` always returns a real `True` or `False`.

```python
print("" or "default")   # 'default'
print(5 and 10)          # 10
print(None and 10)       # None
print(not "")            # True
```

Short-circuiting: Python stops as soon as it knows the answer. In `user and user.name`, the second part never runs if `user` is `None`.

The trap you’ll meet in AI code:

```python
def call_model(temperature=None):
    temperature = temperature or 0.7    # BUG: temperature=0 silently becomes 0.7
```

0 is a valid temperature but it’s falsy. Use `if temperature is None: temperature = 0.7` instead.

## D. Converting between types

```python
int("42")        # 42
int(" 42\n")     # 42: surrounding whitespace is ignored
int("4.2")       # ValueError: the string must look like a whole number
int(4.9)         # 4: chops off the decimal part, it does NOT round
int("ff", 16)    # 255: second argument is the base (hexadecimal here)
float("1e3")     # 1000.0
str(7) + "B"     # '7B'
bool("")         # False
True + True      # 2: bool is a subclass of int
```

### None vs NaN:

`None` means “no value at all”. There is exactly one `None` object.
NaN (“not a number”) is a float that represents an undefined or missing number. pandas uses it for missing numeric data.

```python
nan = float("nan")
nan == nan        # False: NaN isn't equal to anything, not even itself
math.isnan(nan)   # True:  the correct way to check
nan + 1           # nan:   quietly spreads through your maths
None + 1          # TypeError: fails loudly
```

## E. Useful built-in functions

```python
abs(-4.5)                              # 4.5
round(0.5), round(1.5)                 # (0, 2): halfway cases go to the EVEN neighbour ("banker's rounding")
round(1.005, 2)                        # 1.0: 1.005 is actually stored as 1.00499999...
max(["gpt", "claude", "o"], key=len)   # 'claude': key= says what to compare by
sum([0.1] * 10)                        # 0.9999999999999999
math.fsum([0.1] * 10)                  # 1.0: accurate sum for floats
```

## Three mistakes to avoid

1. Comparing floats with `==`. Use `math.isclose`, and add `abs_tol` when comparing against 0.
2. `Decimal(0.1)` instead of `Decimal("0.1")`.
3. `x or default` when 0, `""` or `[]` are valid values. Use `is None`.

## Where this shows up in AI work

- Settings like `temperature=0` and `top_p`: the or-default bug above is real and common in production code.
- LLM costs: price per million tokens × tokens used. Floats are fine for dashboards; use `Decimal` for billing.
- NaN in evaluation scores: one NaN turns the average of all your scores into NaN. You’ll handle this in pandas on Day 26.
- `//` and `%` for batching: number of batches is `(n + size - 1) // size`; `%` assigns items in rotation across workers or API keys.

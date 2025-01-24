"""
Filter
The built-in filter function takes a function and an iterable (in this case a list) and returns a new iterable that only contains elements from the original iterable where the result of the function on that item returned True.

filter function

In Python:

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
Copy icon
Assignment
Complete the remove_invalid_lines function. It accepts a document as input. It should:

Use the built-in filter function and a lambda to return a copy of the input document
Remove any lines that start with a - character.
Keep all other lines and preserve trailing newlines.
For example, this:

* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best

Copy icon
Should become:

* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best

Copy icon
Tips
The splitlines method does not preserve trailing newlines and may cause your output to fail the tests.

The following methods may be useful:

.join

"\n".join(["a", "b", "c"])
# a
# b
# c
Copy icon
.startswith

s = "hello"
s.startswith("h")
# True
s.startswith("o")
# False
Copy icon
.split
"""
s = """hello
world"""
lines = s.split("\n")
# ['hello', 'world']
"""
"""

# solution 1 

"""
def remove_invalid_lines(document):
    return "\n".join(filter(lambda x: x.startswith("*") or len(x) == 0, document.split("\n")))

"""

# solution 2

"""
def remove_invalid_lines(document):
    return "\n".join(filter(lambda x: not x.startswith("-"), document.split("\n")))
"""

def remove_invalid_lines(document):
    return "\n".join(filter(lambda x: not x.startswith("-"), document.split("\n")))
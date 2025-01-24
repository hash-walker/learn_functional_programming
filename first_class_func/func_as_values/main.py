"""
Functions As Values
In Python, functions are just values, like strings, integers, or objects. For example, we can assign an existing function to a variable:

def add(x, y):
    return x + y

# assign the function to a new variable
# called "addition". It behaves the same
# as the original "add" function
addition = add
print(addition(2, 5))
# 7
Copy icon
Assignment
With the popularity of generative AI (like ChatGPT), we need to be able to convert files into pure text to be injected into prompts.

Complete the file_to_prompt function. It should take a file dictionary and a to_string function as inputs and return a formatted string. The provided to_string function is responsible for converting the file dictionary into a string: you don't need to implement it, it's a value passed to your function.

However, your function should wrap the result of the to_string function in triple backticks (```) to format it as a code block in Markdown. For example:

an example string
Copy icon
should become:

```
an example string
```
Copy icon
Tips
Notice the two newlines in the example above! You don't need a trailing newline, but you do need the 2 newlines between the triple backticks. You can achieve this by using the newline \n escape character. Here's an example:

print("I wish the ring had never come to me.\nI wish none of this had happened.")
Copy icon
becomes:

I wish the ring had never come to me.
I wish none of this had happened.
"""

def file_to_prompt(file, to_string):
    return f"```\n{to_string(file)}\n```"

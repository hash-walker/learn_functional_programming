"""
Custom Commands
Doc2Doc is customizable. New commands can be configured to use whichever function suits the user. However, the new commands are causing bugs in other parts of the application by mutating global values and other unintended side effects.

Assignment
Fix the functions add_custom_command, add_format, save_document and add_line_break to make them pure functions without side effects. Here are the reported issues:

add_custom_command: is an impure function that is mutating an input
add_format: is an impure function that is mutating an input
save_document: is an impure function that is mutating an input
add_line_break: is a no-op function with a side-effect
"""

default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    commands_copy = commands.copy()
    commands_copy[new_command] = function
    return commands_copy


def add_format(formats, format):
    formats_copy = formats.copy()
    formats_copy.append(format)
    return formats_copy


def save_document(docs, file_name, doc):
    docs_copy = docs.copy()
    docs_copy[file_name] = doc
    return docs_copy


def add_line_break(line):
    return line + "\n\n"

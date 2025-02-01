"""
Copy/Paste
Doc2Doc has a simple clipboard for copying to and pasting from a cache. Initialize the clipboard to set and get strings.

Assignment
Complete the new_clipboard function. It accepts a dictionary as input and returns two functions, copy_to_clipboard and paste_from_clipboard. It should not modify the original input dictionary.

copy_to_clipboard: It takes a key and value string pair and adds them to the clipboard dictionary.
paste_from_clipboard: It takes a key string and returns its value from the clipboard dictionary. If the key is missing from the clipboard, return an empty string.

"""

def new_clipboard(initial_clipboard):
    copy_ = initial_clipboard.copy()

    def copy_to_clipboard(key, value):
        copy_[key] = value
        return copy_
    
    def paste_from_clipboard(key):
        if key in copy_:
            return copy_[key]
        
        return ""

    return copy_to_clipboard, paste_from_clipboard
"""
Debugging FP
It's nearly impossible, even for tenured senior developers, to write perfect code the first time. That's why debugging is such an important skill. The trouble is, sometimes you have these "elegant" (sarcasm intended) one-liners that are tricky to debug:

def get_player_position(position, velocity, friction, gravity):
    return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)
Copy icon
If the output of get_player_position is incorrect, it's hard to know what's going on inside that black box. Break it up! Then you can inspect the moved, slowed, and final variables more easily:

def get_player_position(position, velocity, friction, gravity):
    moved = calc_move(position, velocity)
    slowed = calc_friction(moved, friction)
    final = calc_gravity(slowed, gravity)
    print("Given:")
    print(f"position: {position}, velocity: {velocity}, friction: {friction}, gravity: {gravity}")
    print("Results:")
    print(f"moved: {moved}, slowed: {slowed}, final: {final}")
    return final
Copy icon
Once you've run it, found the issue, and solved it, you can remove the print statements.

Assignment
Fix the format_line function. It should apply the following transformations in order:

Strip whitespace from the beginning and end of the line.
Capitalize every character in the line.
Remove any periods from the line.
Suffix the line with an ellipsis: words go here...
Run the code. You should see that some subtle bugs are present.

Break up the function to make it easier to debug. Use print() statements to see what's going on at each step.

Tips
Be careful about whitespace! It's easy to miss in console output. I sometimes add a character, like a | to the beginning and end of a string to make whitespace more obvious when print debugging.

.replace(old, new) can be used to replace all instances of a character in a string.
.upper() capitalizes an entire string, .capitalize() capitalizes the first letter.
.strip() removes whitespace from the beginning and end of a string, .lstrip() and .rstrip() remove whitespace from the left and right respectively.
"""

"""
Code to debug

def format_line(line):
    return f"{line.rstrip().capitalize().replace(',', '')}...."

"""

def format_line(line):

    strip = line.strip()
    capitalize = strip.upper()
    final_line = capitalize.replace('.', '')
    
    return f"{final_line}..."
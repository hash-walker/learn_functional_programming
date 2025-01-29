"""
Recursion
Recursion is a famously tricky concept to grasp, but it's honestly quite simple - don't let it intimidate you! A recursive function is just a function that calls itself!

Recursion is the process of defining something in terms of itself.


Example of Recursion
If you thought loops were the only way to iterate over a list, you were wrong! Recursion is fundamental to functional programming because it's how we iterate over lists while avoiding stateful loops. Take a look at this function that sums the numbers in a list:

def sum_nums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15
Copy icon
Don't break your brain on the example above! Let's break it down step by step:

1. Solve a Small Problem
Our goal is to sum all the numbers in a list, but we're not allowed to loop. So, we start by solving the smallest possible problem: summing the first number in the list with the rest of the list:

return nums[0] + sum_nums(nums[1:])
Copy icon
2. Recurse
So, what actually happens when we call sum_nums(nums[1:])? Well, we're just calling sum_nums with a smaller list! In the first call, the nums input was [1, 2, 3, 4, 5], but in the next call it's just [2, 3, 4, 5]. We just keep calling sum_nums with smaller and smaller lists.

3. The Base Case
So what happens when we get to the "end"? sum_nums(nums[1:]) is called, but nums[1:] is an empty list because we ran out of numbers. We need to write a base case to stop the madness.

if len(nums) == 0:
    return 0
Copy icon
The "base case" of a recursive function is the part of the function that does not call itself.

Assignment
Doc2Doc can automatically generate various layouts for a page. There are a lot of possible layouts, so we need a factorial function to calculate the total number of possible layouts.

A factorial is the product of all positive integers less than or equal to a number. For example, 5! (read: "five factorial") is 5 * 4 * 3 * 2 * 1, which is 120.

Complete the factorial_r function. It should recursively calculate the factorial of a number.

Tips
What's a small problem you can solve first?
How can you go from the "first" value of x to the "next" value of x, all the way down to the "last" value of x?
What's the base case that should stop the recursion?
Since 0! is an empty product, what should an input of 0 return?
"""

def factorial_r(x):

    if x == 0 or x == 1:
        return 1
    
    return x * factorial_r(x-1)
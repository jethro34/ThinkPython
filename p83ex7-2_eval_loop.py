# function that iteratively prompts the user, takes the input, evaluates it, and prints the result
# it should continue until "done", and the return the value of the last evaluated expression

import math


def eval_loop():
    """Mathematically evaluates a string input"""
    last_user_input = "0"
    while True:
        user_input = input("please enter a mathematical expression: ")
        if user_input == 'done':
            return eval(last_user_input)
        print(eval(user_input))
        last_user_input = user_input


print(eval_loop())

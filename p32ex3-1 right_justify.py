def right_justify(string):
    final_str = ""
    for sp in range(1, 71 - len(string)):
        final_str += " "
    print(final_str + string)


right_justify("monty")
right_justify("adsfljf;lkasf")
right_justify("1234567890123456789012345678901234567890123456789012345678901234567890")
right_justify("seras tarru?")

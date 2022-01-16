def do_twice(f, val):
    f(val)
    f(val)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def print_spam(val):
    print(val)


do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)


do_twice(print,'spam')
print('')

do_four(print, "spam")

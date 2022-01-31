import random


class Class:
    """Creates a Class class."""

    def __init__(self, class_name, st_total):
        self._class_name = class_name
        self._st_total = st_total
        self._roster = []


class Student:
    """Creates a Student class."""

    def __init__(self, bday=0):
        """Initializes a Student object."""
        self._bday = bday


def populate_class(cl):
    """Creates a class of n Student objects."""

    for i in range(cl._st_total):
        cl._roster.append(Student())


def assign_birthday(st_list):
    """Assigns random birthdays to students in a given list."""

    for st in st_list:
        month = random.randint(1, 12)

        if month == 2:
            day = random.randint(1, 28)
        elif month in [4, 6, 9, 11]:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
        st.bday = month, day


def check_bday(cl):
    """Returns True if there is a birthday match in a given Class object."""
    for i in range(cl._st_total - 1):
        for j in range(i + 1, cl._st_total):
            # print("checking i:", i, "against j: ", j)
            if cl._roster[i].bday == cl._roster[j].bday:
                return True
    return False


c1 = Class('CS161', 23)
populate_class(c1)

count_True = 0

for n in range(100):
    assign_birthday(c1._roster)
    if check_bday(c1):
        count_True += 1

print("There were ", count_True, "birthday matches.")

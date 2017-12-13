#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

import os
import sys

import not_exists_module



HOSTNAME = os.getenv("HOSTNAME", "NONE")
print HOSTNAME

unused = 'This variable is unused.'

def toolong():
    temp = "This is too long,too long,too long,too long,too long,too long,too long,too long,too long,"
    pass

def todo():
    #TODO: todo function
    pass

def not_exists():
    with open("t.txt", "wb") as f:
        f.write("xxx")

def place_holder():
    print '%s %s %s %s' % "place holder xxx "

def xxx(arg):
    str1 = "".split("")
    str2 = 100 + "text"
    pass
    

class Demo:
    class_var = 'class_var'


class Demo1():
    """Demo1"""
    def __init__(self, name):
        self.name = name

    def show_text(self, txt):
        print txt

class Demo2(Demo1):
    """Demo2"""
    def __init__(self, name):
        super(Demo2, self).__init__(name)



def main():
    d1 = Demo1("demo1")
    d2 = Demo2("demo2")
    not_exists()
    place_holder()

if __name__ == "__main__":
    main()


#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

# trying my own function
def repeat(n, exclaim):
  """
  This is what large comments look like. Triple quotes
  Anyways, this just repeats the input. Or adds it, depending on type
  """
  # the * operator means repeat. Multiplies numbers, repeats strings
  result = n * 3
  if exclaim:
    result = result + '!!!'
  print result


# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'

    # booleans begin with capital letters in Python
  repeat(name, True)
  print 'Whats gooooooood', name
  # print 'YAS BITCH'
  # print len(sys.argv)
  # my name is hard coded here, and booleans need cap letters
  # repeat('Brian', True)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

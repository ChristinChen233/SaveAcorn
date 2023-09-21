"""
A simple program that will import your tests and run them all!
Be sure you include tests for your other modules like cells and player!

Usage: python3 test_all.py
"""

import subprocess
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser

print("###########################")
print("### Running unit tests! ###")
print("###########################\n")

test_game()
test_grid()
test_parser()

# Run the e2e script， pls tap bash test_e2e.sh into terminal
# subprocess.call(['./test_e2e.sh'])

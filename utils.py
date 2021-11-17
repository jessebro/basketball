import sys
from enum import Enum
import os


def clear():
	if sys.platform.startswith("win"):
		os.system('cls')
	else:
		os.system('clear')


def print_stuff(script):
	clear()
	print(script)
	input(">>>")

def input_stuff(prompt, options):
	while True:
		choice = input(prompt)
		if choice in options:
			break
	return choice


class Color(Enum):
	BLACK = '\033[30m'
	RED = '\033[31m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	BLUE = '\033[34m'
	PURPLE = '\033[35m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	UNDERLINE = '\033[4m'
	RESET = '\033[0m'
	BOLD = '\33[1m'

	ENEMY = '\033[31m'     # RED
	ALLY = '\033[92m'       # GREEN2


def colour_it(msg, color=Color.RESET):
	if not isinstance(color, Color):
		color = Color.RESET
	return color.value + msg + Color.RESET.value

import random

from utils import print_stuff
from utils import clear
from utils import input_stuff
from utils import colour_it
from utils import Color
import players


def set_positions():
	keys = list(players.goodies.keys())
	while True:
		positions = ["point guard", "small forward", "center", "power forward", "shooting guard"]
		positions_taken = []
		options = ["1", "2", "3", "4", "5"]
		for player in keys:
			clear()
			print(colour_it(players.goodies[player].name, Color.ALLY))
			print(f"""Set where you want {colour_it(players.goodies[player].name, Color.ALLY)} to be.""")
			counter = 0
			for position in positions:
				if position not in positions_taken:
					counter += 1
					print(f"""{counter}. {position.title()} """)
			print(f"""
This player's stats are:
Offense: {players.goodies[player].offense}
Defence: {players.goodies[player].defence}
Speed: {players.goodies[player].speed}""")
			position = input_stuff("""
Select the corresponding number of a position.
>>> """, options)
			players.goodies[player].position = positions[int(position) - 1]
			positions_taken.append(players.goodies[player].position)
			positions.remove(players.goodies[player].position)
			options.remove(options[len(options) - 1])
		clear()
		print("Your team's positions are:")
		for player in keys:
			print(f"{colour_it(players.goodies[player].name, Color.ALLY)}: {players.goodies[player].position.title()}")
		confirm = input_stuff("""Do you wish to continue with this team? (y/n)
>>> """, ["y", "n", "Y", "N"])
		if confirm.lower() == "y":
			break


def enemy_setup():
	positions = ["point guard", "small forward", "center", "power forward", "shooting guard"]
	keys = list(players.baddies.keys())
	for player in keys:
		role = random.choice(positions)
		players.baddies[player].position = role
		positions.remove(role)

from utils import print_stuff
from utils import clear
from utils import input_stuff
from utils import colour_it
from utils import Color
import players

def set_positions():
	positions = ["point guard", "small forward", "center", "power forward", "shooting guard"]
	keys = list(players.goodies.keys())
	while True:
		clear()
		for player in keys:
			print(colour_it(players.goodies[player].name, Color.ALLY))
			print(f"""Set where you want {colour_it(players.goodies[player].name, Color.ALLY)} to be. There are five positions.

1. {positions[0].title()} (Offensive)
2. {positions[1].title()} (Offensive)
3. {positions[2].title()} (Neutral)
4. {positions[3].title()} (Defensive)
5. {positions[4].title()} (Defensive)

This player's stats are:
Offense: {players.goodies[player].offense}
Defence: {players.goodies[player].defence}
Speed: {players.goodies[player].speed}
""")
			position = input_stuff("""
Select the corresponding number of a position.
>>> """, ["1", "2", "3", "4", "5"])
			players.goodies[player].position = positions[int(position) - 1]

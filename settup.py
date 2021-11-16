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
		print(f"""Set where you want each player to be. There are five positions.
1. {positions[0].title()} (Offensive)
2. {positions[1].title()} (Offensive)
3. {positions[2].title()} (Neutral)
4. {positions[3].title()} (Defensive)
5. {positions[4].title()} (Defensive)""")
		position = input_stuff("""
Select the corresponding number of a position.
>>> """, ["1", "2", "3", "4", "5"])
		players.print_players()
		choice = input(f"""Which player do you want to be on for {positions[int(position) - 1]}?
>>> """)
		players.goodies[keys[int(choice) - 1]]['position'] = positions[int(position) - 1]
		positions[int(position) - 1] += ": " + players.goodies[keys[int(choice) - 1]]['firstname'] + " " + players.goodies[keys[int(choice) - 1]]['lastname'] + ""


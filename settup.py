from utils import print_stuff
from utils import clear
from utils import input_stuff
import players

def set_positions():
	positions = ["point guard", "small forward", "center", "power forward", "shooting guard"]
	while True:
		clear()
		print(f"""Set where you want each player to be. There are five positions.
1. {positions[0].capitalize()} (Offensive)
2. {positions[1].capitalize()} (Offensive)
3. {positions[2].capitalize()} (Neutral)
4. {positions[3].capitalize()} (Defensive)
5. {positions[4].capitalize()} (Defensive)""")
		position = input_stuff("""
Select the corresponding number of a position.
>>> """, ["1", "2", "3", "4", "5"])
		players.print_players()
		choice = input(f"""Which player do you want to be on for {positions[int(position) - 1]}?
>>> """)


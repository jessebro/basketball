from utils import print_stuff
from utils import clear
import players

def set_positions():
	clear()
	positions = ["Point Guard", "Small Forward", "Center", "Power Forward", "Shooting Guard"]
	print("""Set where you want each player to be. There are five positions.
1. Point Guard (Offensive)
2. Small Forward (Offensive)
3. Center (Neutral)
4. Power Forward (Defensive)
5. Shooting Guard (Defensive)""")
	position = input("""
Select the corresponding number of a position.
>>> """)
	players.print_players()
	choice = input()

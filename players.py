from utils import print_stuff
import random
import copy
from utils import clear
from utils import colour_it
from utils import Color

firstnames = ["John", "Carl", "David", "Andrew", "Toby", "Nathan", "Rodrigo", "Shaun", "Michael", "Felix", "Matt", "Ethan"]
lastnames = ["Smith", "Cage", "James", "Hill", "Brown", "Mitchel", "Cole", "Johnson", "Wayne", "Miller", "Gabriel", "Davies", "McDuff"]
offenses1 = [45, 55, 60, 70, 80]
defences1 = [45, 55, 60, 70, 80]
speeds1 = [30, 18, 25, 22, 26]
offenses2 = copy.deepcopy(offenses1)
defences2 = copy.deepcopy(defences1)
speeds2 = copy.deepcopy(speeds1)


players = ["player1", "player2", "player3", "player4", "player5"]
goodies = {}
baddies = {}

def choose(list):
	choice = random.choice(list)
	list.remove(choice)
	return choice


def generate_players():
	for player in players:
		goodies[player] = {
	"firstname": choose(firstnames),
	"lastname": choose(lastnames),
	"offense": choose(offenses1),
	"defence": choose(defences1),
	"speed": choose(speeds1),
	"position": ""
}
		baddies[player] = {
	"firstname": choose(firstnames),
	"lastname": choose(lastnames),
	"offense": choose(offenses2),
	"defence": choose(defences2),
	"speed": choose(speeds2),
	"position": ""
}

def print_players():
	counter = 1
	clear()
	print("Your players are:")
	for player in goodies.keys():
		print(f"""{counter}. {colour_it(goodies[player]['firstname'] + " " + goodies[player]['lastname'], Color.ALLY)}""")
		counter += 1


def view_players():
	while True:
		player_numbers = ["1", "2", "3", "4", "5"]
		print_players()
		choice = input("""
Enter a player's number to view their statics, or enter any key to continue.
>>> """)
		if choice not in player_numbers:
			break
		else:
			clear()
			print_stuff(f"""{colour_it(goodies['player' + choice]['firstname'] + " " + goodies['player' + choice]['lastname'], Color.ALLY)}
Offense: {goodies['player' + choice]['offense']}
Defence: {goodies['player' + choice]['defence']}
Speed: {goodies['player' + choice]['speed']}
""")

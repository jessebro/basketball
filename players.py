from utils import print_stuff
import random
import copy
from utils import clear
from utils import colour_it
from utils import Color
from utils import choose

famous = False

class Player:

	def __init__(self, name="", offense=0, defence=0, speed=0, position="", exhaustion=0):
		self.name = name
		self.offense = offense
		self.defence = defence
		self.speed = speed
		self.position = position
		self.exhaustion = exhaustion


	def pass_ball(self, defender, team, ball_player, ball_distance):
		pass


	def skirt(self, defender, team, ball_player, ball_distance):
		pass

	def shoot(self, defender, team, ball_player, ball_distance):
		shot = random.randrange(1, 50 + (45 - ball_distance))
		score = 0
		if ball_distance >= 40:
			print_stuff(f"""{colour_it(self.name, Color.ALLY)} slams the ball through the hoop in a dunk!""")
			return 2
		elif ball_distance <= 23:
			print_stuff(f"""{colour_it(self.name, Color.ALLY)} takes a shot for a 3 pointer!""")
			score = 3
		elif ball_distance <= 18:
			print_stuff(f"""{colour_it(self.name, Color.ALLY)} takes a shot for a 2 pointer!""")
			score = 2
		else:
			print_stuff(f"""{colour_it(self.name, Color.ALLY)} takes a shot!""")
		if shot <= self.offense:
			print_stuff(f"""Swish! Through the hoop!""")
			return score
		else:
			print_stuff("A miss! Unlucky.")
			return 0


firstnames = ["John", "Carl", "David", "Andrew", "Toby", "Nathan", "Rodrigo", "Shaun", "Michael", "Felix", "Matt", "Ethan"]
lastnames = ["Smith", "Cage", "James", "Hill", "Brown", "Mitchel", "Cole", "Johnson", "Wayne", "Miller", "Gabriel", "Davies", "McDuff"]
famous_names = ["Jesus Christ", "Jeff Bezos", "Mohammed Ali", "Derrin Brown", "Obama bin Laden", "Kanye West", "Mr Beast", "Snoop Dogg", "Neil Armstrong", "Spiderman", "Saddam Hussein", "Boe Jiden", "Bill Gates", "Bruce Lee", "Mahatma Gandhi", "Sugar Daddy Craig", "Renegade Raider", "Steve Jobs", "Mike Kachowski"]
offenses1 = [45, 55, 60, 70, 80]
defences1 = [45, 55, 60, 70, 80]
speeds1 = [11, 13, 16, 21, 25]
offenses2 = copy.deepcopy(offenses1)
defences2 = copy.deepcopy(defences1)
speeds2 = copy.deepcopy(speeds1)

player_no = 0

players = ["player1", "player2", "player3", "player4", "player5"]
goodies = {}
baddies = {}


def generate_players():
	removed_players = list(players[player_no:])
	for player in removed_players:
		players.remove(player)
	for player in players:
		if not famous:
			goody_name = choose(firstnames) + " " + choose(lastnames)
			baddy_name = choose(firstnames) + " " + choose(lastnames)
		else:
			goody_name = choose(famous_names)
			baddy_name = choose(famous_names)
		goodies[player] = Player(goody_name, choose(offenses1), choose(defences1), choose(speeds1))
		baddies[player] = Player(baddy_name, choose(offenses2), choose(defences2), choose(speeds2))


def print_players():
	counter = 1
	clear()
	print("Your players are:")
	for player in goodies.keys():
		print(f"""{counter}. {colour_it(goodies[player].name, Color.ALLY)}""")
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
			print_stuff(f"""{colour_it(goodies['player' + choice].name, Color.ALLY)}
Offense: {goodies['player' + choice].offense}
Defence: {goodies['player' + choice].defence}
Speed: {goodies['player' + choice].speed}
""")

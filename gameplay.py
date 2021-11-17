import players
import random
from utils import print_stuff
from utils import input_stuff
from utils import colour_it
from utils import Color

team = {
	"point guard": None,
	"small forward": None,
	"center": None,
	"power forward": None,
	"shooting guard": None,
}

enemy = {
	"point guard": None,
	"small forward": None,
	"center": None,
	"power forward": None,
	"shooting guard": None,
}
positions = ["point guard", "small forward", "center", "power forward", "shooting guard"]

game_state = {
	"ball_position": 0,
	"player_score": 0,
	"enemy_score": 0,
}


def init():
	global game_state
	game_state = {
		"ball_position": 0,  # Increases when taken towards enemy hoop. Decreases when taken towards player's hoop.
		"player_score": 0,
		"enemy_score": 0,
		"possestion": False  # True if the player has it, False if the enemy has it.
	}
	for player in list(players.goodies.keys()):
		team[players.goodies[player].position] = players.goodies[player]
	for player in list(players.baddies.keys()):
		enemy[players.baddies[player].position] = players.baddies[player]


def jump_ball():
	print_stuff("""The jump ball is thrown. The center player from each team contests to reach it.""")
	player_roll = random.randrange(1, team['center'].offense)
	enemy_roll = random.randrange(1, enemy['center'].offense)
	if player_roll >= enemy_roll:
		print_stuff(f"{colour_it(team['center'].name, Color.ALLY)} takes the ball!")
		game_state['possession'] = True
	else:
		print_stuff(f"{colour_it(enemy['center'].name, Color.ENEMY)} takes the ball!")
		game_state['possession'] = False

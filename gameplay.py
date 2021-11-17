import players
import random
from utils import print_stuff
from utils import input_stuff
from utils import colour_it
from utils import Color

sguard = players.Player()
pguard = players.Player()
center = players.Player()
sforward = players.Player()
pforword = players.Player()
epguard = players.Player()
esforward = players.Player()
ecenter = players.Player()
epforword = players.Player()
esguard = players.Player()
team = [pguard, sforward, center, pforword, sguard]
enemy = [epguard, esforward, ecenter, epforword, esguard]
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
		idx = positions.index(players.goodies[player].position)
		team[idx] = players.goodies[player]
	for player in list(players.baddies.keys()):
		idx = positions.index(players.baddies[player].position)
		enemy[idx] = players.baddies[player]


def jump_ball():
	print_stuff("""The jump ball is thrown. The center player from each team contests to reach it.""")
	player_roll = random.randrange(1, center.offense)
	enemy_roll = random.randrange(1, ecenter.offense)
	if player_roll >= enemy_roll:
		print_stuff(f"{colour_it(center.name, Color.ALLY)} takes the ball!")
		game_state['possession'] = True
	else:
		print_stuff(f"{colour_it(ecenter.name, Color.ENEMY)} takes the ball!")
		game_state['possession'] = False

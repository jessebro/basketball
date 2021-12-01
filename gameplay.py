import players
import random
from utils import print_stuff
from utils import input_stuff
from utils import colour_it
from utils import Color

team = {
	"point guard": players.Player(),
	"small forward": players.Player(),
	"center": players.Player(),
	"power forward": players.Player(),
	"shooting guard": players.Player(),
}

enemy = {
	"point guard": players.Player(),
	"small forward": players.Player(),
	"center": players.Player(),
	"power forward": players.Player(),
	"shooting guard": players.Player(),
}

positions = ["point guard", "small forward", "center", "power forward", "shooting guard"]

game_state = {
	"ball_position": 0,
	"player_score": 0,
	"enemy_score": 0,
}

ball_player = None

def init():
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
	global ball_player
	print_stuff("""The jump ball is thrown. The center player from each team contests to reach it.""")
	player_roll = random.randrange(1, team['center'].offense)
	enemy_roll = random.randrange(1, enemy['center'].offense)
	if player_roll >= enemy_roll:
		print_stuff(f"{colour_it(team['center'].name, Color.ALLY)} takes the ball!")
		game_state['possession'] = True
		ball_player = team['center']
	else:
		print_stuff(f"{colour_it(enemy['center'].name, Color.ENEMY)} takes the ball!")
		game_state['possession'] = False
		ball_player = enemy['center']


def game_flow():
	while True:
		if game_state['possession']:
			player_turn()
		else:
			enemy_turn()


def player_turn():
	global ball_player
	game_state['ball_position'] += ball_player.speed
	actions = [ball_player.pass_ball, ball_player.skirt, ball_player.shoot]
	defender = enemy[random.choice(list(enemy.keys()))]
	print(f"""{colour_it(ball_player.name, Color.ALLY)} takes the ball {ball_player.speed} feet towards the enemy hoop.
They are intercepted by {colour_it(defender.name, Color.ENEMY)}""")
	if game_state['ball_position'] >= 0:
		action = input_stuff("""Do they...
1. Pass.
2. Skirt.
3. Shoot.`
>>> """, ["1", "2", "3"])
	else:
		action = input_stuff("""Do they...
1. Pass.
2. Skirt.
>>> """, ["1", "2"])
	effect = actions[int(action) - 1](defender, team, ball_player, game_state["ball_position"])
	if isinstance(effect, str):
		ball_player = team[effect]
	if action == "3":
		game_state['player_score'] += effect


def enemy_turn():
	pass


def enemy_pass():
	pass


def enemy_skirt():
	pass


def enemy_shoot():
	pass

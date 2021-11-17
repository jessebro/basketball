import players
import settup
import gameplay

players.generate_players()
players.view_players()
settup.set_positions()
settup.enemy_setup()
gameplay.init()


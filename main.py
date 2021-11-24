import players
import settup
import gameplay

players.famous = input("""Do you want to play with famous people? (y/n)
>>> """) == "y"
players.generate_players()
players.view_players()
settup.set_positions()
settup.enemy_setup()
gameplay.init()
gameplay.jump_ball()
gameplay.game_flow()

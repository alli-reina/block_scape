from ursina import *
from block_game import BlockGame

app = Ursina()

block_game = BlockGame()
block_game.setup()

def input(key):
    block_game.handle_input(key)

app.run()

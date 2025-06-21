from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from block import Block
from inventory import Inventory


class BlockGame:
    def __init__(self):
        self.terrain_blocks = []
        self.inventory = Inventory()

    def setup(self):
        self.player_controller = FirstPersonController()
        self.sky = Sky()

        for row in range(-10, 10):
            for col in range(-10, 10):
                block = Block(position=(col, 0, row), block_type='grass')
                self.terrain_blocks.append(block)

    def handle_input(self, key):
        # Switch inventory slot for all 7 blocks
        if key in ['1', '2', '3', '4', '5', '6', '7']:
            self.inventory.select_slot(int(key) - 1)

        if key in ('q', 'escape'):
            application.quit()

        for block in self.terrain_blocks:
            if block.hovered:
                if key == 'left mouse down' and self.inventory.has_block():
                    block_type = self.inventory.get_selected_block_type()
                    new_block = Block(position=block.position + mouse.normal, block_type=block_type)
                    self.terrain_blocks.append(new_block)
                    self.inventory.use_block()

                elif key == 'right mouse down':
                    invoke(self.destroy_block, block, delay=0.2)

    def destroy_block(self, block):
        if block in self.terrain_blocks:
            self.terrain_blocks.remove(block)
            destroy(block)
            self.inventory.add_block('dirt')


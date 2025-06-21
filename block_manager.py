from ursina import *

class BlockManager:
    def __init__(self, texture='dirt.png'):
        self.selected_texture = texture
        self.block_list = []

    def create_ground(self, width=20, depth=20):
        for row_index in range(depth):
            for column_index in range(width):
                block = Button(
                    color=color.white,
                    model='cube',
                    position=(column_index, 0, row_index),
                    texture=self.selected_texture,
                    parent=scene,
                    origin_y=0.5
                )
                self.block_list.append(block)

    def handle_input(self, input_key):
        if input_key == 'left mouse down':
            for block in self.block_list:
                if block.hovered:
                    new_block = Button(
                        color=color.white,
                        model='cube',
                        position=block.position + mouse.normal,
                        texture=self.selected_texture,
                        parent=scene,
                        origin_y=0.5
                    )
                    self.block_list.append(new_block)
                    break

        elif input_key == 'right mouse down':
            for block in self.block_list:
                if block.hovered:
                    self.block_list.remove(block)
                    destroy(block)
                    break

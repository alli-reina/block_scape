from ursina import *


class Block(Button):
    def __init__(self, position, block_type='dirt'):
        super().__init__(
            color=color.white,
            model='cube',
            position=position,
            texture=f'{block_type}.png',
            parent=scene,
            origin_y=0.5
        )

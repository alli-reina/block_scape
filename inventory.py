from ursina import *


class Inventory:
    def __init__(self):
        self.slots = ['dirt', 'stone', 'grass']
        self.selected_index = 0
        self.ui_borders = []
        self.ui_boxes = []
        self.ui_icons = []

        self.create_ui()

    def create_ui(self):
        # Layout settings
        slot_width = 0.12
        slot_spacing = 0.03
        total_hotbar_width = len(self.slots) * (slot_width + slot_spacing)
        start_position_x = -total_hotbar_width / 2 + (slot_width / 2)

        for slot_index, block_type in enumerate(self.slots):
            slot_position_x = start_position_x + slot_index * (slot_width + slot_spacing)

            # Square border behind the box
            border_entity = Entity(
                parent=camera.ui,
                model='quad',
                color=color.black,
                scale=(slot_width + 0.01, 0.13),
                position=(slot_position_x, -0.45, 0.01)
            )

            # Square inventory slot
            box_entity = Entity(
                parent=camera.ui,
                model='quad',
                color=color.gray,
                scale=(slot_width, 0.11),
                position=(slot_position_x, -0.45, 0)
            )

            # Block icon inside the box
            icon_entity = Entity(
                parent=box_entity,
                model='quad',
                texture=f'{block_type}.png',
                scale=(1, 1),
                position=(0, 0.015, -0.01)
            )

            self.ui_borders.append(border_entity)
            self.ui_boxes.append(box_entity)
            self.ui_icons.append(icon_entity)

        self.highlight_selected()

    def highlight_selected(self):
        for border_index, border_entity in enumerate(self.ui_borders):
            border_entity.color = color.yellow if border_index == self.selected_index else color.black

    def select_slot(self, slot_index):
        if 0 <= slot_index < len(self.slots):
            self.selected_index = slot_index
            self.highlight_selected()

    def get_selected_block_type(self):
        return self.slots[self.selected_index]

    def has_block(self):
        return True  # unlimited mode

    def use_block(self):
        pass

    def add_block(self, block_type):
        pass

    def update_ui(self):
        pass


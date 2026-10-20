from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialize the Ursina app
app = Ursina()

# Use built-in system colors
block_colors = [color.lime, color.gray, color.brown, color.white]
current_color_index = 0

def update():
    global current_color_index
    if held_keys['1']: current_color_index = 0  # Lime
    if held_keys['2']: current_color_index = 1  # Gray
    if held_keys['3']: current_color_index = 2  # Brown
    if held_keys['4']: current_color_index = 3  # White

class Voxel(Button):
    def __init__(self, position = (0,0,0), b_color = color.lime):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube', 
            color = b_color,        # Uses the direct color object passed in
            scale = 1
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position = self.position + mouse.normal, b_color = block_colors[current_color_index])
            if key == 'right mouse down':
                destroy(self)

# Generate a basic flat 15x15 terrain grid
for z in range(15):
    for x in range(15):
        Voxel(position = (x, 0, z), b_color = color.lime)

# Add player controller
player = FirstPersonController()

# Run the game loop
app.run()


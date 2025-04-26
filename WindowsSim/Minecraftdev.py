import pygame
import numpy as np
import random
import json
import os

# Define block size and world dimensions
BLOCK_SIZE = 50
WORLD_WIDTH = 12  # Number of blocks horizontally
WORLD_HEIGHT = 10  # Number of blocks vertically

# Define colors for different blocks and inventory
GRASS_COLOR = (34, 139, 34)  # Green for grass
STONE_COLOR = (169, 169, 169)  # Gray for stone (tuff)
PLAYER_COLOR = (0, 0, 255)  # Blue for player
INVENTORY_COLOR = (255, 215, 0)  # Yellow for inventory items

# Inventory dictionary to hold collected blocks
inventory = {"grass": 0, "stone": 0}

# Create a simple 2D world represented by a grid of blocks
def generate_world():
    world = np.zeros((WORLD_HEIGHT, WORLD_WIDTH), dtype=int)
    for row in range(WORLD_HEIGHT):
        for col in range(WORLD_WIDTH):
            if row > WORLD_HEIGHT // 2:
                world[row, col] = random.choice([0, 1])  # 0: Grass, 1: Stone (Tuff)
            else:
                world[row, col] = 0  # Grass at the top
    return world

world = generate_world()

# Player position (row, col)
player_pos = [1, 1]  # Start at (1, 1)

# Movement speed for the player
move_speed = 1

# Draw the world (blocks) and player
def draw_world(screen):
    for row in range(world.shape[0]):
        for col in range(world.shape[1]):
            block_type = world[row, col]
            if block_type == 0:
                block_color = GRASS_COLOR
            else:
                block_color = STONE_COLOR
            pygame.draw.rect(screen, block_color, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Draw player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[1] * BLOCK_SIZE, player_pos[0] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Inventory display at the top left corner
def draw_inventory(screen):
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Grass: {inventory['grass']} Stone: {inventory['stone']}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

# Save the world state to a JSON file
def save_world(filename="world.json"):
    world_data = world.tolist()  # Convert numpy array to list for JSON compatibility
    with open(filename, "w") as f:
        json.dump(world_data, f)

# Load the world state from a JSON file
def load_world(filename="world.json"):
    global world
    if os.path.exists(filename):
        with open(filename, "r") as f:
            world_data = json.load(f)
            world = np.array(world_data)
    else:
        print("No save file found. Loading default world.")

# Player interaction: Mining and placing blocks
def interact():
    row, col = player_pos
    if world[row, col] == 1:  # Stone block (Tuff)
        world[row, col] = 0  # "Mine" it by turning it into grass
        inventory['stone'] += 1  # Add stone to inventory
    elif world[row, col] == 0:  # Grass block
        world[row, col] = 1  # Place a stone block (tuff) here
        inventory['grass'] += 1  # Add grass to inventory

# Game loop
def game_loop():
    pygame.init()
    
    # Create the screen with the size 600x800 pixels
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Minecraft DEV")

    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((0, 0, 0))  # Fill screen with black

        # Draw the world and inventory
        draw_world(screen)
        draw_inventory(screen)

        # Event handling (for player movement, interaction, menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player_pos[0] > 0:  # Move up
                    player_pos[0] -= move_speed
                if event.key == pygame.K_s and player_pos[0] < WORLD_HEIGHT - 1:  # Move down
                    player_pos[0] += move_speed
                if event.key == pygame.K_a and player_pos[1] > 0:  # Move left
                    player_pos[1] -= move_speed
                if event.key == pygame.K_d and player_pos[1] < WORLD_WIDTH - 1:  # Move right
                    player_pos[1] += move_speed
                if event.key == pygame.K_e:  # Interact (mine or place)
                    interact()
                if event.key == pygame.K_ESCAPE:  # Quit the game
                    running = False
                if event.key == pygame.K_F5:  # Save world to file
                    save_world("world.json")
                if event.key == pygame.K_F9:  # Load world from file
                    load_world("world.json")

        # Update the display
        pygame.display.flip()

        # Set frame rate
        clock.tick(10)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()

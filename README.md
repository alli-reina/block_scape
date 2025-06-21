# Minecraft-Inspired Game with Ursina

This is a Minecraft-like sandbox block-building game developed using the [Ursina Engine](https://www.ursinaengine.org/). The project is structured in an object-oriented way, split into modules for blocks, inventory, and game logic.

## 🔗 Source and Inspiration
This project is based on and extended from:  
**[Original Source by beaucarnes](https://github.com/beaucarnes/zizyo/tree/master/minecraft)**

All core features are restructured using OOP practices, and the following enhancements have been added:

## 🚀 Features
- WASD movement, jump (space)
- Left click to destroy blocks
- Right click to place blocks
- 7-slot inventory UI with selectable blocks
- New blocks added: `dirt`, `stone`, `grass`, `brick`, `mossy_stone`, `leaves`, `wood`
- Visually styled inventory boxes
- Modular and maintainable code structure

## 📁 Folder Structure
minecraft/
│
├── assets/ # Contains all block textures (PNG files)
├── block.py # Block class definition
├── block_game.py # Main game logic and input handling
├── inventory.py # Inventory UI and management
├── main.py # Entry point to run the game
└── README.md # You're reading this


## 🛠 Requirements
- Python 3.7+
- Ursina Engine  
  Install via: `pip install ursina`

## ▶️ How to Run
Place all PNG textures inside the `assets/` folder.


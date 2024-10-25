# moya Documentation

## Overview
This game engine is built on the Ursina library and provides an easy-to-use API for creating 3D games. The engine allows you to create entities, add physics, control lighting and camera, and manage scenes.

## Prerequisites
```python
pip install ursina
```

## Key Features
1. Entity creation and management
2. Lighting system
3. Camera control
4. Basic physics system
5. Scene management
6. Scene save and load functionality

## Usage

### 1. Initialize the Engine
```python
from ursina import *
engine = GameEngine()
```

### 2. Create a Scene
```python
scene = engine.create_scene("main_scene")
```

### 3. Create Entities
```python
# Create a cube
cube = engine.create_entity(
    model_type='cube',
    position=(0,0,0),
    scale=(1,1,1),
    color=color.white
)

# Add lighting
light = engine.create_light(
    position=(2,3,2),
    color=color.white,
    intensity=1
)

# Create a first-person controller
player = engine.create_fps_controller(position=(0,2,0))
```

### 4. Add Physics
```python
engine.add_physics(cube)
```

### 5. Scene Management
```python
# Add entities to the scene
engine.add_to_scene("main_scene", cube)
engine.add_to_scene("main_scene", light)
engine.add_to_scene("main_scene", player)

# Load a scene
engine.load_scene("main_scene")
```

### 6. Save and Load Scenes
```python
# Save the scene
engine.save_scene_to_file("scene.json")

# Load the scene
engine.load_scene_from_file("scene.json")
```

### 7. Run the Engine
```python
engine.run()
```

## Full Example
```python
engine = GameEngine()

# Create a new scene
scene = engine.create_scene("main")

# Create entities
cube = engine.create_entity('cube', position=(0,0,0))
light = engine.create_light(position=(2,3,2))
player = engine.create_fps_controller(position=(0,2,0))

# Add physics to the cube
engine.add_physics(cube)

# Add entities to the scene
engine.add_to_scene("main", cube)
engine.add_to_scene("main", light)
engine.add_to_scene("main", player)

# Run the engine
engine.run()
```

## Key Functions

### `create_entity()`
Used to create game entities
- model_type: model type ('cube', 'sphere', etc.)
- position: position (x,y,z)
- scale: scale (x,y,z)
- color: color
- texture: texture (optional)

### `create_light()`
Creates a light source
- position: light position
- color: light color
- intensity: light intensity

### `create_camera()`
Creates a camera
- position: camera position
- rotation: camera rotation

### `create_fps_controller()`
Creates a first-person perspective controller
- position: initial player position

### `add_physics()`
Adds physics to an entity

### `save_scene_to_file()` and `load_scene_from_file()`
Save and load scenes to/from a file

## Important Notes
1. The engine must be initialized before creating any entities.
2. Ensure entities are added to the scene after being created.
3. Add physics to entities as needed.
4. Use `run()` at the end of the program to start the engine.

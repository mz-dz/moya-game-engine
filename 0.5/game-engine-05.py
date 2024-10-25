from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import json

class GameEngine:
    def __init__(self):
        self.app = None
        self.entities = []
        self.scenes = {}
        self.current_scene = None
        self.init_engine()

    def init_engine(self):
        """Initialize the Ursina engine"""
        self.app = Ursina()
        
    def create_entity(self, model_type, position=(0,0,0), scale=(1,1,1), color=color.white, texture=None):
        """Create a new entity"""
        entity = Entity(
            model=model_type,
            position=position,
            scale=scale,
            color=color,
            texture=texture
        )
        self.entities.append(entity)
        return entity

    def create_light(self, position=(0,0,0), color=color.white, intensity=1):
        """Create a point light"""
        light = PointLight(
            position=position,
            color=color,
            intensity=intensity
        )
        self.entities.append(light)
        return light

    def create_camera(self, position=(0,0,0), rotation=(0,0,0)):
        """Create a camera"""
        camera = EditorCamera(
            position=position,
            rotation=rotation
        )
        self.entities.append(camera)
        return camera

    def create_fps_controller(self, position=(0,0,0)):
        """Create a first person controller"""
        player = FirstPersonController(
            position=position
        )
        self.entities.append(player)
        return player

    def add_physics(self, entity):
        """Add physics to an entity"""
        if not hasattr(entity, 'rigidbody'):
            entity.add_script(RigidBody())

    def remove_physics(self, entity):
        """Remove physics from an entity"""
        if hasattr(entity, 'rigidbody'):
            entity.remove_script('rigidbody')

class AdvancedPhysics:
    def __init__(self):
        self.gravity = -9.81
        self.collision_systems = []
    
    def add_ragdoll(self, entity):
        # نظام للتحكم في الجسم عند السقوط أو الموت
        pass
        
    def add_joint_constraints(self, entity1, entity2, joint_type):
        # ربط الكائنات مع بعضها
        pass
        
    def add_soft_body(self, entity):
        # فيزياء للأجسام المرنة مثل القماش والسوائل
        pass
        
        
        
        
    def set_parent(self, entity, parent):
        """Set parent for an entity"""
        entity.parent = parent

    def create_scene(self, name):
        """Create a new scene"""
        self.scenes[name] = []
        self.current_scene = name
        return self.scenes[name]

    def add_to_scene(self, scene_name, entity):
        """Add entity to a scene"""
        if scene_name in self.scenes:
            self.scenes[scene_name].append(entity)

    def load_scene(self, scene_name):
        """Load a scene"""
        if scene_name in self.scenes:
            # Clear current entities
            for entity in self.entities:
                destroy(entity)
            self.entities.clear()
            
            # Load scene entities
            self.entities = self.scenes[scene_name]
            self.current_scene = scene_name

    def save_scene_to_file(self, filename):
        """Save current scene to file"""
        scene_data = []
        for entity in self.entities:
            entity_data = self._get_entity_state(entity)
            scene_data.append(entity_data)
        
        with open(filename, 'w') as f:
            json.dump(scene_data, f)

    def load_scene_from_file(self, filename):
        """Load scene from file"""
        with open(filename, 'r') as f:
            scene_data = json.load(f)
        
        # Clear existing entities
        for entity in self.entities:
            destroy(entity)
        self.entities.clear()
        
        # Create new entities from loaded data
        for entity_data in scene_data:
            entity = self._create_entity_from_state(entity_data)
            self.entities.append(entity)

    def _get_entity_state(self, entity):
        """Get entity state for saving"""
        return {
            'model': entity.model.name if hasattr(entity, 'model') else type(entity).__name__,
            'position': entity.position,
            'scale': entity.scale,
            'color': entity.color.hex,
            'texture': str(entity.texture) if hasattr(entity, 'texture') else None,
            'parent': entity.parent.name if entity.parent and entity.parent != scene else None,
            'has_physics': hasattr(entity, 'rigidbody')
        }

    def _create_entity_from_state(self, state):
        """Create entity from saved state"""
        if state['model'] in ['PointLight', 'EditorCamera', 'FirstPersonController']:
            if state['model'] == 'PointLight':
                entity = PointLight()
            elif state['model'] == 'EditorCamera':
                entity = EditorCamera()
            else:
                entity = FirstPersonController()
        else:
            entity = Entity(model=state['model'])
        
        entity.position = state['position']
        entity.scale = state['scale']
        entity.color = color.hex(state['color'])
        if state['texture'] and state['texture'] != 'None':
            entity.texture = state['texture']
        if state['has_physics']:
            entity.add_script(RigidBody())
        return entity

    def run(self):
        """Run the game engine"""
        self.app.run()


class AdvancedGraphics:
    def __init__(self):
        self.shaders = {}
        
    def add_dynamic_shadows(self):
        # إضافة ظلال ديناميكية
        pass
        
    def add_particle_system(self):
        # نظام الجزيئات للدخان والنار والانفجارات
        pass
        
    def add_post_processing(self):
        # تأثيرات ما بعد المعالجة
        pass
# Example usage:
if __name__ == "__main__":
    engine = GameEngine()
    
    # Create a scene
    scene1 = engine.create_scene("main")
    
    # Create entities
    cube = engine.create_entity(
    model_type='cube',
    position=(0,0,0),
    scale=(1,1,1),
    color=color.white 
    )
    light = engine.create_light(
    position=(2,3,2),
    color=color.white,
    intensity=1
    )
    player = engine.create_fps_controller(position=(0,2,0))
    
    # Add physics to cube
    engine.add_physics(cube)
    
    # Add entities to scene
    engine.add_to_scene("main", cube)
    engine.add_to_scene("main", light)
    engine.add_to_scene("main", player)
    
    
    # Run the engine
    engine.run()
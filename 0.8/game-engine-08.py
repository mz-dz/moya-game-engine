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

class AudioSystem:
    def __init__(self):
        self.audio_sources = {}
        self.background_music = None
        
    def load_sound(self, name, path):
        """تحميل ملف صوتي"""
        self.audio_sources[name] = Audio(path, loop=False, autoplay=False)
        
    def play_sound(self, name):
        """تشغيل صوت"""
        if name in self.audio_sources:
            self.audio_sources[name].play()
            
    def play_background_music(self, path):
        """تشغيل موسيقى الخلفية"""
        if self.background_music:
            self.background_music.stop()
        self.background_music = Audio(path, loop=True, autoplay=True)
        
    def stop_all_sounds(self):
        """إيقاف جميع الأصوات"""
        for source in self.audio_sources.values():
            source.stop()
        if self.background_music:
            self.background_music.stop()

class AISystem:
    def __init__(self):
        self.agents = []
        self.navigation_mesh = None
        
    def create_agent(self, entity, behavior_type):
        """إنشاء عميل ذكاء اصطناعي"""
        agent = {
            'entity': entity,
            'behavior': behavior_type,
            'target': None,
            'state': 'idle'
        }
        self.agents.append(agent)
        return agent
        
    def set_target(self, agent, target):
        """تعيين هدف للعميل"""
        agent['target'] = target
        
    def update_agents(self):
        """تحديث سلوك العملاء"""
        for agent in self.agents:
            if agent['behavior'] == 'follow':
                self._update_follow_behavior(agent)
            elif agent['behavior'] == 'patrol':
                self._update_patrol_behavior(agent)
    
    def _update_follow_behavior(self, agent):
        if agent['target']:
            direction = agent['target'].position - agent['entity'].position
            if direction.length() > 0.5:
                agent['entity'].position += direction.normalized() * time.dt
                
    def _update_patrol_behavior(self, agent):
        # تنفيذ سلوك الدورية
        pass

class ResourceManager:
    def __init__(self):
        self.models = {}
        self.textures = {}
        self.animations = {}
        
    def load_model(self, name, path):
        """تحميل نموذج ثلاثي الأبعاد"""
        self.models[name] = load_model(path)
        
    def load_texture(self, name, path):
        """تحميل قوام"""
        self.textures[name] = load_texture(path)
        
    def load_animation(self, name, path):
        """تحميل حركة"""
        self.animations[name] = load_animation(path)
        
    def get_model(self, name):
        return self.models.get(name)
        
    def get_texture(self, name):
        return self.textures.get(name)
        
    def get_animation(self, name):
        return self.animations.get(name)

# تحديث فئة GameEngine لتضمين الأنظمة الجديدة
class GameEngine:
    def __init__(self):
        self.app = None
        self.entities = []
        self.scenes = {}
        self.current_scene = None
        self.audio_system = AudioSystem()
        self.ai_system = AISystem()
        self.resource_manager = ResourceManager()
        self.physics_system = AdvancedPhysics()
        self.graphics_system = AdvancedGraphics()
        self.init_engine()

    # ... (باقي الأساليب كما هي)

    def update(self):
        """تحديث حالة المحرك"""
        self.ai_system.update_agents()

class LightSystem:
    def __init__(self):
        self.lights = []
        self.default_settings = {
            'intensity': 1.0,
            'shadow_resolution': 2048,
            'shadow_map_size': 4096,
            'color_temperature': 6500  # Kelvin
        }

    def create_point_light(self, position=(0,0,0), color=color.white, **kwargs):
        """إنشاء إضاءة نقطية مع خصائص متقدمة"""
        light = PointLight(
            position=position,
            color=color,
            intensity=kwargs.get('intensity', 1.0),
            radius=kwargs.get('radius', 10),
            shadows=kwargs.get('shadows', True),
            shadow_map_resolution=kwargs.get('shadow_resolution', 2048),
            volumetric=kwargs.get('volumetric', False),
            far_z_atten=kwargs.get('far_z_atten', 100),
            shadow_filter_size=kwargs.get('shadow_filter_size', 1.0)
        )
        self.lights.append(light)
        return light

    def create_spotlight(self, position=(0,0,0), color=color.white, **kwargs):
        """إنشاء إضاءة موجهة مع خصائص متقدمة"""
        light = SpotLight(
            position=position,
            color=color,
            intensity=kwargs.get('intensity', 1.0),
            fov=kwargs.get('fov', 45),
            range=kwargs.get('range', 20),
            shadows=kwargs.get('shadows', True),
            shadow_map_resolution=kwargs.get('shadow_resolution', 2048),
            volumetric=kwargs.get('volumetric', False),
            far_z_atten=kwargs.get('far_z_atten', 100),
            shadow_filter_size=kwargs.get('shadow_filter_size', 1.0)
        )
        self.lights.append(light)
        return light

    def create_directional_light(self, rotation=(45,-45,0), color=color.white, **kwargs):
        """إنشاء إضاءة اتجاهية مع خصائص متقدمة"""
        light = DirectionalLight(
            rotation=rotation,
            color=color,
            intensity=kwargs.get('intensity', 1.0),
            shadows=kwargs.get('shadows', True),
            shadow_map_resolution=kwargs.get('shadow_resolution', 4096),
            shadow_filter_size=kwargs.get('shadow_filter_size', 1.0)
        )
        self.lights.append(light)
        return light

    def create_ambient_light(self, color=color.rgb(0.1, 0.1, 0.1), **kwargs):
        """إنشاء إضاءة محيطية"""
        light = AmbientLight(
            color=color,
            intensity=kwargs.get('intensity', 0.1)
        )
        self.lights.append(light)
        return light

# تحديث فئة GameEngine لتضمين نظام الإضاءة الجديد
class GameEngine:
    def __init__(self):
        self.app = None
        self.entities = []
        self.scenes = {}
        self.current_scene = None
        self.light_system = LightSystem()
        self.init_engine()

    def create_advanced_light(self, light_type='point', **kwargs):
        """واجهة موحدة لإنشاء الإضاءة"""
        if light_type == 'point':
            return self.light_system.create_point_light(**kwargs)
        elif light_type == 'spot':
            return self.light_system.create_spotlight(**kwargs)
        elif light_type == 'directional':
            return self.light_system.create_directional_light(**kwargs)
        elif light_type == 'ambient':
            return self.light_system.create_ambient_light(**kwargs)


# مثال على الاستخدام:
if __name__ == "__main__":
    engine = GameEngine()
    
    # إنشاء مشهد
    scene1 = engine.create_scene("main")
    
    # إضافة إضاءة نقطية متقدمة
    point_light = engine.create_advanced_light(
        light_type='point',
        position=(2,3,2),
        color=color.rgb(1, 0.9, 0.8),  # لون دافئ
        intensity=1.5,
        radius=15,
        shadows=True,
        shadow_resolution=2048,
        shadow_filter_size=2.0,
        far_z_atten=150,
        volumetric=True
    )
    
    # إضافة إضاءة موجهة
    spot_light = engine.create_advanced_light(
        light_type='spot',
        position=(0,5,0),
        color=color.rgb(0.9, 0.9, 1),  # لون بارد
        intensity=2.0,
        fov=35,
        range=25,
        shadows=True,
        shadow_resolution=4096,
        shadow_filter_size=1.5
    )
    
    # إضافة إضاءة اتجاهية (مثل الشمس)
    sun_light = engine.create_advanced_light(
        light_type='directional',
        rotation=(45,-45,0),
        color=color.rgb(1, 1, 0.9),
        intensity=1.0,
        shadow_resolution=8192,
        shadow_filter_size=3.0
    )
    
    # إضافة إضاءة محيطية
    ambient_light = engine.create_advanced_light(
        light_type='ambient',
        color=color.rgb(0.1, 0.1, 0.15),
        intensity=0.2
    )
    
    # إنشاء بعض الكائنات للاختبار
    ground = engine.create_entity(
        model_type='plane',
        scale=(20,1,20),
        color=color.gray
    )
    
    cube = engine.create_entity(
        model_type='cube',
        position=(0,1,0),
        scale=(1,1,1),
        color=color.white
    )
    
    player = engine.create_fps_controller(position=(0,2,0))
    
    # إضافة الكائنات إلى المشهد
    for entity in [ground, cube, player]:
        engine.add_to_scene("main", entity)
    
    # تشغيل المحرك
    engine.run()
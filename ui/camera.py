
import bpy
from .. import config
from .base import BittoProperties, setup_ui
from ..utils.registry import regular_registry, property_group_registry


class BittoCameraProperties(BittoProperties):
    pass

BittoCameraProperties.init_annotations(config.camera_props)


class BITTO_PT_camera(bpy.types.Panel):
    bl_label = "Camera"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    COMPAT_ENGINES = {config.engine_name}
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        renderer = context.scene.render
        return renderer.engine == config.engine_name and context.active_object.type == 'CAMERA'

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        camera_props = context.scene.bitto_camera_props
        setup_ui(layout, config.camera_props, camera_props)


def setup():
    regular_registry.add_new_class(BITTO_PT_camera)
    property_group_registry.add_new_property_class(BittoCameraProperties, bpy.types.Camera, "bitto_camera_props")
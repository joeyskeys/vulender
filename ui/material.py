
import bpy
from .. import config
from .base import BittoProperties, setup_ui
from ..utils.registry import regular_registry, property_group_registry


class BITTO_PT_materialslots(bpy.types.Panel):
    bl_label = "Material"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"

    @classmethod
    def poll(cls, context):
        renderer = context.scene.render
        return (context.material or context.object) and renderer.engine == config.engine_name

    def draw(self, context):
        layout = self.layout
        mat = context.material
        slot = context.material_slot
        obj = context.obj
        space = context.space_data


def setup():
    regular_registry.add_new_class(BITTO_PT_materialslots)

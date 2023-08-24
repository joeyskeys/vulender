
import bpy
from .. import config
from .base import BittoProperties, setup_ui
from ..utils.registry import regular_registry, property_group_registry


class BittoAcceleratorProperties(BittoProperties):
    pass

BittoAcceleratorProperties.init_annotations(config.accelerator_props)


class BITTO_PT_accelerator(bpy.types.Panel):
    bl_label = "Accelerator"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    COMPAT_ENGINES = {config.engine_name}
    bl_context = "render"

    @classmethod
    def poll(cls, context):
        renderer = context.scene.render
        return renderer.engine == config.engine_name

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        acc_props = context.scene.bitto_accelerator_props
        setup_ui(layout, config.accelerator_props, acc_props)


def setup():
    regular_registry.add_new_class(BITTO_PT_accelerator)
    property_group_registry.add_new_property_class(BittoAcceleratorProperties, bpy.types.Scene, "bitto_accelerator_props")
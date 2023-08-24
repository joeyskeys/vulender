
import bpy
from .. import config
from .base import BittoProperties, setup_ui
from ..utils.registry import regular_registry, property_group_registry


class BittoSamplerProperties(BittoProperties):
    pass

BittoSamplerProperties.init_annotations(config.sampler_props)


class BITTO_PT_sampler(bpy.types.Panel):
    bl_label = "Sampler"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    COMPAT_ENGINES = {config.engine_name}
    bl_context = "render"

    @classmethod
    def poll(cls, context):
        render = context.scene.render
        return render.engine == config.engine_name

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        sampler_props = context.scene.bitto_sampler_props
        setup_ui(layout, config.sampler_props, sampler_props)


def setup():
    regular_registry.add_new_class(BITTO_PT_sampler)
    property_group_registry.add_new_property_class(BittoSamplerProperties, bpy.types.Scene, "bitto_sampler_props")
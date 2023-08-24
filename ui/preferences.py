
import os
import bpy
from .. import config
from .base import BittoProperties, init_annotations, setup_ui
from ..utils.registry import regular_registry


addon_name = os.path.basename(os.path.dirname(os.path.dirname(__file__)))


class BittoPreferences(bpy.types.AddonPreferences, BittoProperties):
    bl_idname = addon_name

    def draw(self, context):
        layout = self.layout
        setup_ui(layout, config.preference_props, self)

BittoPreferences.init_annotations(config.preference_props)


def get_pref():
    return bpy.context.preferences.addons[addon_name].preferences


def setup():
    regular_registry.add_new_class(BittoPreferences)

import bpy
import mathutils
from .base import BaseIO


class IntegratorIO(BaseIO):
    """
    """

    def __init__(self):
        pass

    def get_props(self):
        return bpy.context.scene.bitto_integrator_props

    def write_description(self, handle):
        pass

    def feed_api(self):
        pass
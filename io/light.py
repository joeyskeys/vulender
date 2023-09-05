
import bpy, mathutils
from .base import BaseIO
from .. import pyvkkk as vk


class LightIO(BaseIO):
    """
    """

    def __init__(self):
        pass

    def get_props(self):
        return object.data.bitto_light_props

    def write_description(self, handle):
        pass

    def feed_api(self, obj, mgr):
        light_type = obj.data.type
        light_color = tuple(obj.data.color)
        light_loc = tuple(obj.location)
        light_dir = mathutils.Vector((0, 0, -1, 0))
        light_dir = tuple(obj.matrix_world @ dir)
        pos = vk.Vec4(*light_loc, 0.0)
        color = vk.Vec4(*light_color, 1.0)
        dir = vk.Vec4(*light_dir)
        
        if light_type == 'POINT':
            mgr.add_pt_light(pos, color)
        elif light_type == 'SUN':
            mgr.add_dir_light(dir, color)
        elif light_type == 'SPOT':
            color = vk.Vec4(pos, dir, vk.Vec3(*light_color))
        else:
            print('Type {} of {} is not supported yet'.format(light_type, obj.name))
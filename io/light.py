
import bpy
from .base import BaseIO


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
        light_loc = obj.location
        
        if light_type == 'POINT':
            pass
        elif light_type == 'DIRECTION':
            pass
        else:
            print('Type {} of {} is not supported yet'.format(light_type, obj.name))
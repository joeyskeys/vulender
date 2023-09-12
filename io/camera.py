
import bpy
import mathutils
import math
from .base import BaseIO
from .. import pyvkkk as vk


class CameraIO(BaseIO):
    """

    """

    def __init__(self):
        pass

    def get_camera_infos(self):
        active_camera = bpy.context.scene.camera
        camera_matrix = active_camera.matrix_world
        eye_pos = camera_matrix.translation
        look_vec = mathutils.Vector((0, 0, -1))
        look_vec.rotate(camera_matrix.to_3x3())
        up_vec = mathutils.Vector((0, 1, 0))
        up_vec.rotate(camera_matrix.to_3x3())
        return eye_pos, look_vec, up_vec

    def get_fov(self):
        return bpy.context.scene.camera.data.angle

    def get_props(self):
        return bpy.context.scene.camera.data.bitto_camera_props

    def write_description(self):
        pass

    def feed_api(self, cam, ratio):
        convert_to_vec3 = lambda v : vk.Vec3(*tuple(v))
        params = map(convert_to_vec3, self.get_camera_infos())
        cam.look_at(*params)

        fov = self.get_fov()
        props = self.get_props()
        near = getattr(props, 'near', 1)
        far = getattr(props, 'far', 1000)
        cam.perspective(fov, ratio, near, far)

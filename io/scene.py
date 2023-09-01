
import bpy
from .camera import CameraIO
from .film import FilmIO
from .mesh import MeshIO
from .material import MaterialIO
from .light import LightIO
from .. import pyvkkk as vk


class SceneIO(BaseIO):
    """
    """

    def __init__(self):
        self.cameraio = CameraIO()
        self.filmio = FilmIO()
        self.meshio = MeshIO()
        self.materialio = MaterialIO()
        self.lightio = LightIO()

        self.camera = vk.Camera()
        self.meshmgr = vk.MeshMgr.Instance()
        self.lightmgr = vk.LightMgr.Instance()

    def write_description(self, handle):
        self.lightio.write_description(handle)

        for obj in bpy.context.scene.objects:
            if obj.hide_get():
                continue

            if obj.type == 'MESH':
                self.meshio.write_description(handle)
                self.materialio.write_description(handle)

    def feed_api(self, ins):
        self.filmio.feed_api(ins)
        self.cameraio.feed_api(self.camera, self.filmio.get_ratio())
        
        for obj in bpy.context.scene.objects:
            if obj.hide_get():
                continue

            if obj.type == 'MESH':
                self.meshio.feed_api(obj, self.meshmgr)
                self.materialio.feed_api(obj)
            elif obj.type == 'LIGHT':
                self.lightio.feed_api(obj, self.lightmgr)

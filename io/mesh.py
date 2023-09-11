import struct
import bpy, bmesh
from .base import BaseIO
from ..utils import triangulate as tr
from .. import pyvkkk as vk


class MeshIO(BaseIO):
    """
    """

    def __init__(self):
        pass

    def write_description(self, handle):
        pass

    @staticmethod
    def convert_to_bytes(data, tmask):
        cnt = len(data[0])
        ret = bytes()
        for e in data:
            ret += struct.pack(tmask * cnt, *e)

    def feed_api(self, obj, mgr):
        depgraph = bpy.context.evaluated_depsgraph_get()
        bm = bmesh.new()
        bm.verts.ensure_lookup_table()
        bm.from_object(obj, depgraph)

        has_uvs = obj.data.uv_layers != None and len(obj.data.uv_layers) > 0
        if not has_uvs:
            raise Exception("Mesh {} doesn't have a UV set".format(obj.name))
        
        verts, normals, uvs, faces = tr.triangulateUV(obj, bm)
        v = len(verts)
        vbuf = self.convert_to_bytes(verts, 'f')
        i = len(faces)
        ibuf = self.convert_to_bytes(faces, 'I')
        mgr.load(obj.name, v, vbuf, i, ibuf)

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
        i = len(faces)
        mgr.load(v, vbuf, i, ibuf)
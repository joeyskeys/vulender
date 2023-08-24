
import os
import bpy
import threading
import time
from .. import config
from ..utils.registry import regular_registry


class BittoRenderThread(threading.Thread):
    def __init__(self, renderer):
        super(BittoRenderThread, self).__init__()
        self.renderer = renderer

    def run(self):
        # Something like the following line to actually start
        # the render
        # self.renderer.render()
        pass


class BittoRenderEngine(bpy.types.RenderEngine):
    bl_idname = config.engine_name
    bl_label = config.engine_label
    bl_use_preview = True
    bl_use_shading_nodes = False
    bl_use_postprocess = True

    # Ctor
    def __init__(self):
        self.renderer = None
        self.render_thread = None

    def __del__(self):
        pass

    def render(self, depsgraph):
        print("Currently just print 'rendering'")
        # Setup rendering thread to keep blender responsive
        # self.render_thread = BittoRenderThread(self.renderer)
        # self.render_thread.start()
        # while self.render_thread.isAlive()
        #     self.render_thread.join(0.5)

    def view_update(self, context, depsgraph):
        pass

    def view_draw(self, context, depsgraph):
        pass


def setup():
    regular_registry.add_new_class(BittoRenderEngine)
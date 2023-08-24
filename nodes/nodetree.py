
import bpy
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem
from nodeitems_builtins import ShaderNodeCategory
from .. import config
from ..utils.registry import Regular, shading_node_registry


@Regular
class BittoNodeTree(bpy.types.NodeTree):
    """
    """

    bl_label = "Bitto Material Nodes"
    bl_idname = "bitto_material_nodes"
    bl_icon = "MATERIAL"

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == config.engine_name


class BittoNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == config.engine_name and context.space_data.tree_type == "ShaderNodeTree"


bitto_shader_node_categories = []
original_poll_func = None

def hide_cycles_nodes_poll():
    @classmethod
    def func(cls, context):
        return context.scene.render.engine != config.engine_name
    return func


def hide_func(cls, context):
    return context.scene.render.engine != config.engine_name


def register():
    global original_poll_func
    original_poll_func = ShaderNodeCategory.poll
    ShaderNodeCategory.poll = hide_func

    for category, label in config.node_categories.items():
        bitto_shader_node_categories.append(BittoNodeCategory(category, label, items=
            [NodeItem(node_info[0], node_info[1]) for node_info in shading_node_registry.node_categories[label]]))
    nodeitems_utils.register_node_categories("BITTO_SHADER_NODES", bitto_shader_node_categories)


def unregister():
    ShaderNodeCategory.poll = original_poll_func
    nodeitems_utils.unregister_node_categories("BITTO_SHADER_NODES")
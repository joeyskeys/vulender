import bpy
from ..utils.typemap import bprop_map


class BittoProperties(bpy.types.PropertyGroup):
    @classmethod
    def init_annotations(cls, prop_dict):
        print('init annotation for ', cls.__name__)
        for attr in prop_dict:
            cls.__annotations__[attr['name']] = bprop_map[attr['type']](**attr['props'])


def init_annotations(cls, prop_dict):
    for attr in prop_dict:
        cls.__annotations__[attr['name']] = bprop_map[attr['type']](**attr['props'])


def setup_ui(layout, prop_dict, prop):
    for attr in prop_dict:
        layout.row().prop(prop, attr['name'], text=attr['text'])


def register_ui(prop_name, prop_class, ui_class):
    # Register property group
    bpy.utils.register_class(prop_class)
    pt = bpy.props.PointerProperty(type=prop_class)
    setattr(bpy.typs.Scene, prop_name, pt)

    # Register UIs
    bpy.utils.register_class(ui_class)


def unregister_ui(prop_name, prop_class, ui_class):
    # Unregister property group
    delattr(bpy.types.Scene, prop_name)
    bpy.utils.unregister_class(prop_class)

    # Unregister UIs
    bpy.utils.unregister_class(ui_class)
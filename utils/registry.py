import bpy
from .. import config


class Registry(object):
    def __init__(self):
        self.cls_to_register = []

    def add_new_class(self, cls):
        print('adding {} to list'.format(cls.__name__))
        self.cls_to_register.append(cls)

    def register(self):
        print('{} classes to register'.format(len(self.cls_to_register)))
        for c in self.cls_to_register:
            print('register', c.__name__)
            bpy.utils.register_class(c)

    def unregister(self):
        for c in self.cls_to_register:
            bpy.utils.unregister_class(c)


class PropertyGroupRegistry(Registry):
    def __init__(self):
        super(PropertyGroupRegistry, self).__init__()
        self.property_groups = {}

    def add_new_property_class(self, cls, host, prop_name):
        self.add_new_class(cls)
        self.property_groups[prop_name] = (cls, host)

    def register(self):
        super().register()
        for prop_name, (cls, host) in self.property_groups.items():
            setattr(host, prop_name, bpy.props.PointerProperty(type=cls))

    def unregister(self):
        super().unregister()
        for prop_name, (cls, host) in self.property_groups.items():
            delattr(host, prop_name)


class ShadingNodeRegistry(Registry):
    def __init__(self):
        super(ShadingNodeRegistry, self).__init__()
        self.node_categories = {}
        for category, label in config.node_categories:
            self.node_categories[label] = []

    def add_new_shading_class(self, cls, node_type=None):
        self.add_new_class(cls)

        if node_type in self.node_categories:
            self.node_categories[node_type].append((cls.__name__, cls.node_name))


regular_registry = Registry()
property_group_registry = PropertyGroupRegistry()
shading_node_registry = ShadingNodeRegistry()


class Regular(object):
    def __init__(self, cls):
        pass

    def __call__(self, cls):
        regular_registry.add_new_class(cls)
        return cls


class ShadingNode(object):
    def __init__(self, cls, node_type):
        self.node_type = node_type

    def __call__(self, cls):
        shading_node_registry.add_new_shading_class(cls, self.node_type)
        return cls


class Property(object):
    def __init__(self, host, prop_name):
        self.host = host
        self.prop_name = prop_name

    def __call__(self, cls):
        property_group_registry.add_new_property_class(cls, self.host, self.prop_name)
        return cls


def create_shading_category_classes():
    for category, label in node_category:
        cls = type(label, (object), {})
        shading_node_registry[category] = (cls, label)

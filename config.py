
engine_name = "vkkk"
engine_label = "vkkk"

film_props = ()

camera_props = (
    {
        'type' : 'float',
        'name' : 'near',
        'text' : 'Near',
        'props' : {
            'description' : 'Near clipping plane',
            'default' : 1,
        }
    },
    {
        'type' : 'float',
        'name' : 'far',
        'text' : 'Far',
        'props' : {
            'description' : 'Far clipping plane',
            'default' : 1000,
        }
    },
)

integrator_props = ()

light_props = ()

sampler_props = ()

world_props = ()

preference_props = (
    {
        'type' : 'int',
        'name' : 'test_prop',
        'text' : 'BlaBla',
        'props' : {
            'description' : 'this is a int property',
            'default' : 5,
        },
    },
)

node_categories = (
    ('BITTO_MATERIAL', 'Material'),
    ('BITTO_TEXTURE', 'Texture'),
)
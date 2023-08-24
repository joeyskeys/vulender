from . import film
from . import camera
from . import integrator
from . import light
from . import material
from . import preferences
from . import sampler
from . import world


def setup():
    film.setup()
    camera.setup()
    integrator.setup()
    light.setup()
    material.setup()
    preferences.setup()
    sampler.setup()
    world.setup()
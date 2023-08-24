
from .camera import CameraIO
from .film import FilmIO
from .sampler import SamplerIO
from .integrator import IntegratorIO
from .scene import SceneIO
from ..ui import preferences
import xml.etree.ElementTree as ET


class BittoOutput(object):
    """
    """

    def __init__(self):
        self.cameraio = CameraIO()
        self.filmio = FilmIO()
        self.samplerio = SamplerIO()
        self.integratorio = IntegratorIO()
        self.sceneio = SceneIO()
        
    def write_description(self, path):
        file_handle = open(path, 'w')
        root = ET.Element('Scene')

        self.filmio.write_description(root)
        self.cameraio.write_description(root)
        self.samplerio.write_description(root)
        self.integratorio.write_description(root)
        self.sceneio.write_description(root)

    def feed_api(self):
        self.filmio.feed_api()
        self.cameraio.feed_api()
        self.samplerio.feed_api()
        self.integratorio.feed_api()
        self.sceneio.feed_api()
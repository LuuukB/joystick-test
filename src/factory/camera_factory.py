# camera_factory.py
import asyncio
from pathlib import Path
from typing import Dict
from ..camera.i_camera_handler  import ICameraHandler
from ..camera.camera_handler import CameraHandler
from ..camera.offline_camera_handler import OfflineCameraHandler

class CameraFactory:
    """Factory en manager voor meerdere camera's tegelijk."""

    def __init__(self):
        self.cameras: Dict[str, ICameraHandler] = {}

    def add_camera(self, name: str, robot_online : bool, source: str = None, stream_name: str = "rgb"):
        """Voeg een camera toe aan de factory."""
        if robot_online:
            cam = CameraHandler(Path(source), stream_name)
        else:
            cam = OfflineCameraHandler(source)
        self.cameras[name] = cam

    def get_camera(self, name: str) -> ICameraHandler:
        return self.cameras[name]

    async def start_all(self):
        """Start alle camera's async."""
        await asyncio.gather(*(cam.start() for cam in self.cameras.values()))

    async def stop_all(self):
        """Stop alle camera's async."""
        await asyncio.gather(*(cam.stop() for cam in self.cameras.values()))

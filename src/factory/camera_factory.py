# camera_factory.py
import asyncio
from pathlib import Path
from typing import Dict
from camera_handler import CameraHandler
from amiga_camera import AmigaCamera
from offline_camera import OfflineVideoCamera

class CameraFactory:
    """Factory en manager voor meerdere camera's tegelijk."""

    def __init__(self):
        self.cameras: Dict[str, CameraHandler] = {}

    def add_camera(self, name: str, robot_online : bool, source: str = None, stream_name: str = "rgb"):
        """Voeg een camera toe aan de factory."""
        if robot_online:
            cam = AmigaCamera(Path(source), stream_name)
        else:
            cam = OfflineVideoCamera(source)
        self.cameras[name] = cam

    def get_camera(self, name: str) -> CameraHandler:
        return self.cameras[name]

    async def start_all(self):
        """Start alle camera's async."""
        await asyncio.gather(*(cam.start() for cam in self.cameras.values()))

    async def stop_all(self):
        """Stop alle camera's async."""
        await asyncio.gather(*(cam.stop() for cam in self.cameras.values()))

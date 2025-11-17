from ..factory.camera_factory import CameraFactory
from ..factory.can_bus_factory import CanBusFactory
class SetupConfig:
    def __init__(self):
        self.cameras = []
        self.robot_online = False
        self.check_robot_status()
        self.camera_factory = CameraFactory()
        self.can_bus_factory = CanBusFactory()

    def initialize(self):
        if self.robot_online:
            can = self.can_bus_factory.create_online("can")
            self.cameras.append( self.camera_factory.add_camera_online("oak1", "path"))
            self.cameras.append(self.camera_factory.add_camera_online("oak2", "path"))
            self.cameras.append(self.camera_factory.add_camera_online("oak3", "path"))
            self.camera_factory.start_all()
            return self.cameras, can
        else:
            self.cameras.append(self.camera_factory.add_camera_offline("can"))
            can = self.can_bus_factory.create_offline()
            self.camera_factory.start_all()
            return self.cameras, can

    def deinitialize(self):
        self.camera_factory.stop_all()
        #self.can_bus_factory

    def check_robot_status(self):
        #check robot status
        return self.robot_online





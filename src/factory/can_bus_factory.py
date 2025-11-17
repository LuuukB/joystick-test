class ServiceFactory:
    @staticmethod
    def create(robot_online, config):
        if robot_online:
            from ..can.can_handler import CanHandler
            return CanHandler(config)
        else:
            from  ..can.mock_can_handler import MockCanHandler
            return MockCanHandler()
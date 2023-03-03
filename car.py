from abc import ABC, abstractmethod

from Serviceable import Serviceable


class car(Serviceable):
    def __init__(self, Engine, Battery):
        self.Engine = Engine
        self.Battery = Battery

    def needs_service(self):
        Pick_service = self.Engine.needs_service() or self.Battery.needs_service()
        return Pick_service

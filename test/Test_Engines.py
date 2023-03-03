import unittest
import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CapuletTestEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 40000
        last_service_mileage = 0
        last_service_date = datetime.date(2015, 8, 23)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 15000
        last_service_mileage = 5
        last_service_date = datetime.date(2015, 8, 23)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class SternmanTestEngine(unittest.TestCase):
    def engine_should_be_serviced_true(self):
        light_on = True
        last_service_date = datetime.date(2015, 8, 23)
        engine = SternmanEngine(last_service_date, light_on)
        self.assertTrue(engine.needs_service())

    def engine_should_be_serviced_false(self):
        light_off = False
        last_service_date = datetime.date(2015, 8, 23)
        engine = SternmanEngine(last_service_date, light_off)
        self.assertFalse(engine.needs_service())


class WilloTestEngine(unittest.TestCase):
    def engine_serviced_true(self):
        current_mileages = 40000
        last_service_mileage = 0
        last_service_date = datetime.date(2015, 8, 23)
        engine = WilloughbyEngine(last_service_date, current_mileages, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def engine_serviced_false(self):
        current_mileage = 15000
        last_service_mileage = 5
        last_service_date = datetime.date(2015, 8, 23)
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

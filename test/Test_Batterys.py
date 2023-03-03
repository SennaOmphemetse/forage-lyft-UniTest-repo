from datetime import date
import unittest


from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery


class NubbinBatteryTest(unittest.TestCase):
    def battery_should_be_serviced_true(self):
        current_date = date.today()
        last_service_date = date(2015, 8, 23)
        check_battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(check_battery.needs_service())

    def battery_should_be_serviced_false(self):
        current_date = date.today()
        last_service_date = date(2022, 8, 23)
        check_battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(check_battery.needs_service())


class SpindlerBatteryTest(unittest.TestCase):
    def battery_should_be_serviced_true(self):
        current_date = date.today()
        last_service_date = date(2015, 8, 23)
        check_battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(check_battery.needs_service())

    def battery_should_be_serviced_false(self):
        current_date = date.today()
        last_service_date = date(2016, 8, 23)
        check_battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(check_battery.needs_service())



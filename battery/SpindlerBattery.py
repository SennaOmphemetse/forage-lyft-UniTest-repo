from battery.Battery import Battery
from datetime import datetime
from dateutil.relativedelta import relativedelta


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_should_be_serviced(self):
        todays_date = datetime.date.today()
        given_date = self.last_service_date + relativedelta(years=4)
        if given_date < todays_date:
            return True
        else:
            return False

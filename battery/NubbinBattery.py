from battery.Battery import Battery
from datetime import datetime
from JustTest import last_service
from JustTest import Number_years
from dateutil.relativedelta import relativedelta


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_should_be_serviced(self):
        today_date = datetime.date.today()
        given_date = last_service(self.last_service_date) + Number_years(2)
        if given_date < today_date:
            return True
        else:
            return False

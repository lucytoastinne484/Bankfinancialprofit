#Salary Class implementation , 2023/06/14#

import math
import calendar
from datetime import datetime
from datetime import date
import time




class Salary:
    def __init__(self):
        pass
    x = float(input("Put your salary: "))
    y = float(input("Put the days you worked:"))
    motnh_salary = x/30 * y
    print(motnh_salary)


class Salary2 :
    def __init__(self):
        pass
    def __init__(self, x2 , y2):
        self.x2 = x2
        self.y2 = y2
        month_salary_2 = x2/30 * y2
        print(month_salary_2)


class PaymentDay:
    def __init__(self):
        pass
    day = date(2023, 7,21)
    print(day)

class YearCalendar(PaymentDay):
    def __init__(self):
        super().__init__()
    def __init__():
        pass
    calendar.prcal(2023)





PaymentDay()

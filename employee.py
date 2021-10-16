#File: employee.py
#Author: Chris Dieckhoff
#Date: 10/10/2021
#Description: This was a project in a C++ course I took in College and decided to port it in python

class employee:
    def __init__(self, name, hourlyWage, hoursWorked):
        self.name = name
        self.payrate = hourlyWage
        self.otrate = round(hourlyWage*1.5,2)
        if(hoursWorked > 40):
            self.hoursWorked = 40
            self.otHours = hoursWorked - 40
        else:
            self.hoursWorked = hoursWorked
            self.otHours = 0

    def getTotalPay(self):
        return round((self.hoursWorked * self.payrate) + (self.otHours * (self.payrate * 1.5)), 2)

    def summary(self):
        sm = "          Name:  {0}\n".format(self.name)
        sm += "  Regular Rate:  ${0:.2f}\n".format(self.payrate)
        sm += " Overtime Rate:  ${0:.2f}\n".format(self.payrate * 1.5)
        sm += " Regular Hours:  {0:.2f}\n".format(self.hoursWorked)
        sm += "Overtime Hours:  {0:.2f}\n".format(self.otHours)
        sm += "   Regular Pay:  ${0:.2f}\n".format(round(self.payrate * self.hoursWorked), 2)
        sm += "  Overtime Pay:  ${0:.2f}\n".format(round(self.otrate * self.otHours),2)
        sm += "     Total Pay:  ${0:.2f}\n".format(self.getTotalPay())
        return sm
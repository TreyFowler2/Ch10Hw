class payrolldeduction:
    def __init__(self, desc, date, chgamt, empid):
        self.__description = desc
        self.__date = date
        self.__chargeamt = chgamt
        self.__employeeid = empid
        self.__totalamt = 0

    def get_description(self):
        return self.__description
    def get_date(self):
        return self.__date
    def get_chargeamt(self):
        return self.__chargeamt
    def get_employeeid(self):
        return self.__employeeid
    def get_totalamt(self, charge2, charge4, charge5):
        self.__totalamt = charge2 + charge4 + charge5
        return self.__totalamt

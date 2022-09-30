class Employee:
    def __init__(self, name, id_number, department, jobt, msal):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__jobt = jobt
        self.__msal = msal

    def get_name(self):
        return self.__name
    def get_id_number(self):
        return self.__id_number
    def get_department(self):
        return self.__department
    def get_jobt(self):
        return self.__jobt
    def get_salary(self):
        return self.__msal




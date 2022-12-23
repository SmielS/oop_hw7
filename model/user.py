class User:
    def __init__(self, first_name, last_name, patronymic):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__patronymic = patronymic

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_patronymic(self, patronymic):
        self.__patronymic = patronymic

    def get_patronymic(self):
        return self.__patronymic

    def __str__(self):
        return 'Full name: ' + self.__last_name + ' ' \
            + self.__first_name + ' ' + self.__patronymic

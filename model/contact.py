class Contact:
    def __init__(self, contact_user, phone, contact_id):
        self.__user = contact_user
        self.__phone = phone
        self.__contact_id = contact_id

    def set_user(self, contact_user):
        self.__user = contact_user

    def get_user(self):
        return self.__user

    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def set_id(self, contact_id):
        self.__contact_id = contact_id

    def get_id(self):
        return self.__contact_id

    def __str__(self):
        return 'ID: ' + self.__contact_id + '. ' + \
            str(self.__user) + '. Phone: ' + self.__phone

from model import repository
from model import contact
from model import user


class Controller:
    def __init__(self, _repository):
        self.__repository = _repository

    def read_contact(self, contact_id):
        contacts = []
        if isinstance(self.__repository, repository.Repository):
            contacts = self.__repository.get_all_contact()
            for _contact in contacts:
                if isinstance(_contact, contact.Contact):
                    if _contact.get_id() == contact_id:
                        return _contact
        print('Contact not found!')

    def read_contacts(self):
        if isinstance(self.__repository, repository.Repository):
            return self.__repository.get_all_contact()

    def save_contact(self, _contact):
        if Controller.validate_contact_data(self, _contact):
            if isinstance(self.__repository, repository.Repository):
                self.__repository.create_contact(_contact)
                print('Done')


    def validate_contact_data(self, _contact):
        if isinstance(_contact, contact.Contact):
            _user = _contact.get_user()
            if isinstance(_user, user.User):
                if not _user.get_last_name() or not _user.get_first_name() or not _user.get_patronymic() or not _contact.get_phone():
                    print('Fields are empty!')
                    return False
        return True

    def delete_contact(self, contact_id):
        if isinstance(self.__repository, repository.Repository):
            self.__repository.delete_contact(contact_id)

    def edit_contact(self, _contact):
        if Controller.validate_contact_data(self, _contact):
            if isinstance(self.__repository, repository.Repository):
                self.__repository.edit_contact(_contact)

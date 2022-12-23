from model import contact
from model import user


class ContactMapperCsv:
    def map_to_str(self, _contact):
        if isinstance(_contact, contact.Contact):
            _user = _contact.get_user()
            if isinstance(_user, user.User):
                return str(_contact.get_id()) + ';' + _user.get_last_name() + ';' + \
                    _user.get_first_name() + ';' + _user.get_patronymic() + ';' + \
                    _contact.get_phone()
            else:
                return 'Input data error!'
        else:
            return 'Input data error!'

    def map_from_str(self, line):
        lines = line.split(';')
        return contact.Contact(user.User(lines[2], lines[1], lines[3]), lines[4], str(lines[0]))

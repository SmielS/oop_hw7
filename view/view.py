from controller import controller
from model import user
from model import contact


class View:
    def __init__(self, _controller):
        self.__controller = _controller

    def run(self):
        while True:
            command = str(input('Input command (help - list of all commands): '))
            if command.lower() == 'exit':
                return

            if command.lower() == 'create':
                first_name = str(input('Input first name: '))
                last_name = str(input('Input last name: '))
                patronymic = str(input('Input patronymic: '))
                phone = str(input('Input phone: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.save_contact(contact.Contact(user.User(first_name, last_name, patronymic),
                                                                   phone, '0'))
            elif command.lower() == 'read':
                contact_id = str(input('Input ID: '))
                if isinstance(self.__controller, controller.Controller):
                    print(self.__controller.read_contact(contact_id))
            elif command.lower() == 'list':
                if isinstance(self.__controller, controller.Controller):
                    contacts = self.__controller.read_contacts()
                    for _contact in contacts:
                        print(_contact)
            elif command.lower() == 'delete':
                contact_id = str(input('Input ID: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.delete_contact(contact_id)
            elif command.lower() == 'edit':
                contact_id = str(input('Input ID: '))
                first_name = str(input('Input first name: '))
                last_name = str(input('Input last name: '))
                patronymic = str(input('Input patronymic: '))
                phone = str(input('Input phone: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.edit_contact(contact.Contact(user.User(first_name, last_name, patronymic),
                                                                   phone, contact_id))
            elif command.lower() == 'help':
                print('List of commands:')
                print('create - create new contact')
                print('read - display contact by ID')
                print('list - display list of all contacts')
                print('edit - edit contact by ID')
                print('delete - delete contact by ID')
                print('exit - exit from program')
            else:
                print('Command not found!')

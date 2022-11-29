from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Contact, Phone
from sqlalchemy.sql import select
from functions.add_functions import *
from functions.change_functions import *
from functions.delete_functions import *
from functions.show_functions import *


def create_session():

    engine = create_engine("sqlite:///addressbook.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


COMMANDS = {"add_contact": add_contact,
            "add_phone": add_phone,
            "add_email": add_email,
            "delete_contact": delete_contact,
            "delete_phone": delete_phone,
            "delete_email": delete_email,
            "change_phone": change_phone,
            "change_email": change_email,
            "show_contact": show_contact,
            "show_phones": show_phones}


def handler(comm):
    return COMMANDS[comm]


def main():

    session = create_session()

    while True:

        user_command = input("Enter a command: ")
        parsed = user_command.split(' ')

        command = parsed[0].lower()

        if command == 'hello':
            print('How can I help you?')

        elif command in COMMANDS.keys():
            print(handler(command)(parsed, session))

        elif command in ["goodbye", "close", "bye"]:
            print("Goodbye!")
            break

        else:
            print("NO SUCH A COMMAND")


if __name__ == '__main__':

    main()

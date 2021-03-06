from datetime import datetime
import pickle


class Contact:
    """
    Define instances of User contacts
    """

    def __init__(self, name, last_name, age, email, phones):
        self.hidden = False
        self.creation_date = datetime.now()
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        # phones is a dictionary with key=phone_number and value=number_type such as "home","office" e.t.c
        self.phones = phones
        pass

    @property
    def full_name(self):
        return "{} {}".format(self.name, self.last_name)

    def __lt__(self, other):
        return self.creation_date < other.creation_date

    def __str__(self):
        return "Full name: {}, Age: {}, Email: {}, Phones: {} ".format(self.full_name, self.age,
                                                                       self.email, self.phones)

    @staticmethod
    def generator(contacts):
        gen = (x for x in contacts if not x.hidden)
        l1 = list(gen)
        return l1

    def update_contact(self, **fields):
        if "name" in fields:
            self.name = fields["name"]
        if "last_name" in fields:
            self.last_name = fields["last_name"]
        if "age" in fields:
            self.age = fields["age"]
        if "email" in fields:
            self.email = fields["email"]
        if "phones" in fields:
            if "type" in fields:
                self.phones[fields["phones"]] = fields["type"]
            if "phone_num" in fields:
                _temp = self.phones[fields["phones"]]
                del self.phones[fields["phones"]]
                self.phones[fields["phone_num"]] = _temp


class User:
    """
    Define the instance of an user
    """

    def __init__(self):
        self.contact_list = []
        pass

    def update_contact(self, index, **fields):
        contact = self.contact_list[index]
        contact.update_contact(fields)
        pass

    def hide_contact(self, index):
        contact = self.contact_list[index]
        contact.hidden = True
        pass

    def create_contact(self, name, last_name, age, email, phones):
        new_user = Contact(name, last_name, age, email, phones)
        self.contact_list.append(new_user)
        pass

    def sort_by_date_and_visible(self):
        sorted_list = sorted(Contact.generator(self.contact_list))
        return sorted_list

    def __get_contact(self, index):
        return self.contact_list[index]


def show_menu():
    print("==============")
    print("Welcome User:")
    print("Options:")
    print("1. List contacts")
    print("2. Create new contact")
    print("3. Update existing contact")
    print("4. Hide contact")
    print("5. Save User")
    print("6. Load User")
    print("7. Quit")
    print("==============")
    pass


def show_menu_1():
    print("===============")
    print("Options")
    print("1. List contacts")
    print("2. List contacts sorted by date creation")
    print("3. List hidden contacts")
    print("==============")
    pass


def show_menu_3():
    print("===============")
    print("What do you want to modify")
    print("1. Name")
    print("2. Last name")
    print("3. Age")
    print("4. Email")
    print("5. Phone numbers")
    print("6. Don't modify")
    print("===============")
    pass


def handle_menu_1(user, op):
    print("==============")
    if op == 1:
        for i in user.contact_list:
            if not i.hidden:
                print(i)
        pass
    if op == 2:
        for i in user.sort_by_date_and_visible():
            print(i)
        pass
    if op == 3:
        for i in user.contact_list:
            if i.hidden:
                print(i)
        pass
    print("==============")
    pass


def handle_menu_2(user):
    print("==============")
    _name = input("Input name: ")
    _last_name = input("Input Last name: ")
    _age = int(input("Input age: "))
    _email = input("Input email: ")
    print("==============")
    _option = ""
    _dict = {}
    while _option != "n":
        _key = int(input("Input phone number: "))
        _val = input("Input number type: ")
        _dict[_key] = _val
        _option = input("Do you want to add another number [y/n]: ")

    user.create_contact(_name, _last_name, _age, _email, _dict)
    pass


def handle_menu_3(user):
    print("===============")
    for i, e in enumerate(user.contact_list):
        print("{}. {}".format(i, e))

    _option = int(input("Input contact index to modify: "))
    contact = user.contact_list[_option]
    while _option != 6:
        show_menu_3()
        _option = int(input("Input option: "))
        if _option == 1:
            contact.update_contact(name=input("Input new name: "))
            pass
        if _option == 2:
            contact.update_contact(last_name=input("Input new last name: "))
            pass
        if _option == 3:
            contact.update_contact(age=int(input("Input new age: ")))
            pass
        if _option == 4:
            contact.update_contact(email=input("Input new email: "))
            pass
        if _option == 5:
            print("===============")
            for e in contact.phones:
                print(e)
            _option1 = int(input("Which phone do you want to modify or a new number to add a new one: "))
            if _option1 not in contact.phones:
                contact.update_contact(phones=_option1, type=input("Phone type: "))
                continue

            _temps = input("Do you wanna modify the type or number [type/number]: ")

            if _temps == "number":
                _data = int(input("Input new phone number: "))
                contact.update_contact(phones=_option1, phone_num=_data)
            else:
                _data = input("Input new type: ")
                contact.update_contact(phones=_option1, type=_data)
            print("===============")
            pass

    print("===============")
    pass


def handle_menu_4(user):
    print("==============")
    _l = [x for x in user.contact_list if not x.hidden]
    for i, e in enumerate(_l):
        print("{}. {}".format(i, e))
    _option = int(input("Input number of contact you want to hide: "))
    _l[_option].hidden = True
    print("==============")
    pass


def handle_menu_5(user):
    print("===============")
    s = input("Input File name to save: ")
    s += ".pickle"
    print(s)
    f1 = open(s, "wb")
    f1.write(pickle.dumps(user))
    f1.close()
    print("===============")
    pass


def handle_menu_6():
    print("===============")
    s = input("Input File name to load (without extension): ")
    s += ".pickle"
    print(s)
    f2 = open(s, "rb")
    from_file = f2.read()
    f2.close()
    user = pickle.loads(from_file)
    print("===============")
    return user


u = User()
option = 0
while option != 7:
    show_menu()
    option = int(input("Input number option "))
    if option == 1:
        show_menu_1()
        option_1 = int(input("Input number option "))
        handle_menu_1(u, option_1)
        pass
    if option == 2:
        handle_menu_2(u)
        pass
    if option == 3:
        handle_menu_3(u)
        pass
    if option == 4:
        handle_menu_4(u)
        pass
    if option == 5:
        handle_menu_5(u)
        pass
    if option == 6:
        u = handle_menu_6()
        pass

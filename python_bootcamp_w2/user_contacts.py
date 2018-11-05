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

    def __lt__(self, other):
        return self.creation_date < other.creation_date

    def __str__(self):
        return "Name: {}, Last name: {}, Age: {}, Email: {}, Phones: {} ".format(self.name, self.last_name, self.age,
                                                                                 self.email, self.phones)

    def update_contact(self, **fields):
        pass
    """
    
    def update_contact(self, **fields):
        if "name" in fields:
            self.name = fields["name"]
        if "last_name" in field:
            self.last_name = fields["last_name"]
        if "age" in fields:
            self.age = fields["age"]
        if "email" in fields:
            self.email = fields["email"]
        if "phone" in fields:
            self.phones[ fields["phone"] ]

        # Later
    """


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
        sorted_list = sorted([e for e in self.contact_list if not e.hidden])
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
    while(_option != "n"):
        _key = int(input("Input phone number: "))
        _val = input("Input number type: ")
        _dict[_key]=_val
        _option = input("Do you want to add another number [y/n]: ")

    user.create_contact(_name,_last_name,_age,_email,_dict)
    pass

#Handle_menu_3

def handle_menu_4(user):
    print("==============")
    _l = [x for x in user.contact_list if not x.hidden]
    for i, e in enumerate(_l):
        print("{}. {}".format(i,e))
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
    s+=".pickle"
    print(s)
    f2 = open(s, "rb")
    from_file = f2.read()
    f2.close()
    user = pickle.loads(from_file)
    print("===============")
    return user


u = User()

"""
u.create_contact("Juan","Perez",10,"JP@hotmail.com", { 123:"home", 321:"office"})
u.create_contact("Jonhatan","Florez",20,"JF@hotmail.com", {3123:"home"})
u.create_contact("Pedro","Ramirez",30,"PR@gmail.com",{})

"""

option = 0
while option != 7:
    show_menu()
    option = int(input("Input number option "))
    if option == 1:
        show_menu_1()
        option_1 = int(input("Input number option "))
        handle_menu_1(u,option_1)
        pass
    if option == 2:
        handle_menu_2(u)
        pass
    if option == 3:
        #missing modified
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

from datetime import datetime

class Phone:
    """
    Define instances of contact number phones with its type
    """
    def __init__(self,type="casa",number):
        self.number=number
        self.type=type
        pass

class Contact:
    """
    Define instances of User contacts
    """
    def __init__(self,name,last_name,age,email):
        self.hidden = False
        self.creation_date = datetime.now()
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.Phones = set()
        pass

class User:
    """
    Define the instace of an user
    """
    def __init__(self):
        self.contact_list=[]
        pass

    def update_contact(self, **fields):
        pass

    def hide_contact(self,user):
        pass

    def create_contact(self,):
        pass





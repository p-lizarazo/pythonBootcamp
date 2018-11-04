

class Phone:
    """
    Define instances of contact number phones with its type
    """
    def __init__(self,type="casa",number):
        self.number=number
        self.type=type


class Contact:
    """
    Define instances of User contacts
    """
    def __init__(self,name,last_name,age,email,):
        self.hidden = False
        self.creation_date = #here goes the tiem elibrary w.e
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.Phones = set()

    

class User:
    """
    Define the instace of an user
    """
    def __init__(self):
        self.contact_list=[]

    def update_contact(self, **fields):
        pass

    def




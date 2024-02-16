class Phone:
    def __init__(self, name, last_name, phone_number):
        self.name = name
        self.last_name = last_name
        self.phone_number= phone_number
    def get_info(self):
        return "Contact: {name} {last_name}, phone:{num}".format(name= self.name, last_name = self.last_name,
                                                                 num = self.phone_number)

contact = Phone("Gleb", "Efremenko", "89237164689")
print(contact.get_info())
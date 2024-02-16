class Password:
    def __init__(self, password):
        self.password = password
    def validate(self):
        if len(self.password) < 8 or len(self.password) > 15:
            raise ValueError("You wrote an incorrect password (length)")
        elif not any(char.isdigit() for char in self.password):
            raise ValueError("You wrote an incorrect password (digit)")
        elif not any(char in "@', '#', '&', '$', '%', '!', '~', '*" for char in self.password):
            raise ValueError("You wrote an incorrect password (symbols)")
        else:
            print( "Your password has been saved")
    def __str__(self):
        return "*" * len(self.password)


first = Password("554frrrdd4#")
first.validate()
print(first.__str__())
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


user = User('Stiven', 'Spilberg')
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
# user.full_name = 'Stiven Hoking' # AttributeError: property 'full_name' of 'User' object has no setter
user.last_name = 'Hoking'
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')

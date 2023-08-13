class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


user = User('Stiven')
print(f'{user.name = }')
# user.name = 'Slavik' # AttributeError: property 'name' of 'User' object has no setter

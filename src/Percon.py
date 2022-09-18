class Person:
    def __init__(self, person_id, name, address, work, age):
        self.person_id = person_id
        self.name = name
        self.address = address
        self.work = work
        self.age = age

    def get_id(self):
        return self.person_id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age



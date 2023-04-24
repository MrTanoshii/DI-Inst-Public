# OOP

# Theses are not definitions, these are "non-tech" explanations
# Classes are the bluetprints/templates for objects
# Objects is an instance of a class
# A method is a function which is associated with a class


class Electronics:
    total_electronics_count = 0
    object_list = []

    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand
        Electronics.total_electronics_count += 1
        # total_electronics_count += 1 # This will not work

        Electronics.object_list.append(self)
        self.display()

    def __str__(self):
        return f"{self.name} | {self.brand} - ${self.price}"

    def __gt__(self):
        pass

    def display(self):
        print(self)


import json


class TV(Electronics):
    def __init__(self, name, price, brand, screen_size=0):
        self.screen_size = screen_size  # This will work
        super().__init__(name, price, brand)
        # self.screen_size = screen_size # This will fail

    def __str__(self):
        return f"{self.name} | {self.brand} - ${self.price} - {self.screen_size}"

    def save_json(self):
        # Save a json representation of this object in a .json file
        file_name = "tv_json.json"
        with open(file_name, "w") as file:
            json.dump(self.__dict__, file)

    def load_json(self):
        # Load a .json file and make my object resemble it
        file_name = "tv_json.json"
        with open(file_name, "r") as file:
            json_dict = json.load(file)

        self.screen_size = json_dict["screen_size"]
        self.name = json_dict["name"]
        self.price = json_dict["price"]
        self.brand = json_dict["brand"]

        print(json_dict)

        self.display()

        # Another method
        # make a new TV()
        # return the TV()
        # You would need to reassign `television` to the returned value


# TV should contain screen_size
# Mouse should contain number_buttons


# print(Electronics.total_electronics_count)

# television = Electronics("TV", 1000, "Samsung")
television = TV("TV", 1000, "Samsung", 100)
# television.save_json()
television.load_json()
# print(Electronics.total_electronics_count)
# print(f"The length of the list is: {len(Electronics.object_list)}")

# mouse = Electronics("Mouse", 50, "Logitech")
# print(Electronics.total_electronics_count)
# print(f"The length of the list is: {len(Electronics.object_list)}")
# mouse.display()


# DATABASE

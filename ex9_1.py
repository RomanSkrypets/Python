class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name} and kitchen {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\nThe {self.restaurant_name} is open!")

rest = Restaurant('Texe','spanish')

print(f"\nRestaurant {rest.restaurant_name} has a kitchen {rest.cuisine_type}")
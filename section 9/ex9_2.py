class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name} and kitchen {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\nThe {self.restaurant_name} is open!")

rest_texe = Restaurant('Texe', 'spanish')
rest_fr = Restaurant('France', 'francis')
rest_sush = Restaurant('SuPro', 'japanise')

print(f"\nRestaurant {rest_texe.cuisine_type} kitchen - {rest_texe.restaurant_name}")
print(f"\nRestaurant {rest_fr.cuisine_type} kitchen - {rest_fr.restaurant_name}")
print(f"\nRestaurant {rest_sush.cuisine_type} kitchen - {rest_sush.restaurant_name}")
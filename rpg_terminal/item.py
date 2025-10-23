from utilities import say

#Item class
class Item:
    def __init__(self, name, healing, quantity):
        self.name = name
        self.healing = healing
        self.quantity = quantity
    def use_healing_item(self):
        # Depending on the item it will heal x HP
        if self.quantity != 0: 
            self.quantity = self.quantity - 1
            return self.healing
        else: 
            say(f'No {self.name} left...')
            return 0

import random as rd
from utilities import say
from item import Item
#=============================================
# CHARACTER AND GAME CLASSES
#=============================================
#Lord class
class Lord:
    def __init__(self, name, maxHealth): 
        self.name = name
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.inventory = [Item('Vulnerary',20,3)]
        

    # Checks that player never has more than the max health
    def limit_of_health(self):
        if self.health > self.maxHealth:
            self.health = self.maxHealth
    # Method 1: Player attacking
    def attack(self):
        damage = 12
        random_multiplier = rd.randint(1,4)
        totalDamage = damage + random_multiplier
        say([f'{self.name} slashed the enemy!', f'{totalDamage} HP lost!'])
        return totalDamage
        
    # Method 2: Player healing
    def heal(self):
        for item in self.inventory:
            if item.name == 'Vulnerary':
                healing = item.use_healing_item()
                if healing != 0:
                    say([f'{self.name} uses a {item.name}!', f'{self.name} recovers {healing} HP!'])
                self.health += healing
                self.limit_of_health()

#Enemy class
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        enemyIA = rd.randint(1, 3)
        damage = 10
        if enemyIA == 1 or enemyIA == 2:
            random_multiplier = rd.randint(1,4)
            totalDamage = damage + random_multiplier
            say([f"{self.name} swings it's axe!", f'{totalDamage} HP lost!'])
            return totalDamage
        elif enemyIA == 3:
            secondHit = damage / 2
            totalDamage = damage + secondHit
            say([f'{self.name} swings twice!', f'{totalDamage} HP lost!'])
            return totalDamage

import os
import random as rd

# Clear terminal
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Dialogue to improve conversations
def say(text):
    if(isinstance(text,list)):
        for line in text:
            print(line)
            input()
    else:
        print(text)
        input()
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
        
# Item List For Now
vulnerary = Item('Vulnerary',20,3)

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
    def heal(self, item):
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

#Combat system
def combatSystem(player, enemy):
    clear_console()
    #Check the enemy type you encounter
    say(f'You encounter {enemy.name}!')
    #When check, initiates combat
    #Player Turn
    while player.health > 0 and enemy.health > 0:
        
        print(' ================= ')
        print(f'   {player.name}   ')
        print(f'  Health Points: {player.health}/{player.maxHealth}')
        print(' ================= ')
        while True:
            try:
                option = int(input('  Actions: 1) ATTACK | 2) HEAL   '))
                if option in [1, 2]:
                    break
                else:
                    print('-Wrong input- -Try again-')
            except ValueError:
                print('-Insert a number-')
        if option == 1:
            totalDamage = player.attack()
            enemy.health -= totalDamage
        elif option == 2:
            player.heal(vulnerary)
    #Enemy Turn

        if enemy.health > 0:
            print(' ================= ')
            print(f'   {enemy.name}   ')
            print(f'  Health Points: {enemy.health}')
            print(' ================= ')
            say(f'{enemy.name} turn!')
            totalDamage = enemy.attack()
            player.health -= totalDamage
    # Checks win condition
    if enemy.health <= 0: 
        say(['All enemies have been defeated!', f'{player.name} wins!'])
        return True
    elif player.health <= 0:
        say([f'Oh no! {player.name} has collapsed!', 'GAME OVER' ])
        return False
       


        
# This little rpg is inspired by one of the chapters of Fire Emblem (2003) so spoilers ahead if you wish to play the game before
# If any of your character's HP drops to 0 you lose!

# These are the protagonists of Fire Emblem (2003) each one has an unique fighting style, in this demo only Lin will be playable

#character_1 = 'Eliwood' # Eliwood has a rapier
# Lyn character: Lyn uses as primary weapon a sword
player = Lord('Lyn', 40)
#character_3 = 'Hector' # Hector has an axe

#Enemy Number 3: Bandits
bandit1 = Enemy('Bandit Herny', 22)
banditLeader = Enemy('Batta the Beast', 33)
"""
vulnerary = 3
print(vars(player))
print(vars(banditLeader))
player.heal(vulnerary)
print(vulnerary)
print(player.health)
"""
#boss = 'Black Fang'
# Like in Fire Emblem, weapon triangles are essential to understand the flaws and strengths of your party
# Rapiers beat Swords (Normally are Lances, but Eliwood doesn't use a spear lmao)
# Swords beat Axes
# Axes beat Rapiers

alive = True

# Chapter 0: The Girl of The Plains

if alive:
    say(['??: Are you awake? ','I found you unconscious on the plains.',f"I am {player.name}, of the Lorca tribe. You're safe now."])
    tactician = input("Who are you? Can you remmember my name? ")
    while tactician == '':
        print("Please insert a name. ")
        tactician = input("Who are you? Can you remmember my name? ")
    say([f'Your name is {tactician}? What an odd-sounding name... ','But pay me no mind. It is a good name.','I see by your attire that you are a traveler',
        'What brings you to the Sacae Plains?','Would you share your story with me?','Hm? What was that noise?',"Oh, no! Bandits! They must have come down from the Bern Mountains!",
        "They must be planning on raiding the local villages. I... I have to stop them!",f"If that's all of them I can handle them of my own. You'll be safe in here, {tactician}.",
        "What? You want to help? Well, can you use a weapon?","Ah, I see... So you're a strategist by trade? An odd profession, but... ","Very well. We'll go together!"])

    say(["(A bandit is approaching you!)",f'If you want to help {tactician}, I could use your advice.',"I'll protect you, so stay close to me.",
         f"({player.name} will aid you, be wise and help {player.name} to defeat her foes!)"])

    # Combat Nº1 
    alive = combatSystem(player,bandit1)

    say([f'{player.name}: Victory!',"But I've been injured.",'I have need of a vulnerary.'])

    while True:
        try:
            print(f'Heal {player.name}? 1) Yes | 2) No ')
            heal = int(input(''))
            if heal in [1,2]:
                break
            else: 
                print('-Wrong input- -Try again-')  
        except ValueError:
           print('-Insert a number-') 
    if heal == 1:
        player.heal(vulnerary)
        say(f"{player.name}: Thank you {tactician}! Now let's go get that brigand over by the ger!")
                
    elif heal == 2:
        say(f"{player.name}: Let's go get that brigand over by the ger!")

    say(["(You reach finally to the bandits base.)","??: Who do you think you are? ",f"??: You think you can stand up to {banditLeader.name}?"])
    
    
    # Combat Nº2 
    alive = combatSystem(player,banditLeader)
           
    say(['Lyn: Whew... \nThat was close.', 'I sorely underestimated him \nSorry if I worried you.',
         "I'll need to be stronger if I'm going to survive... Strong enough that no one can defeat me.",
         f"Good work, {tactician}!\nLet's go home.",'That fight must have taken a lot out of you.'])
    say("You have some experience in the ways of the war, I can see.")
      
    answer = input("Would you allow me to travel with you? (Yes/No) ")
    while answer is '' and answer is not 'Yes' and answer is not 'No':
        print("Please insert Yes or No. ")
        answer = input("Would you allow me to travel with you? (Yes/No) ")
    if answer == 'Yes':
        say(["What? You... want me to get permission from my parents?","My mother and my father died six months ago.",
             "My people the Lorca they don't...\n I'm the last of my tribe.",f"The apprentice tactician {tactician} and the young swordfighter {player.name}.",
             'A strange pair on an even stranger journey.','Chapter 0 ends.'])
        alive = False
    elif answer == 'No':
        say(f'I see... I pray for your safety then, {tactician}.')
        alive = False



    
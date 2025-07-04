import random

# This little rpg is inspired by one of the chapters of Fire Emblem (2003) so spoilers ahead if you wish to play the game before
# If any of your character's HP drops to 0 you lose!

# These are the protagonists of Fire Emblem (2003) each one has an unique fighting style, in this demo only Lin will be playable

#character_1 = 'Eliwood' # Eliwood has a rapier
character_2 = 'Lyn' # Lin has a sword
#character_3 = 'Hector' # Hector has an axe

#enemy_1 = 'Cavalry'
#enemy_2 = 'Knight'
#Enemy Number 3: Bandits
hp_bandit = 22
hp_banditleader = 33

#boss = 'Black Fang'
# Like in Fire Emblem, weapon triangles are essential to understand the flaws and strengths of your party
# Rapiers beat Swords (Normally are Lances, but Eliwood doesn't use a spear lmao)
# Swords beat Axes
# Axes beat Rapiers

lance_damage = 11
sword_damage = 12
axe_damage = 14

game_over = False

# Lyn character: Lyn uses as primary weapon a sword (sword_damage)
hp_lyn = 32
vulnerary = 3


# Chapter 0: The Girl of The Plains

print('??: Are you awake? ')
input()
print('I found you unconscious on the plains.')
input()
print("I am Lyn, of the Lorca tribe. You're safe now.")
input()
player = input("Who are you? Can you remmember my name? ")
while player == '':
     print("Please insert a name. ")
     player = input("Who are you? Can you remmember my name? ")
print('Your name is ' + str(player) + '? What an odd-sounding name... ')
input()
print('But pay me no mind. It is a good name.')
input()
print('I see by your attire that you are a traveler')
input()
print('What brings you to the Sacae Plains? ')
input()
print('Would you share your story with me? ')
input()
print('Hm? What was that noise?')
input()
print("Oh, no! Bandits! They must have come down from the Bern Mountains!")
input()
print("They must be planning on raiding the local villages. I... I have to stop them!")
input()
print("If that's all of them I can handle them of my own. You'll be safe in here, " + str(player) + ".")
input()
print("What? You want to help? Well, can you use a weapon?")
input()
print("Ah, I see... So you're a strategist by trade? An odd profession, but... ")
input()
print("Very well. We'll go together!")
input()
print("(A bandit is approaching you!)")
input()
print("If you want to help, " + str(player) + ", I could use your advice.")
input()
print("I'll protect you, so stay close to me.")
input()
print("(" + str(character_2) + " will aid you, be wise and help " + str(character_2) +  " to defeat her foes!)")
input()
# Combat Nº1 
print("You encounter with a bandit!")
combat = True
while combat is True:
        # Checks if the player has HP left and the enemy doesn't have HP left
        if hp_bandit <= 0 and hp_lyn > 0:
            print('The enemy has been defeated')
            print('You won!')
            input()
            combat = False
        # Checks if the player HP is 0 the battle is over
        elif hp_lyn <= 0 and hp_bandit > 0:
            game_over = True
            combat = False
        else: 
            # Menu
            print()
            print('---- ' + str(character_2) + ' ----')
            print('---- HP: 32/' + str(hp_lyn) +  ' ----')
            print('---- Actions: 1) Attack | 2) Heal ----')
            attack = int(input('---- Choose an option: '))
            while attack != 1 and attack != 2:
                    print("ERROR: Choose an option")
                    attack = int(input('---- Choose an option: '))
                
            # Player Attacking the Enemy
            if attack == 1:
                random_multiplier = random.randint(1, 3)
                total_damage = sword_damage - random_multiplier

                print(str(character_2) + ' slashes the enemy! ' + str(total_damage) + ' HP!')
                hp_bandit = hp_bandit - total_damage
                
            #Player healing itself 
            elif attack == 2 and vulnerary != 0:
                random_multiplier = random.randint(1, 3)
                total_heal = 15 + random_multiplier

                print(str(player) + ' uses a vulnerary!')
                vulnerary = vulnerary - 1
                hp_lyn = hp_lyn + total_heal
                print(str(character_2) + ' recovers ' + str(total_heal) + ' HP!')
                # To prevent the player has more hp than the max
                if hp_lyn > 32:
                    hp_lyn = 32
            
            elif vulnerary <= 0:             
                    print('You ran out of vulneraries!')
                   
            
        # Checks if the player has HP left and the enemy doesn't have HP left
        if hp_bandit <= 0 and hp_lyn > 0:
            print('The enemy has been defeated')
            print('You won!')
            input()
            combat = False
        
        # Checks if the player HP is 0 the battle is over
        elif hp_lyn <= 0 and hp_bandit > 0:
            game_over = True
            combat = False

        else: 
            # Enemy Turn
            print("It's the enemy turn!")
            enemy_IA = random.randint(1, 3)
            
            # Enemy Attacking the Player
            if enemy_IA == 1 or enemy_IA == 2:
                random_multiplier = random.randint(1, 3)
                total_damage = axe_damage - random_multiplier

                print("The enemy swings it's axe! " + str(total_damage) + " HP lost!")
                hp_lyn = hp_lyn - total_damage

            elif enemy_IA == 3:
                num_attacks = random.randint(2, 4)
                print("The enemy strikes you with several attacks!")
                for i in range(1, num_attacks + 1):
                    strike_damage = random.randint(1, 5)
                    print(str(strike_damage) + " HP lost!")
                    hp_lyn = hp_lyn - strike_damage

if game_over is True:
    print(str(character_2) + ' has fainted!')
    print('You lose...')
    input()
    print('GAME OVER')

else:
    print('Lyn: Victory!')
    input()
    print("But I've been injured.")
    input()
    print("I have need of a vulnerary.")
    print('Heal ' + str(character_2) + '? 1) Yes | 2) No ')
    heal = int(input(''))
    while heal != 1 and heal != 2:
        print("ERROR: Wrong input: Please choose between 1 or 2")
        print('Heal ' + str(character_2) + '? 1) Yes | 2) No ')
        heal = int(input(''))

    if heal == 1 and vulnerary != 0:
        random_multiplier = random.randint(1, 3)
        total_heal = 15 + random_multiplier

        print(str(player) + ' uses a vulnerary!')
        vulnerary = vulnerary - 1
        hp_lyn = hp_lyn + total_heal
        print(str(character_2) + ' recovers ' + str(total_heal) + ' HP!')
        # To prevent the player has more hp than the max
        if hp_lyn > 32:
            hp_lyn = 32
        print(str(character_2) + ": Thank you " + str(player) + "! Now let's go get that brigand over by the ger!")
        input()
                
    elif heal == 2:
        print(str(character_2) + ": Let's go get that brigand over by the ger!")
        input()

    elif vulnerary == 0:
        print('You ran out of vulneraries!')
        print(str(character_2) + ": Let's go get that brigand over by the ger!")
        input()

    print("(You reach finally to the bandits base.) ")
    input()
    print("??: Who do you think you are? ")
    input()
    print("??: You think you can stand up to Batta the Beast?")
    input()

    # Combat Nº2 
    print("You encounter with the leader of the bandits!")
    combat = True
    while combat is True:
        # Checks if the player has HP left and the enemy doesn't have HP left
        if hp_banditleader <= 0 and hp_lyn > 0:
            print('The enemy has been defeated')
            print('You won!')
            input()
            
            combat = False
        # Checks if the player HP is 0 the battle is over
        elif hp_lyn <= 0 and hp_banditleader > 0:
            game_over = True
            combat = False
        else: 

            if hp_lyn <= 10:
                print("Lyn: Whew! He's tough...")
                input()
                print("It all comes down to this next blow.")
                input()
                print(str(player) + ", if I fall, I want you to flee. You must escape! ")
                input()
                 # Menu
                print()
                print('---- ' + str(character_2) + ' ----')
                print('---- HP: 32/' + str(hp_lyn) +  ' ----')
                print('---- Actions: 1) Attack  ----')
                attack = int(input('---- Choose an option: '))
                while attack != 1:
                    print("ERROR: Choose an option")
                    attack = int(input('---- Choose an option: '))
                if attack == 1:
                    critical_hit = random.randint(2, 3)
                    random_multiplier = random.randint(1, 3)
                    total_damage = (critical_hit * sword_damage) - random_multiplier
                    print("!!!")
                    print(str(character_2) + ' used all her strength in one blow! ' + str(total_damage) + ' HP!')
                    hp_banditleader = hp_banditleader - total_damage
                
            # Menu
            else:
                print()
                print('---- ' + str(character_2) + ' ----')
                print('---- HP: 32/' + str(hp_lyn) +  ' ----')
                print('---- Actions: 1) Attack | 2) Heal ----')
                attack = int(input('---- Choose an option: '))
                while attack != 1 and attack != 2:
                        print("ERROR: Choose an option")
                        attack = int(input('---- Choose an option: '))
                    
                # Player Attacking the Enemy
                if attack == 1:
                    random_multiplier = random.randint(1, 3)
                    total_damage = sword_damage - random_multiplier

                    print(str(character_2) + ' slashes the enemy! ' + str(total_damage) + ' HP!')
                    hp_banditleader = hp_banditleader - total_damage
                    
                #Player healing itself 
                elif attack == 2 and vulnerary != 0:
                    random_multiplier = random.randint(1, 3)
                    total_heal = 15 + random_multiplier

                    print(str(player) + ' uses a vulnerary!')
                    vulnerary = vulnerary - 1
                    hp_lyn = hp_lyn + total_heal
                    print(str(character_2) + ' recovers ' + str(total_heal) + ' HP!')
                    # To prevent the player has more hp than the max
                    if hp_lyn > 32:
                        hp_lyn = 32
                
                elif vulnerary <= 0:             
                    print('You ran out of vulneraries!')
            
        # Checks if the player has HP left and the enemy doesn't have HP left
        if hp_banditleader <= 0 and hp_lyn > 0:
            print('Batta: What?')
            print('How... How did you... ')
            input()
            print("You won!")
            combat = False
        
        # Checks if the player HP is 0 the battle is over
        elif hp_lyn <= 0 and hp_banditleader > 0:
            game_over = True
            combat = False

        else: 
            # Enemy Turn
            print("It's the enemy turn!")
            enemy_IA = random.randint(1, 3)
            
            # Enemy Attacking the Player
            if enemy_IA == 1 or enemy_IA == 2:
                random_multiplier = random.randint(1, 3)
                total_damage = axe_damage - random_multiplier

                print("The enemy swings it's axe! " + str(total_damage) + " HP lost!")
                hp_lyn = hp_lyn - total_damage

            elif enemy_IA == 3:
                num_attacks = random.randint(2, 4)
                print("The enemy strikes you with several attacks!")
                for i in range(1, num_attacks + 1):
                    strike_damage = random.randint(1, 5)
                    print(str(strike_damage) + " HP lost!")
                    hp_lyn = hp_lyn - strike_damage
    
    if game_over is True:
        print(str(character_2) + ' has fainted!')
        print('You lose...')
        input()
        print('GAME OVER')
    else: 
        input()
        print('Lyn: Whew...')
        print('That was close. ')
        input()
        print("I sorely underestimated him")
        print("Sorry if I worried you.")
        input()
        print("I'll need to be stronger if I'm going to survive... Strong enough that no one can defeat me.")
        input()
        print("Good work, " + str(player) + "! Let's go home.")
        input()
        print("That fight must have taken a lot out of you.")
        input()
        print("You have some experience in the ways of the war, I can see.")
        answer = input("Would you allow me to travel with you? (Yes/No) ")
        while answer is '' and answer is not 'Yes' and answer is not 'No':
            print("Please insert Yes or No. ")
            answer = input("Would you allow me to travel with you? (Yes/No) ")
        if answer == 'Yes':
            print("What? You... want me to get permission from my parents?")
            input()
            print("My mother and my father died six months ago.")
            input()
            print("My people the Lorca they don't... I'm the last of my tribe.")
            input()
            print("The apprentice tactician " + str(player) + " and the young swordfighter " + str(character_2) + ".")
            print("A strange pair on an even stranger journey.")
            input()
            print("Chapter 0 ends.")
            input()
        elif answer == 'No':
            print("I see... I pray for your safety then, " + str(player) + ".")
    


    
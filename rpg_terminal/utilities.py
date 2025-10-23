import os
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

#Combat system
def combatSystem(player, enemy):
    clear_console()
    #Check the enemy type you encounter
    if player.health > 0:
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
            player.heal()
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
        say(f'Oh no! {player.name} has collapsed!')
        return False
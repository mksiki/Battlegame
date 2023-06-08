# Author: Jesus Antonio
# About: This is a game that allows the user to select a
# character, and then fights a dragon to the death.

from random import randint
print("Welcome to the Battle Game!")


# print("Welcome to Battle Game!!")

print("""

________                                         ________                       
\______ \____________     ____   ____   ____    /  _____/_____    _____   ____  
 |    |  \_  __ \__  \   / ___\ /  _ \ /    \  /   \  ___\__  \  /     \_/ __ \ 
 |    `   \  | \// __ \_/ /_/  >  <_> )   |  \ \    \_\  \/ __ \|  Y Y  \  ___/ 
/_______  /__|  (____  /\___  / \____/|___|  /  \______  (____  /__|_|  /\___  >
        \/           \//_____/             \/          \/     \/      \/     \/ 

        

                      ,-'`\\
                  _,"'    j
           __....+       /               .
       ,-'"             /               ; `-._.'.
      /                (              ,'       .'
     |            _.    \             \   ---._ `-.
     ,|    ,   _.'  Y    \             `- ,'   \   `.`.
     l'    \ ,'._,\ `.    .              /       ,--. l
  .,-        `._  |  |    |              \       _   l .
 /              `"--'    /              .'       ``. |  )
.\    ,                 |                .        \ `. '
`.                .     |                '._  __   ;. \'
  `-..--------...'       \                  `'  `-"'.  \\
      `......___          `._                        |  \\
               /`            `..                     |   .
              /|                `-.                  |    L
             / |               \   `._               .    |
           ,'  |,-"-.   .       .     `.            /     |
         ,'    |     '   \      |       `.         /      |
       ,'     /|       \  .     |         .       /       |
     ,'      / |        \  .    +          \    ,'       .'
    .       .  |         \ |     \          \_,'        / j
    |       |  L          `|      .          `        ,' '
    |    _. |   \          /      |           .     .' ,'
    |   /  `|    \        .       |  /        |   ,' .'
    |   ,-..\     -.     ,        | /         |,.' ,'
    `. |___,`    /  `.   /`.       '          |  .'
      '-`-'     j     ` /."7-..../|          ,`-'
                |        .'  / _/_|          .
                `,       `"'/"'    \          `.
                  `,       '.       `.         |
             __,.-'         `.        \'       |
            /_,-'\          ,'        |        _.
             |___.---.   ,-'        .-':,-"`\,' .
                  L,.--"'           '-' |  ,' `-.\\
                                        `.' 


""")

wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
wizard_damage = 150

elf_hp = 100
elf_damage = 100

human_hp = 150
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    choice = input("Choose your character: ")

    if choice == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif choice == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif choice == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Choose a valid selection: ")
print()
print(
    f"You have chosen the character: {character} \nHealth: {my_hp}\nDamage: {my_damage}")
print()

while True:
    dragon_hp -= my_damage
    print(
        f"The {character}, damaged the Dragon!\nThe Dragon's health is: {dragon_hp}")
    print()

    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_hp -= dragon_damage
    print(
        f"The Dragon strikes back at the {character}!\nThe {character}'s health is: {my_hp} ")
    print()

    if my_hp <= 0:
        print("Your character has lost the battle!")
        break

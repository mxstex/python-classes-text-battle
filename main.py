# ------------ imports ------------
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword

# ------------ setup ------------
game_loop = True
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

# ------------ game loop ------------
while game_loop:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    if enemy.health == 0 or hero.health == 0:
        print("End")
        game_loop = False

    # input()

from time import sleep
from random import randint

from bestiary.knight import Knight
from bestiary.dragon import Dragon

from weaponry.sword import Sword
from weaponry.shield import Shield
from weaponry.crossbow import Crossbow

import volume_of_poems


print("🥀 Баллада о драконе, рыцаре и ООП 🥀")

# Слово о бестии 🥀
volume_of_poems.dragons_legend()
dragon = Dragon()

# Слово об имени 🥀
print()
print("Ужасной твари вызов бросил — великий рыцарь, храбрый воин")
try:
    hero: Knight = Knight("Росс Ван Гвидо")
except TypeError:
    volume_of_poems.are_you_still_a_knight()
try:
    print(f"И звали его {hero.name}, и имени он был достоин!")
except AttributeError:
    volume_of_poems.knight_without_a_name()
######################################################

# Слово о здоровье 🥀
print("Родился в знатном доме он, жил на раздолье")
try:
    if hero.health.check() == 100:
        print("Он фехтованью обучился, и был хорош здоровьем")
    else:
        volume_of_poems.are_you_still_a_human()
except AttributeError:
    volume_of_poems.spoiled_health()

######################################################

# Слово о мече 🥀
print()
print("Намеревался он сразить мечом дракона,")
print("И звался меч его...", end="")
try:
    hero.equipment.sword = Sword(ranged=False,
                                 damage=10,
                                 name=Knight.NOBLE_SWORD_NAME)
    print(" " + hero.equipment.sword.name + "!")
except AttributeError:
    volume_of_poems.inglorious_fate("sword")
######################################################

# Слово о щите 🥀
print("В другой руке его был щит стальной с гербом короны")
hero.equipment.shield = Shield()
print("Прикинул щит в руке... ", end="")
try:
    if hero.check_shield():
        print("Послужит он для обороны! ")
    else:
        print("Ох... щит его разорван")
        volume_of_poems.inglorious_fate("shield")
except AttributeError:
    volume_of_poems.the_shield_of_crown()
######################################################

# Слово об арбалете 🥀
print()
print("На поясе, на всякий случай, нет-нет и да, авось да-да и нет")
print("Наш воин бравый, рыцарь мощный, повесил мини-арбалет")
hero.equipment.crossbow = Crossbow(True, 10)
print("И зарядил в него он три болта")
try:
    hero.loads_crossbow(bolts=3)
    if len(hero.equipment.crossbow) != 3:
        volume_of_poems.uneducated_shameful_death()
except AttributeError:
    volume_of_poems.inglorious_fate("crossbow")
print("Дракон повержен будет, пусть полетит хоть сволота")
######################################################

# Слово о битве 🥀
volume_of_poems.dragon_comes()

print()
print("И хоть на поединок с тварью вышел,\n"
      "Представиться велит закон,\n"
      "Узри же, слушай быдло,")
if str(hero) != f"Вот я — {hero.name}, мой меч — {hero.equipment.sword.name}!":
    volume_of_poems.forgotten_himself()
print(hero)  # "Вот я — {имя}, мой меч — {имя_меча}!"
print("А ныне перечислю славных родичей моих!")

for elder in ["Пандас Ван Гвидо", "Джанго Ван Гвидо", "Фласк Ван Гвидо"]:
    result = ""
    try:
        result = Knight.pronoun_an_elder(elder)
    except AttributeError:
        volume_of_poems.forgotten_his_roots()
    expected = f"Мой славный предок, рыцарь {elder}"
    if result == expected:
        print(result)
    else:
        volume_of_poems.forgotten_his_roots()

print("Умри дракон!")

######################################################
###   Код дальше не дает информации для задания,   ###
### это концовка истории, которую мы с вами писали ###
######################################################


def dragon_attacks(knight: Knight, dragon_attack: int, attack_type: str):
    if knight.equipment.shield.health.alive:
        knight.equipment.shield.health.damaged(dragon_attack)
        if attack_type == "claws":
            print(f"🐉 🛡️ Не дремлет бестия... Терзает щит когтями на {dragon_attack} очков урона")
        else:
            print(f"🔥 🛡 Не дремлет бестия... Огнем жжет щит на {dragon_attack} очков урона")
    else:
        knight.health.damaged(dragon_attack)
        if attack_type == "claws":
            print(f"🐉 Не дремлет бестия... Бьёт рыцаря когтями на {dragon_attack} очков урона ")
        else:
            print(f"🔥 Не дремлет бестия... Огнем жжет рыцаря на {dragon_attack} очков урона ")


for i in range(3):
    print("...")
    sleep(0.5)
print("🥀")
sleep(2)

print()
while hero.health.alive and dragon.health.alive:
    if not dragon.is_flying:
        heros_strike = hero.equipment.sword.deal_damage()
        dragon.health.damaged(heros_strike)
        sleep(0.5)
        print(f"🗡️ Размах меча, "
              f"отважный рыцарь тварь увечит — {heros_strike} очков урона")

        if not dragon.health.alive: break
        dragon_attacks(hero, dragon.claws.double_attack(), "claws")
        dragon.is_it_time_to_fly()
    else:
        heros_shot = hero.equipment.crossbow.shoot()
        dragon.health.damaged(heros_shot)
        sleep(0.5)
        print(f"🏹 Тяжелый воздух рассекает болт, "
              f"отважный рыцарь тварь увечит — {heros_shot} очков урона")

        if not dragon.health.alive and randint(1, 10) % 2 == 0:
            break
        else:
            print("Последнее дыханье бестии — огонь 🔥")
        dragon_attacks(hero, dragon.fire.shoot(), "fire")

    print(f"Рыцарь: {hero.health.check()}", end="")
    print(f" + 🛡️{hero.equipment.shield.health.check()}" if hero.equipment.shield.health.alive else "")
    print(f"Дракон: {dragon.health.check()}")
    sleep(0.5)

if not hero.health.alive and not dragon.health.alive:
    volume_of_poems.both_dead()
elif not hero.health.alive:
    volume_of_poems.hero_is_dead()
elif not dragon.health.alive:
    volume_of_poems.dragon_is_dead()

volume_of_poems.coda()

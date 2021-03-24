# Assignment Name: Repetition Assignment
# Question Number: 2
# 
# TODO: Jonathan Joestar and Joseph Joestar get into a heated argument and decide
# to spar it out. Jonathan Joestar can take a hit like a champ, as he has 800 
# hit points, while Joseph only has 200 hit points. What Joseph lacks in tankiness
# he makes up for in damage. Joseph can deal damage consistently between 75 to 125.
# This means that Joseph can reduce Jonathan’s hitpoints randomly between 75 to 125.
# Jonathan can only deal between 10 to 40 damage. Create a looped game where they
# fight until one gets knocked out. In each round, each player only gets to attack 
# once, but the first one to land the punch is random. Both players cannot be
# knocked out at the end of the round. Output the health of each character at the 
# end of each round and how much damage their attack does.

# date and time completed: 2021-03-23 9:22
import random

JonathanHP = 800 # Jonathan's hit points
JosephHP = 200 # Joseph's hit points

def battle(fighter1, fighter2, fighter1HP, fighter1DMG, fighter2HP, fighter2DMG):
    '''Calculates the damage dealt by each fighter in each round. The fighter1
parameter takes the name of the fighter dealing the first punch, as an argument.
The fighter2 parameter takes the same thing, except is the name of the fighter 
that takes the second punch, that is, if they are even alive by then. The 
fighter1HP and fighter2HP parameters take each fighters remaining HP as an argument.
The fighter1DMG and fighter2DMG parameters take each fighters possible damage dealing points 
as an argument. At the end, returns the value of both fighters HP to be stored as
global variables'''
    fighter2HP -= fighter1DMG
    print(f'{fighter1} attacked first, dealing {fighter1DMG} DMG')
    if fighter2HP > 0:
        fighter1HP -= fighter2DMG
        print(f'{fighter2} attacked next, dealing {fighter2DMG} DMG')
    return fighter1HP, fighter2HP

# While both fighters HP are above 0, outputs the health of each fighter at the end
# of each round and how much damage their attack does.
while JosephHP > 0 and JonathanHP > 0:
    JonathanDMG = random.randrange(10, 40) # Possible amount of damage Jonathan can deal
    JosephDMG = random.randrange(75, 125) # Possible amount of damage Joseph can deal
    punchChance = random.randrange(0, 2) # punchChance is used to randomize who lands the first punch
    if punchChance == 0: # If punchChance == 0, Jonathan attacks first
        JonathanHP, JosephHP = battle('Jonathan', 'Joseph', JonathanHP, JonathanDMG, JosephHP, JosephDMG)
    elif punchChance == 1: # If punchChance == 1, Joseph attacks first
        JosephHP, JonathanHP = battle('Joseph', 'Jonathan', JosephHP, JosephDMG, JonathanHP, JonathanDMG)
    if JonathanHP < 0 or JosephHP < 0:
        if JonathanHP < 0:
            print(f'Jonathan HP: 0\nJoseph HP: {JosephHP}\n')
        if JosephHP < 0:
            print(f'Jonathan HP: {JonathanHP}\nJoseph HP: 0\n')
    else:
        print(f'Jonathan HP: {JonathanHP}\nJoseph HP: {JosephHP}\n')
else: # As soon as one fighter reaches 0HP, prints the winner and loser. 
    if JonathanHP < 0 and JosephHP > 0:
        print("Jonathan is KO'd\nJoseph WINS!")
    if JosephHP < 0 and JonathanHP > 0:
        print("Joseph is KO'd\nJonathan WINS!")
    
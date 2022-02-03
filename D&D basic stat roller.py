import random

class dice(object):
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def roll_die(self):
        return(random.randint(1, self.sides))

d2 = dice("d2",2)
d4 = dice("d4",4)
d6 = dice("d6",6)
d10 = dice("d10",10)
d12 = dice("d12",12)
d20 = dice("d20",20)
d100 = dice("d100",100)

"""""
roll_die = input("Enter dice to roll: ") 

if roll_die == "d2":
    d2.roll_die()
elif roll_die == "d4":
    d4.roll_die()
elif roll_die == "d6":
    d6.roll_die()
elif roll_die == "d10":
    d10.roll_die()
elif roll_die == "d12":
    d12.roll_die()
elif roll_die == "d20":
    d20.roll_die()
elif roll_die == "d100":
    d100.roll_die()
else:
    print("Invalid input!")
"""""
    #There are six ability scores: 
    # Strength, 
    # Dexterity, 
    # Constitution, 
    # Intelligence, 
    # Wisdom,
    # Charisma.
    
class character():
    def __init__ (self, first_name, last_name, class_, level, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.first_name = first_name
        self.last_name = last_name
        self.class_ = class_
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
    
SteveParker = character("Steve", "Parker", "Bard", "1", "10", "10" ,"10" , "10" , "10" , "10")

print("Tuning Strings")
print("")

SteveParker.strength = d20.roll_die()
SteveParker.dexterity = d20.roll_die()
SteveParker.constitution = d20.roll_die()
SteveParker.intelligence = d20.roll_die()
SteveParker.wisdom = d20.roll_die()
SteveParker.charisma = d20.roll_die()

print(SteveParker.first_name, SteveParker.last_name, "is a level ", SteveParker.level, SteveParker.class_)
print("His Strength is " + str(SteveParker.strength) + " his dexterity is " + str(SteveParker.dexterity), "his constitution is " + str(SteveParker.constitution))
print("His intelligence is " + str(SteveParker.intelligence), "his wisdom is " + str(SteveParker.wisdom), "his charisma is " + str(SteveParker.charisma))
print("HP " + str(SteveParker.strength))
print("Ooo err I am so posh")

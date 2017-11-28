from random import *

class Soldiers:
# Býr til vopn fyrir hermenina
    def weaponstats(self):
        if self.weapon == 1:
            return "Vibro-blade"
        elif self.weapon == 2:
            return "Electrostaff"
        elif self.weapon == 3:
            return "Blaster"
        elif self.weapon == 4:
            return "Sniper"
        elif self.weapon == 5:
            return "Lightsaber"
        elif self.weapon == 6:
            return "Heavy Blaster pistol"
        elif self.weapon == 7:
            return "Bowcaster"
        elif self.weapon == 8:
            return "Wrist rockets"
        elif self.weapon == 9:
            return "Disruptor"
        elif self.weapon == 10:
            return "Force pike"
        elif self.weapon == 11:
            return "Vibro-az"
        elif self.weapon == 12:
            return "Ion Blaster"
        elif self.weapon == 13:
            return "Minigun"
        elif self.weapon == 14:
            return "Thermal detonator"
        else:
            return "BOII THAT AINT A WEAPON THAT WE HAVE!"

        return "Unknown"
    #setur líf, kraft og vopn fyrir hermenina
    def __init__(self, name, live=0, weapon=1, power=0):
        self.name = name
        self.live = live
        self.weapon = weapon
        self.power = power
        self.weaponname = self.weaponstats()

    def printsoldier(self):
        return self.name + ' Weapon: ' + self.weaponname + ' Power: ' + str(self.power) + ' Live:  ' + str(self.live)